from unittest import TestCase
from helper.eagleSchematic import EagleSchematic
from assertionMatchers import AnyStringWith


class ConversionTest(TestCase):

  def test_extractSinglePartCorrectly(self):
    inputData = open("../testRessources/singleTransistor.sch", 'r').read()
    circuit = EagleSchematic(inputData)

    parts = circuit._getParts()

    self.assertEqual(len(parts), 1)
    self.assertEqual(parts[0].getAttribute('name'), 'Q1')


  def test_extractSingleDeviceCorrectly(self):
    inputData = open("../testRessources/singleTransistor.sch", 'r').read()
    circuit = EagleSchematic(inputData)

    devices = circuit._getDevices()

    self.assertEqual(len(devices), 1)
    self.assertEqual(devices[0].getAttribute('name'), 'TRANSISTOR-NPN-GENERIC')


  def test_getDeviceForPart(self):
    inputData = open("../testRessources/singleTransistor.sch", 'r').read()
    circuit = EagleSchematic(inputData)

    transistor = circuit._getParts()[0]
    attributes = circuit._getDeviceAttributes(transistor)

    self.assertEqual(len(attributes), 3)

  def test_getNetMapForPart(self):
    inputData = open("../testRessources/singleTransistor.sch", 'r').read()
    circuit = EagleSchematic(inputData)

    transistor = circuit._getParts()[0]
    netMap = circuit._getNetMapForPart(transistor)

    self.assertEqual(len(netMap.keys()), 3)
    self.assertEqual(netMap['COLLECTOR'], 'COLLECTOR')
    self.assertEqual(netMap['BASE'], 'BASE')
    self.assertEqual(netMap['EMITTER'], 'EMITTER')

  def test_getSpiceNetlistForPart(self):
    inputData = open("../testRessources/singleTransistor.sch", 'r').read()
    circuit = EagleSchematic(inputData)

    transistor = circuit._getParts()[0]
    spiceData = circuit._getSpiceNetlistForPart(transistor)

    self.assertEqual(spiceData, "QQ1 COLLECTOR BASE EMITTER BC547")


  def test_getSpiceModelForPart(self):
    inputData = open("../testRessources/singleTransistor.sch", 'r').read()
    circuit = EagleSchematic(inputData)

    transistor = circuit._getParts()[0]
    spiceData = circuit._getSpiceModelForPart(transistor)

    self.assertEqual(spiceData, ".model BC547 NPN ()")
