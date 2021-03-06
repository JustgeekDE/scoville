from unittest import TestCase

from lxml import etree
from pkg_resources import resource_string
from scoville import eagleSchematic


class SchematicReplacementTest(TestCase):
  def getSchematic(self, schematic):
    inputData = resource_string('test', 'testRessources/replacementExamples/' + schematic + '.sch')
    return eagleSchematic.EagleSchematic(inputData)

  def prettifyXML(self, inputData):
    parser = etree.XMLParser(remove_blank_text=True)
    parsedXML = etree.fromstring(inputData, parser)
    prettyXML = etree.tostring(parsedXML, pretty_print=True)
    return prettyXML

  def test_readingAndWritingToFileShouldStayTheSame(self):
    self.maxDiff = None
    inputData = resource_string('test', 'testRessources/replacementExamples/singleDiode.sch')
    baseSchematic = eagleSchematic.EagleSchematic(inputData)

    originalFile = self.prettifyXML(inputData)
    savedFile = baseSchematic.toString()

    self.assertEqual(originalFile, savedFile)

  def test_afterExchangeLibraryShouldBeIncluded(self):
    baseSchematic = self.getSchematic('singleDiode')
    replacementSchematic = self.getSchematic('singleLed')

    baseSchematic.replace('1N4004', replacementSchematic)

    self.assertIn('led', baseSchematic.libraries.keys())

  def test_afterExchangeLibraryShouldBeInXML(self):
    baseSchematic = self.getSchematic('singleDiode')
    replacementSchematic = self.getSchematic('singleLed')

    baseSchematic.replace('1N4004', replacementSchematic)
    xml = baseSchematic.toString()

    self.assertIn('<library name="led">', xml)

  def test_afterExchangingSinglePartItShouldBeIncluded(self):
    baseSchematic = self.getSchematic('singleDiode')
    replacementSchematic = self.getSchematic('singleLed')

    baseSchematic.replace('1N4004', replacementSchematic)
    xml = baseSchematic.toString()

    self.assertIn('D1-LED1', baseSchematic.parts.keys())
    self.assertIn('name="D1-LED1"', xml)
    self.assertIn('part="D1-LED1"', xml)


  def test_afterExchangingMultiplePartsTheyShouldBeIncluded(self):
    baseSchematic = self.getSchematic('twoDiodes')
    replacementSchematic = self.getSchematic('singleLed')

    baseSchematic.replace('1N4004', replacementSchematic)
    xml = baseSchematic.toString()

    self.assertIn('D1-LED1', baseSchematic.parts.keys())
    self.assertIn('name="D1-LED1"', xml)
    self.assertIn('part="D1-LED1"', xml)
    self.assertIn('D2-LED1', baseSchematic.parts.keys())
    self.assertIn('name="D2-LED1"', xml)
    self.assertIn('part="D2-LED1"', xml)

  def test_afterExchangingComplexPartTheNewNetShouldBeIncluded(self):
    baseSchematic = self.getSchematic('basicComplexSchematic')
    replacementSchematic = self.getSchematic('basicTwoPartSchematic')

    baseSchematic.replace('SIMPLE_LED', replacementSchematic)
    xml = baseSchematic.toString()

    self.assertNotIn('<part name="P1"', xml)
    self.assertNotIn('<instance part="P1"', xml)

    self.assertIn('<pinref part="P1-LED1"', xml)
    self.assertIn('<net name="P1-INT-1"', xml)


  def test_afterExchangingComplexPartTheNewPartsShouldBeTranslated(self):
    baseSchematic = self.getSchematic('basicComplexSchematicWith2Parts')
    replacementSchematic = self.getSchematic('basicTwoPartSchematic')

    baseSchematic.replace('SIMPLE_LED', replacementSchematic)
    xml = baseSchematic.toString()

    self.assertIn('<instance part="P1-LED1" gate="G$1" x="17.78" y="5.08"/>', xml)
    self.assertIn('<instance part="P2-LED1" gate="G$1" x="30.48" y="15.24" rot="R270"/>', xml)
    self.assertIn('<text x="35.56" y="22.86" size="1.778" layer="97" rot="R270">LED</text>', xml)

  def test_afterExchangingLibrariesShouldBeMerged(self):
    baseSchematic = self.getSchematic('singleGateFromLibrary')
    replacementSchematic = self.getSchematic('differentGateFromLibrary')

    baseSchematic.replace('AND', replacementSchematic)
    xml = baseSchematic.toString()

    self.assertIn('<package name="NAND"', xml)
    self.assertIn('<package name="OR"', xml)

