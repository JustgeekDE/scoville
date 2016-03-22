from unittest import TestCase

from lxml import etree
from pkg_resources import resource_string
from scoville import eagleBoard


class BoardReplacementTest(TestCase):
  def getBoard(self, schematic):
    inputData = resource_string('test', 'testRessources/replacementExamples/' + schematic + '.brd')
    return eagleBoard.EagleBoard(inputData)

  def prettifyXML(self, inputData):
    parser = etree.XMLParser(remove_blank_text=True)
    parsedXML = etree.fromstring(inputData, parser)
    prettyXML = etree.tostring(parsedXML, pretty_print=True)
    return prettyXML

  def test_readingAndWritingToFileShouldStayTheSame(self):
    self.maxDiff = None
    inputData = resource_string('test', 'testRessources/replacementExamples/singleDiode.brd')
    board = eagleBoard.EagleBoard(inputData)

    originalFile = self.prettifyXML(inputData)
    savedFile = board.toString()

    self.assertEqual(originalFile, savedFile)

  def test_afterExchangeLibraryShouldBeIncluded(self):
    baseBoard = self.getBoard('singleDiode')
    replacementBoard = self.getBoard('singleLed')

    baseBoard.replaceByPackage('DO41-10', replacementBoard)
    xml = baseBoard.toString()

    self.assertIn('<library name="led">', xml)

  def test_afterExchangingSinglePartItShouldBeIncluded(self):
    baseBoard = self.getBoard('singleDiode')
    replacementBoard = self.getBoard('singleLed')

    baseBoard.replaceByPackage('DO41-10', replacementBoard)
    xml = baseBoard.toString()

    self.assertIn('<element name="D1-LED1"', xml)


  def test_afterExchangingMultiplePartsTheyShouldBeIncluded(self):
    baseBoard = self.getBoard('twoDiodes')
    replacementBoard = self.getBoard('singleLed')

    baseBoard.replaceByPackage('DO41-10', replacementBoard)
    xml = baseBoard.toString()

    self.assertIn('<element name="D1-LED1"', xml)
    self.assertIn('<element name="D2-LED1"', xml)

  def test_afterExchangingComplexPartTheNewNetShouldBeIncluded(self):
    baseBoard = self.getBoard('basicComplexSchematic')
    replacementBoard = self.getBoard('basicTwoPartSchematic')

    baseBoard.replaceByPackage('SIMPLE_LED', replacementBoard)
    xml = baseBoard.toString()

    self.assertNotIn('<element name="P1"', xml)

    self.assertIn('<contactref element="P1-LED1"', xml)
    self.assertIn('<signal name="P1-INT-1"', xml)


  def test_afterExchangingComplexPartTheNewPartsShouldBeTranslated(self):
    baseBoard = self.getBoard('basicComplexSchematicWith2Parts')
    replacementBoard = self.getBoard('basicTwoPartSchematic')

    baseBoard.replaceByPackage('SIMPLE_LED', replacementBoard)
    xml = baseBoard.toString()

    self.assertIn('<element name="P1-LED1" library="p.peter-leds" package="LED-5MM" value="" x="13.97" y="5.08"/>', xml)
    self.assertIn('<element name="P2-LED1" library="p.peter-leds" package="LED-5MM" value="" x="26.67" y="17.78" rot="R270"/>', xml)
    self.assertIn('<text x="24.13" y="27.94" size="1.016" layer="21" ratio="15" rot="R270">LED</text>', xml)

