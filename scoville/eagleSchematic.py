import xml.etree.ElementTree as XML


class SchematicParsingException(Exception):
  pass


class EaglePart:
  def __init__(self, partNode, schematic):
    self.attributes = {}
    self.gates = {}

    self.xml = partNode
    self.name = partNode.get('name')
    self.value = partNode.get('value')

    self.libraryName = partNode.get('library')
    self.devicesetName = partNode.get('deviceset')
    self.deviceName = partNode.get('device')
    self.technologyName = partNode.get('technology')

    self.attributes = self._extractAttributes(schematic)
    self.netMap = self._extractNetMap(schematic)
    pass

  def _extractAttributes(self, schematic):
    technology = self.method_name(schematic, self.technologyName)

    if technology == None:
      technology = self.method_name(schematic, "DEFAULT")

    if technology == None:
      technology = self.method_name(schematic, "")

    if technology == None:
      raise SchematicParsingException("Can't find correct attributes for part {}".format(self.name))

    attributes = {}
    for element in technology.findall('attribute'):
      attributes[element.get('name')] = element.get('value')

    return attributes

  def method_name(self, schematic, technologyName):
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


class EagleLibrary:
  def __init__(self, libraryNode):
    self.name = libraryNode.get('name')
    self.xml = libraryNode
    pass


class EagleSchematic:
  def __init__(self, xmlString):
    tree = XML.fromstring(xmlString)

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

    for part in self.parts.values():
      self.addIfNotNone(voltageSources, part.getSpiceSupply())
      self.addIfNotNone(netLists, part.getSpiceNetlist())
      self.addIfNotNone(models, part.getSpiceModel())

    netList = "\n".join(netLists)
    models = "\n".join(models)
    voltageSources = "\n".join(voltageSources)

    return voltageSources + "\n" + netList + "\n" + models + "\n.end"

  @staticmethod
  def addIfNotNone(collection, value):
    if value != None:
      collection.add(value)
