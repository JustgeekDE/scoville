import math
from lxml import etree

import eagleBoard
import genericNodeTransformations

class BoardTranslation:
  def __init__(self, translation):
    self.coordinateTransform = genericNodeTransformations.CoordinateTranslation(translation)

  def transform(self, board):

    originalXMLString = board.toString()
    xml = etree.fromstring(originalXMLString, etree.XMLParser(remove_blank_text=True))

    elements = []
    elements.extend(xml.findall('./drawing/board/plain/*'))
    elements.extend(xml.findall('./drawing/board/signals/signal/*'))
    elements.extend(xml.findall('./drawing/board/elements/*'))

    for element in elements:
      self.coordinateTransform.translate(element)

    return eagleBoard.EagleBoard(etree.tostring(xml))
