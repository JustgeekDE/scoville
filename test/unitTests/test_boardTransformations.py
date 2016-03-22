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

  def test_rotatingSchematicShouldWork(self):
    transformation = boardTransformations.BoardRotation(90)
    baseBoard = self.getBoard('simpleSchematicWithParts')

    newBoard = transformation.transform(baseBoard)

    originalXml = baseBoard.toString()
    xml = newBoard.toString()

    self.assertIn('<wire x1="1.27" y1="2.54" x2="7.62" y2="2.54" width="0.4064" layer="21"/>', originalXml)
    self.assertIn('<wire x1="-2.54" y1="1.27" x2="-2.54" y2="7.62" width="0.4064" layer="21"/>', xml)

    self.assertIn('<text x="0.254" y="8.763" size="1.016" layer="21" ratio="15">Example!</text>', originalXml)
    self.assertIn('<text x="-8.763" y="0.254" size="1.016" layer="21" ratio="15" rot="R90">Example!</text>', xml)

    self.assertIn('<hole x="13.97" y="1.27" drill="0.6"/>', originalXml)
    self.assertIn('<hole x="-1.27" y="13.97" drill="0.6"/>', xml)

    self.assertIn('package="LED-5MM" value="" x="10.16" y="5.08" rot="R180"/>',originalXml)
    self.assertIn('package="LED-5MM" value="" x="-5.08" y="10.16" rot="R270"/>',xml)

    self.assertIn('<wire x1="13.97" y1="8.89" x2="12.7" y2="8.89" width="0.4064" layer="1"/>', originalXml)
    self.assertIn('<wire x1="-5.08" y1="13.97" x2="-8.89" y2="13.97" width="0.4064" layer="1"/>', xml)

    self.assertIn('<via x="12.7" y="8.89" extent="1-16" drill="0.6" shape="square"/>', originalXml)
    self.assertIn('<via x="-8.89" y="12.7" extent="1-16" drill="0.6" shape="square"/>', xml)

    self.assertIn('<pad name="K" x="1.27" y="0" drill="0.8128" shape="octagon"/>', originalXml)
    self.assertIn('<pad name="K" x="1.27" y="0" drill="0.8128" shape="octagon"/>', xml)
    self.assertIn('<text x="3.175" y="0.5334" size="1.27" layer="25" ratio="10">&gt;NAME</text>', originalXml)
    self.assertIn('<text x="3.175" y="0.5334" size="1.27" layer="25" ratio="10">&gt;NAME</text>', xml)

