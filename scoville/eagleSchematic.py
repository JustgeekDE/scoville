import copy
from lxml import etree

class SchematicParsingException(Exception):
  pass

class EaglePart:
  def __init__(self, partNode, schematic):
    self.attributes = {}

    self.xml = partNode
    self.name = partNode.get('name')
    self.value = partNode.get('value')

    self.libraryName = partNode.get('library')
    self.devicesetName = partNode.get('deviceset')
    self.deviceName = partNode.get('device')
    self.technologyName = partNode.get('technology')

    self.attributes = self._extractAttributes(schematic)
    self.netMap = self._extractNetMap(schematic)
    self.gates = self._extractGates(schematic)

    pass

  def _extractGates(self, schematic):
    result = {}
    queryString = ".//instance[@part='{name}']".format(name=self.name)
    for element in schematic.findall(queryString):
      result[element.get('gate')] = element
    return result


  def _extractAttributes(self, schematic):
    technology = self.getTechnologyValue(schematic, self.technologyName)

    if technology == None:
      technology = self.getTechnologyValue(schematic, "DEFAULT")

    if technology == None:
      technology = self.getTechnologyValue(schematic, "")

    if technology == None:
      raise SchematicParsingException("Can't find correct attributes for part {}".format(self.name))

    attributes = {}
    for element in technology.findall('attribute'):
      attributes[element.get('name')] = element.get('value')

    return attributes

  def getTechnologyValue(self, schematic, technologyName):
    technologyPathString = "./libraries/library[@name='{library}']/devicesets/deviceset[@name='{deviceset}']/devices/device[@name='{device}']/technologies/technology[@name='{technology}']"
    return schematic.find(
        technologyPathString.format(library=self.libraryName, deviceset=self.devicesetName, device=self.deviceName,
                                    technology=technologyName))

  def _extractNetMap(self, schematic):
    nets = schematic.findall('.//net')
    netMap = {}

    for net in nets:
      pinrefs = net.findall('.//pinref')
      for pinref in pinrefs:
        if pinref.get('part') == self.name:
          netMap[pinref.get('pin')] = net.get('name')

    return netMap

  def getSpiceNetlist(self):
    spicePrefix = self.getAttribute("SV_SPICE_PREFIX")

    if spicePrefix == None:
      return None

    spiceOrder = self.getAttribute("SV_SPICE_ORDER").split(';')

    netList = ''
    for pin in spiceOrder:
      netList += self.netMap[pin] + ' '

    return spicePrefix + self.name + ' ' + netList + self.value

  def getSpiceModel(self):
    spiceModel = self.getAttribute("SV_SPICE_MODEL")

    if spiceModel == None:
      return None

    return '.model ' + self.value + ' ' + spiceModel

  def getSpiceSupply(self):

    if self.libraryName not in ['supply1', 'supply2']:
      return None

    if 'GND' in self.devicesetName:
      return None

    voltage = self.devicesetName
    name = voltage.replace('+', 'P').replace('-', 'M')
    connection = ' '.join(self.netMap.values())

    return 'V' + name + ' ' + connection + ' GND dc ' + voltage + ' ac 0V'

  def getSpiceSubCircuit(self):
    subCircuitData = self.getAttribute("SV_SPICE_SUBCKT")

    if subCircuitData == None:
      return None

    subCircuitData = subCircuitData.replace("\\n", "\n")
    subCircuitData = subCircuitData.replace('%NAME%', self.value)
    return subCircuitData

  def getAttribute(self, attributeName):
    try:
      return self.attributes[attributeName]
    except KeyError:
      pass
    return None

  def rename(self, newName):
    self.name = newName
    self.xml.set('name', newName)
    for gate in self.gates.values():
      gate.set('part', newName)


class EagleLibrary:
  def __init__(self, libraryNode):
    self.name = libraryNode.get('name')
    self.xml = libraryNode
    pass


class EagleSchematic:
  def __init__(self, xmlString):
    tree =  etree.fromstring(xmlString, etree.XMLParser(remove_blank_text=True))

    self.xml = tree

    self.settings = tree.find('./drawing/settings')
    self.grid = tree.find('./drawing/grid')
    self.layers = tree.find('./drawing/layers')

    schematic = tree.find('./drawing/schematic')
    self.libraries = self._parseLibraries(schematic)
    self.parts = self._parseParts(schematic)

  def _parseLibraries(self, rootNode):
    libraries = {}
    for libraryNode in rootNode.findall('.//library'):
      library = EagleLibrary(libraryNode)
      libraries[library.name] = library

    return libraries

  def _parseParts(self, rootNode):
    parts = {}
    for partNode in rootNode.findall('.//part'):
      part = EaglePart(partNode, rootNode)
      parts[part.name] = part

    return parts

  def getSpiceData(self):
    netLists = set()
    models = set()
    voltageSources = set()
    subCircuits = set()

    for part in self.parts.values():
      self.addIfNotNone(voltageSources, part.getSpiceSupply())
      self.addIfNotNone(netLists, part.getSpiceNetlist())
      self.addIfNotNone(models, part.getSpiceModel())
      self.addIfNotNone(subCircuits, part.getSpiceSubCircuit())

    netList = "\n".join(netLists)
    models = "\n".join(models)
    voltageSources = "\n".join(voltageSources)
    subCircuits = "\n".join(subCircuits)

    return voltageSources + "\n" + netList + "\n" + models + "\n" + subCircuits + "\n.end"

  def toString(self):
    return etree.tostring(self.xml, pretty_print=True)

  def replace(self, deviceSet, replacementSchematic):
    self._replaceLibraries(replacementSchematic.libraries)
    for oldPart in self.parts.values():
      if oldPart.devicesetName == deviceSet:
        newSchematic = copy.deepcopy(replacementSchematic)
        self._replaceSinglePart(newSchematic, oldPart)
    pass

  def _replaceLibraries(self, newLibraries):
    self.libraries.update(newLibraries)
    libraryNode = self.xml.find('./drawing/schematic/libraries')
    libraryNode.clear()
    for library in self.libraries.values():
      libraryNode.append(library.xml)

  def _replaceSinglePart(self, replacementSchematic, oldPart):
    self.parts.pop(oldPart.name)
    for newPart in replacementSchematic.parts.values():
      newPart.rename(oldPart.name + '-' + newPart.name)
      self.parts[newPart.name] = newPart

    self._rebuildPartTree()

  def _rebuildPartTree(self):
    partsNode = self.xml.find('./drawing/schematic/parts')
    partsNode.clear()
    for part in self.parts.values():
      partsNode.append(part.xml)
    self._replaceInstanceTree()

  def _replaceInstanceTree(self):
    instanceNode = self.xml.find('.//instances')
    instanceNode.clear()
    for part in self.parts.values():
      for instance in part.gates.values():
        instanceNode.append(instance)

  @staticmethod
  def addIfNotNone(collection, value):
    if value != None:
      collection.add(value)

