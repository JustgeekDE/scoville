from unittest import TestCase
from pkg_resources import resource_string
import xml.etree.ElementTree as XML
from BeautifulSoup import BeautifulStoneSoup

from scoville import eagleSchematic



class ConversionTest(TestCase):
  def getSchematic(self, schematic):
    inputData = resource_string('test', 'testRessources/replacementExamples/' + schematic + '.sch')
    return eagleSchematic.EagleSchematic(inputData)

  def test_afterExchangeLibraryShouldBeIncluded(self):
    baseSchematic = self.getSchematic('singleDiode')
    replacementSchematic = self.getSchematic('singleLed')

    baseSchematic.replace('1N4004', replacementSchematic)

    self.assertIn('led', baseSchematic.libraries.keys())

  def test_readingAndWritingToFileShouldStayTheSame(self):
    self.maxDiff = None
    inputData = resource_string('test', 'testRessources/replacementExamples/singleDiode.sch')
    baseSchematic = eagleSchematic.EagleSchematic(inputData)

    originalXML = XML.fromstring(inputData)


    originalFile = BeautifulStoneSoup(XML.tostring(originalXML)).prettify().strip()
    savedFile = BeautifulStoneSoup(baseSchematic.toString()).prettify().strip()

    self.assertEqual(originalFile,savedFile)
