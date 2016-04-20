from lxml import etree

import schematicTransformations
import eagleLibrary

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
      net = self.netMap[pin]
      net = net.replace('-', '_')
      netList += net + ' '

    name = self.name.replace('-', '_')

    return spicePrefix + name + ' ' + netList + self.value

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

  def getRotation(self):
    rotation = 0
    for gate in self.gates.values():
      rot = gate.get('rot')
      if rot != None:
        rotation = int(rot[1:])
    return rotation

  def getPosition(self):
    position = (0,0)
    for gate in self.gates.values():
      x = float(gate.get('x'))
      y = float(gate.get('y'))
      position = (x,y)
    return position


class EagleSchematic:
  def __init__(self, xmlString):
    tree =  etree.fromstring(xmlString, etree.XMLParser(remove_blank_text=True))

    self.xml = tree

    self.settings = tree.find('./drawing/settings')
    self.grid = tree.find('./drawing/grid')
    self.layers = tree.find('./drawing/layers')

    schematic = tree.find('./drawing/schematic')
    self.libraries = eagleLibrary.parseLibraries(self.xml)
    self.parts = self._parseParts(schematic)

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
        newSchematic = replacementSchematic.deepCopy()

        rotation = schematicTransformations.SchematicRotation(oldPart.getRotation())
        translation = schematicTransformations.SchematicTranslation(oldPart.getPosition())

        newSchematic = rotation.transform(newSchematic)
        newSchematic = translation.transform(newSchematic)

        newSchematic.prefixParts(oldPart.name + '-')

        self._replaceDocu(newSchematic)
        self._replaceSinglePart(newSchematic, oldPart)
        self._replaceNets(newSchematic, oldPart)

    pass

  def prefixParts(self, prefix):
    for part in self.parts.values():
      oldName = part.name
      newName = prefix + oldName

      partRefs =  self.xml.findall(".//pinref[@part='{partName}']".format(partName=oldName))
      for ref in partRefs:
        ref.set('part', newName)
      part.rename(newName)

    self._rebuildPartTree()


  def _replaceLibraries(self, newLibraries):
    self.libraries = eagleLibrary.mergeLibraryLists(self.libraries, newLibraries)

    libraryNode = self.xml.find('./drawing/schematic/libraries')
    libraryNode.clear()
    for library in self.libraries.values():
      library = library.deepCopy()
      libraryNode.append(library.xml)

  def _replaceSinglePart(self, replacementSchematic, oldPart):
    self.parts.pop(oldPart.name)
    for newPart in replacementSchematic.parts.values():
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

  def _replaceNets(self, replacementSchematic, oldPart):
    replacedNets = []
    pinRefs =  self.xml.findall(".//pinref[@part='{partName}']".format(partName=oldPart.name))
    for refNode in pinRefs:
      pin = refNode.get('pin')
      replacementNet = replacementSchematic.getNet(pin)
      if replacementNet != None:
        replacementSegments = replacementNet.findall('.//segment')
        for segment in replacementSegments:
          for connection in segment.getchildren():
            refNode.getparent().append(connection)

        refNode.getparent().remove(refNode)
        replacedNets.append(pin)

    newNets = replacementSchematic.getNets()
    for net in newNets:
      oldName = net.get('name')
      if oldName not in replacedNets:
        newName = oldPart.name + '-' + oldName
        net.set('name', newName)
        self.addNet(net)

  def _replaceDocu(self, replacementSchematic):
    self.addDocu(replacementSchematic.getDocu())

  def getDocu(self):
    return self.xml.findall(".//plain/")

  def addDocu(self, newDocu):
    docuNode = self.xml.find(".//plain")
    for newNode in newDocu:
      docuNode.append(newNode)

  def getNets(self):
    return self.xml.findall(".//net")

  def getNet(self, netName):
    return self.xml.find(".//net[@name='{partName}']".format(partName=netName))

  def addNet(self, netNode):
    parent = self.xml.find(".//nets")
    parent.append(netNode)

  def getLibraries(self):
    return self.libraries

  def deepCopy(self):
    originalXMLString = self.toString()
    return EagleSchematic(originalXMLString)

  @staticmethod
  def addIfNotNone(collection, value):
    if value != None:
      collection.add(value)

