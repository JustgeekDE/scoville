from unittest import TestCase
from pkg_resources import resource_string

from scoville import eagleSchematic


class ConversionTest(TestCase):
  def singleTransistorSchematic(self):
    return resource_string('test', "testRessources/singleTransistor.sch")

  def test_extractSinglePartCorrectly(self):
    inputData = self.singleTransistorSchematic()
    circuit = eagleSchematic.EagleSchematic(inputData)

    parts = circuit.parts

    self.assertEqual(len(parts), 1)
    self.assertEqual(parts['Q1'].name, 'Q1')

  def test_extractSingleDeviceCorrectly(self):
    inputData = self.singleTransistorSchematic()
    circuit = eagleSchematic.EagleSchematic(inputData)

    devices = circuit.parts

    self.assertEqual(len(devices), 1)
    self.assertEqual(devices['Q1'].devicesetName, 'TRANSISTOR-NPN-GENERIC')

  def test_getDeviceForPart(self):
    inputData = self.singleTransistorSchematic()
    circuit = eagleSchematic.EagleSchematic(inputData)

    transistor = circuit.parts['Q1']
    attributes = transistor.attributes

    self.assertEqual(len(attributes), 3)

  def test_getNetMapForPart(self):
    inputData = self.singleTransistorSchematic()
    circuit = eagleSchematic.EagleSchematic(inputData)

    transistor = circuit.parts['Q1']
    netMap = transistor.netMap

    self.assertEqual(len(netMap.keys()), 3)
    self.assertEqual(netMap['COLLECTOR'], 'COLLECTOR')
    self.assertEqual(netMap['BASE'], 'BASE')
    self.assertEqual(netMap['EMITTER'], 'EMITTER')

  def test_getSpiceNetlistForPart(self):
    inputData = self.singleTransistorSchematic()
    circuit = eagleSchematic.EagleSchematic(inputData)

    transistor = circuit.parts['Q1']
    spiceData = transistor.getSpiceNetlist()

    self.assertEqual(spiceData, "QQ1 COLLECTOR BASE EMITTER BC547")

  def test_getSpiceModelForPart(self):
    inputData = self.singleTransistorSchematic()
    circuit = eagleSchematic.EagleSchematic(inputData)

    transistor = circuit.parts['Q1']
    spiceData = transistor.getSpiceModel()

    self.assertEqual(spiceData, ".model BC547 NPN ()")

  def test_getSpiceModelForSupplyPart(self):
    inputData = resource_string('test', "testRessources/transistorAndResistorWithSupply.sch")
    circuit = eagleSchematic.EagleSchematic(inputData)

    positiveSupply = circuit.parts['P+1']
    spiceModel = positiveSupply.getSpiceModel()
    spiceNet = positiveSupply.getSpiceNetlist()
    spiceSupply = positiveSupply.getSpiceSupply()

    self.assertEqual(spiceModel, None)
    self.assertEqual(spiceNet, None)
    self.assertEqual(spiceSupply, "VP5V +5V GND dc +5V ac 0V")

  def test_shouldNotCreateSupplyForGNDNode(self):
    inputData = resource_string('test', "testRessources/transistorAndResistorWithSupply.sch")
    circuit = eagleSchematic.EagleSchematic(inputData)

    negativeSupply = circuit.parts['GND1']
    spiceModel = negativeSupply.getSpiceModel()
    spiceNet = negativeSupply.getSpiceNetlist()
    spiceSupply = negativeSupply.getSpiceSupply()

    self.assertEqual(spiceModel, None)
    self.assertEqual(spiceNet, None)
    self.assertEqual(spiceSupply, None)

  def test_shouldNotCreateModelForUnknowNode(self):
    inputData = resource_string('test', "testRessources/transistorAndResistorWithSupplyAndTestPoint.sch")
    circuit = eagleSchematic.EagleSchematic(inputData)

    testPoint = circuit.parts['TP1']
    spiceModel = testPoint.getSpiceModel()
    spiceNet = testPoint.getSpiceNetlist()
    spiceSupply = testPoint.getSpiceSupply()

    self.assertEqual(spiceModel, None)
    self.assertEqual(spiceNet, None)
    self.assertEqual(spiceSupply, None)
