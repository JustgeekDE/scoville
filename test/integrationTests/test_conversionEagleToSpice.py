from unittest import TestCase
from pkg_resources import resource_string

from test.assertionMatchers import AnyListWithString
from scoville.eagleSchematic import EagleSchematic


class ConversionTest(TestCase):

  def getSchematic(self, schematic):
    return resource_string('test', 'testRessources/simulationExamples/' + schematic)

  def test_ConvertingSingleTransistor(self):
    inputData = self.getSchematic('singleTransistor.sch')
    circuit = EagleSchematic(inputData)

    result = circuit.getSpiceData().split("\n")

    self.assertEqual(AnyListWithString("QQ1 COLLECTOR BASE EMITTER BC547"), result)
    self.assertEqual(AnyListWithString(".model BC547 NPN ()"), result)

  def test_ConvertingTwoParts(self):
    inputData = self.getSchematic('transistorAndResistor.sch')
    circuit = EagleSchematic(inputData)

    result = circuit.getSpiceData().split("\n")

    self.assertEqual(AnyListWithString("QQ1 COLLECTOR BASE GND BC547"), result)
    self.assertEqual(AnyListWithString("RR1 COLLECTOR +5V 10k"), result)
    self.assertEqual(AnyListWithString(".model BC547 NPN ()"), result)

  def test_ConvertingWithVoltageSource(self):
    inputData = self.getSchematic('transistorAndResistorWithSupply.sch')
    circuit = EagleSchematic(inputData)

    result = circuit.getSpiceData().split("\n")

    self.assertEqual(AnyListWithString("VP5V +5V GND dc +5V ac 0V"), result)
    self.assertEqual(AnyListWithString("QQ1 COLLECTOR BASE GND BC547"), result)
    self.assertEqual(AnyListWithString("RR1 COLLECTOR +5V 10k"), result)
    self.assertEqual(AnyListWithString(".model BC547 NPN ()"), result)

  def test_ConversionShouldIncludeEndTag(self):
    inputData = self.getSchematic('singleTransistor.sch')
    circuit = EagleSchematic(inputData)

    result = circuit.getSpiceData().split("\n")

    self.assertEqual('.end', result[-1])

  def test_ConversionShouldIncludeSubCircuits(self):
    inputData = self.getSchematic('relayWithSubCircuit.sch')
    circuit = EagleSchematic(inputData)

    result = circuit.getSpiceData().split("\n")

    self.assertEqual(AnyListWithString(".model SW_OPEN SW(Ron=.1 Roff=1Meg Vt=6 )"), result)
