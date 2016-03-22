import math
from lxml import etree

import eagleBoard


class NodeRotation:
  def __init__(self, angle):
    self.angle = angle

  def rotateNode(self, node):
    rotation = self._getNodeRotation(node)
    rotation += self.angle
    self._setNodeRotation(node, rotation)

    return node

  def _setNodeRotation(self, node, rotation):
    while rotation >= 360:
      rotation -= 360
    while rotation < 0:
      rotation += 360
    if rotation != 0:
      node.set('rot', 'R' + str(rotation))

  def _getNodeRotation(self, node):
    rotation = 0
    rot = node.get('rot')
    if rot != None:
      rotation = int(rot[1:])
      del node.attrib['rot']
    return rotation


class CoordinateRotation:
  def __init__(self, angle):
    self.angle = angle

  def _replaceCoordinateSet(self, angle, node, (xName, yName)):
    x = node.get(xName)
    y = node.get(yName)
    if x != None and y != None:
      x = float(x)
      y = float(y)
      (x, y) = self._rotateCoordinates((x, y), angle)
      node.set(xName, str(x))
      node.set(yName, str(y))

  def _rotateCoordinates(self, (orgX, orgY), angle):
    angle = math.radians(angle)
    newX = (orgX * math.cos(angle)) - (orgY * math.sin(angle))
    newY = (orgX * math.sin(angle)) + (orgY * math.cos(angle))
    return newX, newY

  def rotateNode(self, node):
    self._replaceCoordinateSet(self.angle, node, ('x','y'))
    self._replaceCoordinateSet(self.angle, node, ('x1','y1'))
    self._replaceCoordinateSet(self.angle, node, ('x2','y2'))
    return node


class CoordinateTranslation:
  def __init__(self, translation):
    self.translation = translation

  def translate(self, node):
    self._replaceCoordinatePair(node, ('x', 'y'), self.translation)
    self._replaceCoordinatePair(node, ('x1', 'y1'), self.translation)
    self._replaceCoordinatePair(node, ('x2', 'y2'), self.translation)

    return node

  def _replaceCoordinatePair(self, node, (xName, yName), (dX, dY)):
    self._replaceCoordinateAttributeTranslated(node, dX, xName)
    self._replaceCoordinateAttributeTranslated(node, dY, yName)

  def _replaceCoordinateAttributeTranslated(self, node, delta, attributeName):
    value = node.get(attributeName)
    if value != None:
      oldValue = float(value)
      newValue = oldValue + delta
      node.set(attributeName, str(newValue))
