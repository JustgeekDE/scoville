from unittest import TestCase

from lxml import etree
from pkg_resources import resource_string

from scoville import schematicTransformations
from scoville import eagleSchematic


class ConversionTest(TestCase):
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


  def test_movingSchematicShouldWork(self):
    transformation = schematicTransformations.SchematicTranslation((2, 5))
    baseSchematic = self.getSchematic('simpleSchematicWithParts')

    newSchematic = transformation.transform(baseSchematic)

    originalXml = baseSchematic.toString()
    xml = newSchematic.toString()

    self.assertIn('text x="27.94"', originalXml)
    self.assertIn('text x="29.94"', xml)

    self.assertIn('<instance part="LED1" gate="G$1" x="35.56" y="50.8"/>', originalXml)
    self.assertIn('<instance part="LED1" gate="G$1" x="37.56" y="55.8"/>', xml)

    self.assertIn('<wire x1="25.4" y1="58.42" x2="25.4" y2="43.18"', originalXml)
    self.assertIn('<wire x1="27.4" y1="63.42" x2="27.4" y2="48.18"', xml)

    self.assertIn('<wire x1="33.02" y1="50.8" x2="27.94" y2="50.8"', originalXml)
    self.assertIn('<wire x1="35.02" y1="55.8" x2="29.94" y2="55.8"', xml)

  def test_rotationByQuarter(self):
    transformation = schematicTransformations.SchematicRotation(90)

    (x, y) = transformation._rotateCoordinates((1, 0), 90)
    self.assertAlmostEqual(x, 0.0)
    self.assertAlmostEqual(y, 1.0)

    (x, y) = transformation._rotateCoordinates((1, 0), 180)
    self.assertAlmostEqual(x, -1.0)
    self.assertAlmostEqual(y, 0.0)

    (x, y) = transformation._rotateCoordinates((1, 0), 270)
    self.assertAlmostEqual(x, 0.0)
    self.assertAlmostEqual(y, -1.0)

    (x, y) = transformation._rotateCoordinates((1, 0), 360)
    self.assertAlmostEqual(x, 1.0)
    self.assertAlmostEqual(y, 0.0)

  def test_rotatingSchematicShouldWork(self):
    transformation = schematicTransformations.SchematicRotation(90)
    baseSchematic = self.getSchematic('simpleSchematicWithParts')

    newSchematic = transformation.transform(baseSchematic)

    originalXml = baseSchematic.toString()
    xml = newSchematic.toString()

    self.assertIn('<text x="27.94" y="45.72"', originalXml)
    self.assertIn('<text x="-45.72" y="27.94"', xml)

    self.assertIn('<instance part="LED1" gate="G$1" x="35.56" y="50.8"/>', originalXml)
    self.assertIn('<instance part="LED1" gate="G$1" x="-50.8" y="35.56"/>', xml)

    self.assertIn('<wire x1="25.4" y1="58.42" x2="25.4" y2="43.18"', originalXml)
    self.assertIn('<wire x1="-58.42" y1="25.4" x2="-43.18" y2="25.4"', xml)

    self.assertIn('<wire x1="33.02" y1="50.8" x2="27.94" y2="50.8"', originalXml)
    self.assertIn('<wire x1="-50.8" y1="33.02" x2="-50.8" y2="27.94"', xml)
