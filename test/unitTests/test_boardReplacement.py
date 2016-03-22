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
  #
  #
  # def test_afterExchangingMultiplePartsTheyShouldBeIncluded(self):
  #   baseBoard = self.getSchematic('twoDiodes')
  #   replacementBoard = self.getSchematic('singleLed')
  #
  #   baseBoard.replace('1N4004', replacementBoard)
  #   xml = baseBoard.toString()
  #
  #   self.assertIn('D1-LED1', baseBoard.parts.keys())
  #   self.assertIn('name="D1-LED1"', xml)
  #   self.assertIn('part="D1-LED1"', xml)
  #   self.assertIn('D2-LED1', baseBoard.parts.keys())
  #   self.assertIn('name="D2-LED1"', xml)
  #   self.assertIn('part="D2-LED1"', xml)
  #
  # def test_afterExchangingComplexPartTheNewNetShouldBeIncluded(self):
  #   baseBoard = self.getSchematic('basicComplexSchematic')
  #   replacementBoard = self.getSchematic('basicTwoPartSchematic')
  #
  #   baseBoard.replace('SIMPLE_LED', replacementBoard)
  #   xml = baseBoard.toString()
  #
  #   self.assertNotIn('<part name="P1"', xml)
  #   self.assertNotIn('<instance part="P1"', xml)
  #
  #   self.assertIn('<pinref part="P1-LED1"', xml)
  #   self.assertIn('<net name="P1-INT-1"', xml)
  #
  #
  # def test_afterExchangingComplexPartTheNewPartsShouldBeTranslated(self):
  #   baseBoard = self.getSchematic('basicComplexSchematicWith2Parts')
  #   replacementBoard = self.getSchematic('basicTwoPartSchematic')
  #
  #   baseBoard.replace('SIMPLE_LED', replacementBoard)
  #   xml = baseBoard.toString()
  #
  #   self.assertIn('<instance part="P1-LED1" gate="G$1" x="17.78" y="5.08"/>', xml)
  #   self.assertIn('<instance part="P2-LED1" gate="G$1" x="30.48" y="15.24" rot="R270"/>', xml)
  #   self.assertIn('<text x="35.56" y="22.86" size="1.778" layer="97" rot="R270">LED</text>', xml)
  #
