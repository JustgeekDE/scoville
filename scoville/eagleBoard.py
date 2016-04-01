from lxml import etree

import boardTransformations
import eagleLibrary

class EagleBoardElement:
  def __init__(self, node):
    self.node = node

  def getRotation(self):
    rotation = self.node.get('rot')
    if rotation != None:
      return int(rotation[1:])
    return 0

  def getPosition(self):
    position = (0,0)
    x = float(self.node.get('x'))
    y = float(self.node.get('y'))
    return x,y

  def getName(self):
    return self.node.get('name')


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
        eaglePart = EagleBoardElement(part)

        copiedBoard = replacementBoard.deepCopy()
        partName = eaglePart.getName()

        rotation = boardTransformations.BoardRotation(eaglePart.getRotation())
        translation = boardTransformations.BoardTranslation(eaglePart.getPosition())

        copiedBoard = rotation.transform(copiedBoard)
        copiedBoard = translation.transform(copiedBoard)

        copiedBoard.prefixParts(partName + '-')

        self._replaceDocu(copiedBoard)
        self._replaceSinglePart(part, copiedBoard)
        self._replaceSignals(partName, copiedBoard)

  def _replaceSinglePart(self, part, replacementSchematic):
    parent = part.getparent()
    parent.remove(part)
    for newPart in replacementSchematic.getParts():
      parent.append(newPart)

  def addLibraries(self, newLibraries):
    currentLibraries = self.getLibraries()

    self.libraries = eagleLibrary.mergeLibraryLists(currentLibraries, newLibraries)

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

  def _replaceDocu(self, replacementBoard):
    self.addDocu(replacementBoard.getDocu())

  def getLibraries(self):
    return eagleLibrary.parseLibraries(self.xml)

  def getDocu(self):
    return self.xml.findall(".//plain/")

  def addDocu(self, newDocu):
    docuNode = self.xml.find(".//plain")
    for newNode in newDocu:
      docuNode.append(newNode)


