from lxml import etree
from eagleSchematic import EagleLibrary

class EagleBoard:
  def __init__(self, xmlString):
    tree =  etree.fromstring(xmlString, etree.XMLParser(remove_blank_text=True))

    self.xml = tree

  def toString(self):
    return etree.tostring(self.xml, pretty_print=True)

  def replace(self, partType, replacementSchematic):
    pass

  def getLibraries(self):
    libraries = {}
    for libraryNode in self.xml.findall('.//library'):
      library = EagleLibrary(libraryNode)
      libraries[library.name] = library

    return libraries


