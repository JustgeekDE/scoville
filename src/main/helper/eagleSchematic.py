from xml.dom.minidom import parse, parseString

class EagleSchematic:
  def __init__(self, xmlString):
    self.xml = parseString(xmlString)


  def getSpiceData(self):
    return ""

  def _getParts(self):
    return self.xml.getElementsByTagName('part')

  def _getDevices(self):
    return self.xml.getElementsByTagName('deviceset')

  def _getDeviceAttributes(self, part):
    devices = self._getDevices()

    for deviceset in devices:
      if deviceset.getAttribute('name') == part.getAttribute('deviceset'):
        for device in deviceset.getElementsByTagName('device'):
          if device.getAttribute('name') == part.getAttribute('device'):
            defaultTechnology = device.getElementsByTagName('technology')[0]
            return defaultTechnology.getElementsByTagName('attribute')

    return []

  def _getSpiceNetlistForPart(self, part):
    netMap = self._getNetMapForPart(part)
    spicePrefix = self._getAttributeValueForPart(part, "SV_SPICE_PREFIX")
    spiceOrder = self._getAttributeValueForPart(part, "SV_SPICE_ORDER").split(';')
    partName = part.getAttribute('name')
    partValue = part.getAttribute('value')

    netList = ''
    for pin in spiceOrder:
      netList += netMap[pin] + ' '

    return spicePrefix + partName + ' ' + netList + partValue

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
    partValue = part.getAttribute('value')

    return '.model ' + partValue + ' ' + spiceModel
