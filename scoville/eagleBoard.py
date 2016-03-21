from lxml import etree
from eagleSchematic import EagleLibrary

class EagleBoard:
  def __init__(self, xmlString):
    tree =  etree.fromstring(xmlString, etree.XMLParser(remove_blank_text=True))

    self.xml = tree

  def toString(self):
    return etree.tostring(self.xml, pretty_print=True)

  def replace(self, partType, replacementSchematic):
    self.addLibraries(replacementSchematic.getLibraries())
    pass

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



