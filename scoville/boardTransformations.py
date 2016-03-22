import math
from lxml import etree

import eagleBoard
import genericNodeTransformations

class BoardTransformation:

  def getTransformableElements(self,xml):
    elements = []
    elements.extend(xml.findall('./drawing/board/plain/*'))
    elements.extend(xml.findall('./drawing/board/signals/signal/*'))
    elements.extend(xml.findall('./drawing/board/elements/*'))

    return elements


class BoardTranslation(BoardTransformation):
  def __init__(self, translation):
    self.coordinateTransform = genericNodeTransformations.CoordinateTranslation(translation)

  def transform(self, board):
    originalXMLString = board.toString()
    xml = etree.fromstring(originalXMLString, etree.XMLParser(remove_blank_text=True))

    elements = self.getTransformableElements(xml)
    for element in elements:
      self.coordinateTransform.translate(element)

    return eagleBoard.EagleBoard(etree.tostring(xml))
