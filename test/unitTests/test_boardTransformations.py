from unittest import TestCase

from lxml import etree
from pkg_resources import resource_string

from scoville import boardTransformations
from scoville import eagleBoard


class BoardTransformationTest(TestCase):
  def getBoard(self, schematic):
    inputData = resource_string('test', 'testRessources/replacementExamples/' + schematic + '.brd')
    return eagleBoard.EagleBoard(inputData)

  def test_movingSchematicShouldWork(self):
    transformation = boardTransformations.BoardTranslation((2, 5))
    baseBoard = self.getBoard('simpleSchematicWithParts')

    newBoard = transformation.transform(baseBoard)

    originalXml = baseBoard.toString()
    xml = newBoard.toString()

    self.assertIn('<wire x1="1.27" y1="2.54" x2="7.62" y2="2.54" width="0.4064" layer="21"/>', originalXml)
    self.assertIn('<wire x1="3.27" y1="7.54" x2="9.62" y2="7.54" width="0.4064" layer="21"/>', xml)

    self.assertIn('<text x="0.254" y="8.763" size="1.016" layer="21" ratio="15">Example!</text>', originalXml)
    self.assertIn('<text x="2.254" y="13.763" size="1.016" layer="21" ratio="15">Example!</text>', xml)

    self.assertIn('<hole x="13.97" y="1.27" drill="0.6"/>', originalXml)
    self.assertIn('<hole x="15.97" y="6.27" drill="0.6"/>', xml)

    self.assertIn('package="LED-5MM" value="" x="10.16" y="5.08" rot="R180"/>',originalXml)
    self.assertIn('package="LED-5MM" value="" x="12.16" y="10.08" rot="R180"/>',xml)

    self.assertIn('<wire x1="13.97" y1="8.89" x2="12.7" y2="8.89" width="0.4064" layer="1"/>', originalXml)
    self.assertIn('<wire x1="15.97" y1="13.89" x2="14.7" y2="13.89" width="0.4064" layer="1"/>', xml)

    self.assertIn('<via x="12.7" y="8.89" extent="1-16" drill="0.6" shape="square"/>', originalXml)
    self.assertIn('<via x="14.7" y="13.89" extent="1-16" drill="0.6" shape="square"/>', xml)

    self.assertIn('<pad name="K" x="1.27" y="0" drill="0.8128" shape="octagon"/>', originalXml)
    self.assertIn('<pad name="K" x="1.27" y="0" drill="0.8128" shape="octagon"/>', xml)
    self.assertIn('<text x="3.175" y="0.5334" size="1.27" layer="25" ratio="10">&gt;NAME</text>', originalXml)
    self.assertIn('<text x="3.175" y="0.5334" size="1.27" layer="25" ratio="10">&gt;NAME</text>', xml)

    # def test_rotationByQuarter(self):
    #   transformation = boardTransformations.SchematicRotation(90)
    #
    #   (x, y) = transformation._rotateCoordinates((1, 0), 90)
    #   self.assertAlmostEqual(x, 0.0)
    #   self.assertAlmostEqual(y, 1.0)
    #
    #   (x, y) = transformation._rotateCoordinates((1, 0), 180)
    #   self.assertAlmostEqual(x, -1.0)
    #   self.assertAlmostEqual(y, 0.0)
    #
    #   (x, y) = transformation._rotateCoordinates((1, 0), 270)
    #   self.assertAlmostEqual(x, 0.0)
    #   self.assertAlmostEqual(y, -1.0)
    #
    #   (x, y) = transformation._rotateCoordinates((1, 0), 360)
    #   self.assertAlmostEqual(x, 1.0)
    #   self.assertAlmostEqual(y, 0.0)
    #
    # def test_rotatingSchematicShouldWork(self):
    #   transformation = boardTransformations.SchematicRotation(90)
    #   baseBoard = self.getSchematic('simpleSchematicWithParts')
    #
    #   newBoard = transformation.transform(baseBoard)
    #
    #   originalXml = baseBoard.toString()
    #   xml = newBoard.toString()
    #
    #   self.assertIn('<text x="27.94" y="45.72"', originalXml)
    #   self.assertIn('<text x="-45.72" y="27.94"', xml)
    #
    #   self.assertIn('<instance part="LED1" gate="G$1" x="35.56" y="50.8"/>', originalXml)
    #   self.assertIn('<instance part="LED1" gate="G$1" x="-50.8" y="35.56" rot="R90"/>', xml)
    #
    #   self.assertIn('<wire x1="25.4" y1="58.42" x2="25.4" y2="43.18"', originalXml)
    #   self.assertIn('<wire x1="-58.42" y1="25.4" x2="-43.18" y2="25.4"', xml)
    #
    #   self.assertIn('<wire x1="33.02" y1="50.8" x2="27.94" y2="50.8"', originalXml)
    #   self.assertIn('<wire x1="-50.8" y1="33.02" x2="-50.8" y2="27.94"', xml)
    #
