from unittest import TestCase
from pkg_resources import resource_string

from scoville import eagleSchematic


class ConversionTest(TestCase):
  def singleTransistorSchematic(self):
    return self.getSchematic('singleTransistor.sch')

  def getSchematic(self, schematic):
    return resource_string('test', 'testRessources/simulationExamples/' + schematic)

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
    inputData = self.getSchematic('transistorAndResistorWithSupply.sch')
    circuit = eagleSchematic.EagleSchematic(inputData)

    positiveSupply = circuit.parts['P+1']
    spiceModel = positiveSupply.getSpiceModel()
    spiceNet = positiveSupply.getSpiceNetlist()
    spiceSupply = positiveSupply.getSpiceSupply()

    self.assertEqual(spiceModel, None)
    self.assertEqual(spiceNet, None)
    self.assertEqual(spiceSupply, "VP5V +5V GND dc +5V ac 0V")

  def test_shouldNotCreateSupplyForGNDNode(self):
    inputData = self.getSchematic('transistorAndResistorWithSupply.sch')
    circuit = eagleSchematic.EagleSchematic(inputData)

    negativeSupply = circuit.parts['GND1']
    spiceModel = negativeSupply.getSpiceModel()
    spiceNet = negativeSupply.getSpiceNetlist()
    spiceSupply = negativeSupply.getSpiceSupply()

    self.assertEqual(spiceModel, None)
    self.assertEqual(spiceNet, None)
    self.assertEqual(spiceSupply, None)

  def test_shouldNotCreateModelForUnknowNode(self):
    inputData = self.getSchematic('transistorAndResistorWithSupplyAndTestPoint.sch')
    circuit = eagleSchematic.EagleSchematic(inputData)

    testPoint = circuit.parts['TP1']
    spiceModel = testPoint.getSpiceModel()
    spiceNet = testPoint.getSpiceNetlist()
    spiceSupply = testPoint.getSpiceSupply()

    self.assertEqual(spiceModel, None)
    self.assertEqual(spiceNet, None)
    self.assertEqual(spiceSupply, None)

  def test_shouldCreateSubCircuitForModelWithSubCircuit(self):
    inputData = self.getSchematic('relayWithSubCircuit.sch')
    circuit = eagleSchematic.EagleSchematic(inputData)

    relay = circuit.parts['RELAY1']
    spiceModel = relay.getSpiceModel()
    spiceNet = relay.getSpiceNetlist()
    spiceSupply = relay.getSpiceSupply()
    spiceSubCircuit = relay.getSpiceSubCircuit()

    self.assertEqual(spiceModel, None)
    self.assertEqual(spiceNet, 'xRELAY1 NOP CENT NCL NPOS NNEG basicRelay')
    self.assertEqual(spiceSupply, None)
    self.assertEqual(spiceSubCircuit, ".subckt basicRelay  1   2   3   4   5\nSOpen 1 2 4 5 SW_OPEN on\nSClosed 2 3 4 5 SW_CLOSED on\n.model SW_OPEN SW(Ron=.1 Roff=1Meg Vt=6 )\n.model SW_CLOSED SW(Ron=1Meg Roff=.1 Vt=6 )\n.ends")

