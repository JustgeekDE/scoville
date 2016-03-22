from lxml import etree
from eagleSchematic import EagleLibrary

class EagleBoard:
  def __init__(self, xmlString):
    tree =  etree.fromstring(xmlString, etree.XMLParser(remove_blank_text=True))

    self.xml = tree

  def toString(self):
    return etree.tostring(self.xml, pretty_print=True)

  def replaceByPackage(self, packageName, replacementBoard):
    self.addLibraries(replacementBoard.getLibraries())

    oldParts = self.getPartsWithPackage(packageName)
    if oldParts != None:
      for part in oldParts:
        copiedBoard = replacementBoard.deepCopy()
        partName = part.get('name')

        copiedBoard.prefixParts(partName + '-')

        self._replaceSinglePart(part, copiedBoard)
        self._replaceSignals(partName, copiedBoard)

  def _replaceSinglePart(self, part, replacementSchematic):
    parent = part.getparent()
    parent.remove(part)
    for newPart in replacementSchematic.getParts():
      parent.append(newPart)

  def getLibraries(self):
    libraries = {}
    for libraryNode in self.xml.findall('.//library'):
      library = EagleLibrary(libraryNode)
      libraries[library.name] = library

    return libraries

  def addLibraries(self, newLibraries):
    currentLibraries = self.getLibraries()

    currentLibraries.update(newLibraries)
    libraryNode = self.xml.find('./drawing/board/libraries')
    libraryNode.clear()
    for library in currentLibraries.values():
      library = library.deepCopy()
      libraryNode.append(library.xml)


  def getPartsWithPackage(self, package):
    return self.xml.findall(".//element[@package='{package}']".format(package=package))

  def getParts(self):
    return self.xml.findall(".//element")

  def prefixParts(self, prefix):
    parts = self.getParts()
    for part in parts:
      partName = part.get('name')
      newPartName = prefix+partName

      part.set('name', newPartName)
      connections = self.xml.findall(".//*[@element='{partName}']".format(partName=partName))
      for connection in connections:
        connection.set('element', newPartName)

  def deepCopy(self):
    originalXMLString = self.toString()
    return EagleBoard(originalXMLString)

  def _replaceSignals(self, partName, replacementBoard):
    replacedSignals = []
    contactRefs =  self.xml.findall(".//contactref[@element='{partName}']".format(partName=partName))
    for refNode in contactRefs:
      pad = refNode.get('pad')
      replacementNet = replacementBoard.getSignal(pad)
      if replacementNet != None:
        for connection in replacementNet.getchildren():
          refNode.getparent().append(connection)

        refNode.getparent().remove(refNode)
        replacedSignals.append(pad)

    newSignals = replacementBoard.getSignals()
    for signal in newSignals:
      oldName = signal.get('name')
      if oldName not in replacedSignals:
        newName = partName + '-' + oldName
        signal.set('name', newName)
        self.addSignal(signal)

  def addSignal(self, signalNode):
    parent = self.xml.find(".//signals")
    parent.append(signalNode)

  def getSignals(self):
    return self.xml.findall(".//signal")

  def getSignal(self, signalName):
    return self.xml.find(".//signal[@name='{signalName}']".format(signalName=signalName))



