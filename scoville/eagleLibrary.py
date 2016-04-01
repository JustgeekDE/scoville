from lxml import etree

def parseLibraries(rootNode):
  libraries = {}
  for libraryNode in rootNode.findall('.//library'):
    library = EagleLibrary(libraryNode)
    libraries[library.name] = library

  return libraries

class EagleLibrary:
  def __init__(self, libraryNode):
    self.name = libraryNode.get('name')
    self.xml = libraryNode
    pass

  def deepCopy(self):
    node = self._copyNode(self.xml)
    return EagleLibrary(node)

  def _copyNode(self, xml):
    originalXMLString = etree.tostring(xml, pretty_print=True)
    node = etree.fromstring(originalXMLString, etree.XMLParser(remove_blank_text=True))
    return node

  def merge(self, otherLibrary):
    if otherLibrary.name == self.name:
      self._mergePackages(otherLibrary.getPackages())
      self._mergeSymbols(otherLibrary.getSymbols())
      self._mergeDevices(otherLibrary.getDeviceSets())

  def _mergePackages(self, otherPackages):
    ourPackages = self.getPackages()
    packageNode = self.xml.find('.//packages')
    self._mergeSubNodes(ourPackages, otherPackages, packageNode)

  def _mergeSymbols(self, otherSymbols):
    ourSymbols = self.getSymbols()
    symbolNode = self.xml.find('.//symbols')
    self._mergeSubNodes(ourSymbols, otherSymbols, symbolNode)

  def _mergeDevices(self, otherDevices):
    ourDevices = self.getDeviceSets()
    deviceNode = self.xml.find('.//devicesets')
    self._mergeSubNodes(ourDevices, otherDevices, deviceNode)

  def _mergeSubNodes(self, ourNodes, otherNodes, parentNode):
    if len(otherNodes) > 0:
      nodeNames = []
      for node in ourNodes:
        nodeNames.append(node.get('name'))

      for node in otherNodes:
        name = node.get('name')
        if name not in nodeNames:
          newNode = self._copyNode(node)
          parentNode.append(node)

  def getPackages(self):
    return self.xml.findall(".//package")

  def getSymbols(self):
    return self.xml.findall(".//symbol")

  def getDeviceSets(self):
    return self.xml.findall(".//deviceset")

  def toString(self):
    return etree.tostring(self.xml, pretty_print=True)

