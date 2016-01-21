from unittest import TestCase
from pkg_resources import resource_string

from scoville.eagleSchematic import EagleSchematic


class ConversionTest(TestCase):

  def singleTransistorSchematic(self):
    return resource_string('test', "testRessources/singleTransistor.sch")

  def test_extractSinglePartCorrectly(self):
    inputData = self.singleTransistorSchematic()
    circuit = EagleSchematic(inputData)

    parts = circuit._getParts()

    self.assertEqual(len(parts), 1)
    self.assertEqual(parts[0].getAttribute('name'), 'Q1')

  def test_extractSingleDeviceCorrectly(self):
    inputData = self.singleTransistorSchematic()
    circuit = EagleSchematic(inputData)

    devices = circuit._getDevices()

    self.assertEqual(len(devices), 1)
    self.assertEqual(devices[0].getAttribute('name'), 'TRANSISTOR-NPN-GENERIC')


  def test_getDeviceForPart(self):
    inputData = self.singleTransistorSchematic()
    circuit = EagleSchematic(inputData)

    transistor = circuit._getParts()[0]
    attributes = circuit._getDeviceAttributes(transistor)

    self.assertEqual(len(attributes), 3)


  def test_getNetMapForPart(self):
    inputData = self.singleTransistorSchematic()
    circuit = EagleSchematic(inputData)

    transistor = circuit._getParts()[0]
    netMap = circuit._getNetMapForPart(transistor)

    self.assertEqual(len(netMap.keys()), 3)
    self.assertEqual(netMap['COLLECTOR'], 'COLLECTOR')
    self.assertEqual(netMap['BASE'], 'BASE')
    self.assertEqual(netMap['EMITTER'], 'EMITTER')


  def test_getSpiceNetlistForPart(self):
    inputData = self.singleTransistorSchematic()
    circuit = EagleSchematic(inputData)

    transistor = circuit._getParts()[0]
    spiceData = circuit._getSpiceNetlistForPart(transistor)

    self.assertEqual(spiceData, "QQ1 COLLECTOR BASE EMITTER BC547")


  def test_getSpiceModelForPart(self):
    inputData = self.singleTransistorSchematic()
    circuit = EagleSchematic(inputData)

    transistor = circuit._getParts()[0]
    spiceData = circuit._getSpiceModelForPart(transistor)

    self.assertEqual(spiceData, ".model BC547 NPN ()")


  def test_getSpiceModelForSupplyPart(self):
    inputData = resource_string('test', "testRessources/transistorAndResistorWithSupply.sch")
    circuit = EagleSchematic(inputData)

    positiveSupply  = circuit._getNodeWithTagAndName('part', 'P+1')
    spiceModel  = circuit._getSpiceModelForPart(positiveSupply)
    spiceNet    = circuit._getSpiceNetlistForPart(positiveSupply)
    spiceSupply = circuit._getSpiceSupplyForPart(positiveSupply)

    self.assertEqual(spiceModel, None)
    self.assertEqual(spiceNet, None)
    self.assertEqual(spiceSupply, "VP5V +5V GND dc +5V ac 0V")

  def test_shouldNotCreateSupplyForGNDNode(self):
    inputData = resource_string('test', "testRessources/transistorAndResistorWithSupply.sch")
    circuit = EagleSchematic(inputData)

    negativeSupply  = circuit._getNodeWithTagAndName('part', 'GND1')
    spiceModel  = circuit._getSpiceModelForPart(negativeSupply)
    spiceNet    = circuit._getSpiceNetlistForPart(negativeSupply)
    spiceSupply = circuit._getSpiceSupplyForPart(negativeSupply)

    self.assertEqual(spiceModel, None)
    self.assertEqual(spiceNet, None)
    self.assertEqual(spiceSupply, None)

  def test_shouldNotCreateModelForUnknowNode(self):
    inputData = resource_string('test', "testRessources/transistorAndResistorWithSupplyAndTestPoint.sch")
    circuit = EagleSchematic(inputData)

    negativeSupply  = circuit._getNodeWithTagAndName('part', 'TP1')
    spiceModel  = circuit._getSpiceModelForPart(negativeSupply)
    spiceNet    = circuit._getSpiceNetlistForPart(negativeSupply)
    spiceSupply = circuit._getSpiceSupplyForPart(negativeSupply)

    self.assertEqual(spiceModel, None)
    self.assertEqual(spiceNet, None)
    self.assertEqual(spiceSupply, None)
