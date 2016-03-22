from lxml import etree
from eagleSchematic import EagleLibrary

class EagleBoard:
  def __init__(self, xmlString):
    tree =  etree.fromstring(xmlString, etree.XMLParser(remove_blank_text=True))

    self.xml = tree

  def toString(self):
    return etree.tostring(self.xml, pretty_print=True)

  def replaceByPackage(self, packageName, replacementSchematic):
    self.addLibraries(replacementSchematic.getLibraries())

    oldParts = self.getPartsWithPackage(packageName)
    if oldParts != None:
      for part in oldParts:
        newSchematic = replacementSchematic.deepCopy()
        partName = part.get('name')
        newSchematic.prefixParts(partName + '-')
        self._replaceSinglePart(part, newSchematic)

    pass

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


