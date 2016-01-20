from unittest import TestCase
from pkg_resources import resource_string

from test.assertionMatchers import AnyListWithString
from scoville.eagleSchematic import EagleSchematic


class ConversionTest(TestCase):

  def test_ConvertingSingleTransistor(self):
    inputData = resource_string('test', 'testRessources/singleTransistor.sch')
    circuit = EagleSchematic(inputData)

    result = circuit.getSpiceData().split("\n")

    self.assertEqual(AnyListWithString("QQ1 COLLECTOR BASE EMITTER BC547"), result)
    self.assertEqual(AnyListWithString(".model BC547 NPN ()"), result)

  def test_ConvertingTwoParts(self):
    inputData = resource_string('test', 'testRessources/transistorAndResistor.sch')
    circuit = EagleSchematic(inputData)

    result = circuit.getSpiceData().split("\n")

    self.assertEqual(AnyListWithString("QQ1 COLLECTOR BASE GND BC547"), result)
    self.assertEqual(AnyListWithString("RR1 COLLECTOR +5V 10k"), result)
    self.assertEqual(AnyListWithString(".model BC547 NPN ()"), result)