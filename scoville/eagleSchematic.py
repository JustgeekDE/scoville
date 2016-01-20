from xml.dom.minidom import parse, parseString

class EagleSchematic:
  def __init__(self, xmlString):
    self.xml = parseString(xmlString)


  def getSpiceData(self):
    netLists = []
    models = set()

    parts = self._getParts()
    for part in parts:

      netList = self._getSpiceNetlistForPart(part)
      if netList != None:
        netLists.append(netList)

      model = self._getSpiceModelForPart(part)
      if model != None:
        models.add(model)

    netList = "\n".join(netLists)
    models = "\n".join(models)

    return netList + "\n" + models

  def _getParts(self):
    return self.xml.getElementsByTagName('part')

  def _getDevices(self):
    return self.xml.getElementsByTagName('deviceset')

  def _getDeviceAttributes(self, part):
    library = self._getNodeWithTagAndName('library', part.getAttribute('library'))
    deviceset = self._getNodeWithTagAndName('deviceset', part.getAttribute('deviceset'), library)
    device = self._getNodeWithTagAndName('device', part.getAttribute('device'), deviceset)
    technology = self._getNodeWithTagAndName('technology', part.getAttribute('technology'), device)

    if technology == None:
      technology = device.getElementsByTagName('technology')[0]

    if technology != None:
      return technology.getElementsByTagName('attribute')

    return []

  def _getSpiceNetlistForPart(self, part):
    if self._getSpiceSupplyForPart(part) != None:
      return None

    netMap = self._getNetMapForPart(part)
    spicePrefix = self._getAttributeValueForPart(part, "SV_SPICE_PREFIX")
    spiceOrder = self._getAttributeValueForPart(part, "SV_SPICE_ORDER").split(';')
    partName = part.getAttribute('name')
    partValue = part.getAttribute('value')

    netList = ''
    for pin in spiceOrder:
      netList += netMap[pin] + ' '

    return spicePrefix + partName + ' ' + netList + partValue

  def _getSpiceSupplyForPart(self, part):
    partLibrary = part.getAttribute('library')
    if partLibrary not in ['supply1', 'supply2']:
      return None

    voltage = part.getAttribute('deviceset')
    name = voltage.replace('+', 'P').replace('-', 'M')
    connection = ' '.join(self._getNetMapForPart(part).values())


    return 'V'+name+' '+ connection + ' GND dc ' + voltage + ' ac 0V'


  def _getAttributeValueForPart(self, part, attributeName):
    attributes = self._getDeviceAttributes(part)
    for attribute in attributes:
      if attribute.getAttribute('name') == attributeName:
        return attribute.getAttribute('value')

    return ""

  def _getNetMapForPart(self, part):
    nets = self.xml.getElementsByTagName('net')
    netMap = {}

    for net in nets:
      pinrefs = net.getElementsByTagName('pinref')
      for pinref in pinrefs:
        if pinref.getAttribute('part') == part.getAttribute('name'):
          netMap[pinref.getAttribute('pin')] = net.getAttribute('name')


    return netMap

  def _getSpiceModelForPart(self, part):
    spiceModel = self._getAttributeValueForPart(part, 'SV_SPICE_MODEL')

    if spiceModel == '':
      return None

    partValue = part.getAttribute('value')

    return '.model ' + partValue + ' ' + spiceModel

  def _getNodeWithTagAndName(self, tag, name, root = None):
    if root == None:
      root = self.xml

    nodes = root.getElementsByTagName(tag)
    for node in nodes:
      if node.getAttribute('name') == name:
        return node
    return None
