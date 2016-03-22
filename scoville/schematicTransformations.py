import math
from lxml import etree

import eagleSchematic
import genericNodeTransformations


class SchematicRotation:
  def __init__(self, angle):
    self.coordinateTransform = genericNodeTransformations.CoordinateRotation(angle)
    self.nodeTransform = genericNodeTransformations.NodeRotation(angle)

  def transform(self, schematic):
    originalXMLString = schematic.toString()
    xml = etree.fromstring(originalXMLString, etree.XMLParser(remove_blank_text=True))
    schematic = xml.find('./drawing/schematic/sheets')

    for element in schematic.findall('.//*[@x]'):
      self.coordinateTransform.rotateNode(element)

    for element in schematic.findall('.//*[@x1]'):
      self.coordinateTransform.rotateNode(element)

    for element in schematic.findall('.//instance'):
      self.nodeTransform.rotateNode(element)

    for element in schematic.findall('.//plain/text'):
      self.nodeTransform.rotateNode(element)


    return eagleSchematic.EagleSchematic(etree.tostring(xml))


class SchematicTranslation:
  def __init__(self, translation):
    self.coordinateTransform = genericNodeTransformations.CoordinateTranslation(translation)

  def transform(self, schematic):

    originalXMLString = schematic.toString()
    xml = etree.fromstring(originalXMLString, etree.XMLParser(remove_blank_text=True))
    schematic = xml.find('./drawing/schematic/sheets')
    for element in schematic.findall('.//*[@x]'):
      self.coordinateTransform.translate(element)

    for element in schematic.findall('.//*[@x1]'):
      self.coordinateTransform.translate(element)

    return eagleSchematic.EagleSchematic(etree.tostring(xml))
