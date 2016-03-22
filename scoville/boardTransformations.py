import math
from lxml import etree

import eagleBoard
import genericNodeTransformations

class BoardTransformation:

  def getCoordinateElements(self, xml):
    elements = []
    elements.extend(xml.findall('./drawing/board/plain/*'))
    elements.extend(xml.findall('./drawing/board/signals/signal/*'))
    elements.extend(xml.findall('./drawing/board/elements/*'))

    return elements

  def getRotationElements(self, xml):
    elements = []
    elements.extend(xml.findall('./drawing/board/plain/text'))
    elements.extend(xml.findall('./drawing/board/elements/*'))

    return elements


class BoardTranslation(BoardTransformation):
  def __init__(self, translation):
    self.coordinateTransform = genericNodeTransformations.CoordinateTranslation(translation)

  def transform(self, board):
    originalXMLString = board.toString()
    xml = etree.fromstring(originalXMLString, etree.XMLParser(remove_blank_text=True))

    elements = self.getCoordinateElements(xml)
    for element in elements:
      self.coordinateTransform.translate(element)

    return eagleBoard.EagleBoard(etree.tostring(xml))

class BoardRotation(BoardTransformation):
  def __init__(self, angle):
    self.coordinateTransform = genericNodeTransformations.CoordinateRotation(angle)
    self.nodeTransform = genericNodeTransformations.NodeRotation(angle)

  def transform(self, board):
    originalXMLString = board.toString()
    xml = etree.fromstring(originalXMLString, etree.XMLParser(remove_blank_text=True))

    elements = self.getCoordinateElements(xml)
    for element in elements:
      self.coordinateTransform.rotateNode(element)

    elements = self.getRotationElements(xml)
    for element in elements:
      self.nodeTransform.rotateNode(element)

    return eagleBoard.EagleBoard(etree.tostring(xml))
