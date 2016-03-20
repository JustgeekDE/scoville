import math
from lxml import etree

import eagleSchematic


class SchematicRotation:
  def __init__(self, angle):
    self.angle = angle

  def transform(self, schematic):
    originalXMLString = schematic.toString()
    xml = etree.fromstring(originalXMLString, etree.XMLParser(remove_blank_text=True))
    schematic = xml.find('./drawing/schematic/sheets')
    for element in schematic.findall('.//*[@x]'):
      self._replaceCoordinateAttributesRotated(self.angle, element, ('x', 'y'))

    for element in schematic.findall('.//*[@x1]'):
      self._replaceCoordinateAttributesRotated(self.angle, element, ('x1', 'y1'))
      self._replaceCoordinateAttributesRotated(self.angle, element, ('x2', 'y2'))

    for element in schematic.findall('.//instance'):
      self._rotateElement(element)

    for element in schematic.findall('.//plain/text'):
      self._rotateElement(element)


    return eagleSchematic.EagleSchematic(etree.tostring(xml))

  def _replaceCoordinateAttributesRotated(self, angle, element, (xName, yName)):
    x = float(element.get(xName))
    y = float(element.get(yName))
    (x, y) = self._rotateCoordinates((x, y), angle)
    element.set(xName, str(x))
    element.set(yName, str(y))

  def _rotateCoordinates(self, (orgX, orgY), angle):
    angle = math.radians(angle)
    newX = (orgX * math.cos(angle)) - (orgY * math.sin(angle))
    newY = (orgX * math.sin(angle)) + (orgY * math.cos(angle))
    return (newX, newY)

  def _rotateElement(self, element):
    rotation = 0
    rot = element.get('rot')
    if rot != None:
      rotation = int(rot[1:])
      del element.attrib['rot']

    rotation += self.angle
    while rotation >= 360:
      rotation -= 360
    while rotation < 0:
      rotation += 360

    if rotation != 0:
      element.set('rot', 'R'+str(rotation))
    return element




class SchematicTranslation:
  def __init__(self, translation):
    self.translation = translation

  def transform(self, schematic):
    (dX, dY) = self.translation

    originalXMLString = schematic.toString()
    xml = etree.fromstring(originalXMLString, etree.XMLParser(remove_blank_text=True))
    schematic = xml.find('./drawing/schematic/sheets')
    for element in schematic.findall('.//*[@x]'):
      self._replaceCoordinateAttributeTranslated(element, dX, 'x')
      self._replaceCoordinateAttributeTranslated(element, dY, 'y')

    for element in schematic.findall('.//*[@x1]'):
      self._replaceCoordinateAttributeTranslated(element, dX, 'x1')
      self._replaceCoordinateAttributeTranslated(element, dY, 'y1')
      self._replaceCoordinateAttributeTranslated(element, dX, 'x2')
      self._replaceCoordinateAttributeTranslated(element, dY, 'y2')

    return eagleSchematic.EagleSchematic(etree.tostring(xml))

  def _replaceCoordinateAttributeTranslated(self, element, delta, attributeName):
    oldValue = float(element.get(attributeName))
    newValue = oldValue + delta
    element.set(attributeName, str(newValue))
