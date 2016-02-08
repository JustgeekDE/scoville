from unittest import TestCase
from pkg_resources import resource_string
import xml.etree.ElementTree as XML
from BeautifulSoup import BeautifulStoneSoup
from lxml import etree

from scoville import eagleSchematic



class ConversionTest(TestCase):
  def getSchematic(self, schematic):
    inputData = resource_string('test', 'testRessources/replacementExamples/' + schematic + '.sch')
    return eagleSchematic.EagleSchematic(inputData)

  def prettifyXML(self, inputData):
    return etree.tostring(etree.fromstring(inputData, etree.XMLParser(remove_blank_text=True)), pretty_print=True)

  def test_afterExchangeLibraryShouldBeIncluded(self):
    baseSchematic = self.getSchematic('singleDiode')
    replacementSchematic = self.getSchematic('singleLed')

    baseSchematic.replace('1N4004', replacementSchematic)

    self.assertIn('led', baseSchematic.libraries.keys())

  def test_readingAndWritingToFileShouldStayTheSame(self):
    self.maxDiff = None
    inputData = resource_string('test', 'testRessources/replacementExamples/singleDiode.sch')
    baseSchematic = eagleSchematic.EagleSchematic(inputData)

    originalFile = self.prettifyXML(inputData)
    savedFile = baseSchematic.toString()

    self.assertEqual(originalFile,savedFile)

