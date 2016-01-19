from unittest import TestCase
from helper.eagleSchematic import EagleSchematic
from assertionMatchers import AnyStringWith, AnyListWithString


class ConversionTest(TestCase):
  def test_ConvertingSingleTransistor(self):

    inputData = open("../testRessources/singleTransistor.sch", 'r').read()
    circuit = EagleSchematic(inputData)

    result = circuit.getSpiceData().split("\n")

    self.assertEqual(AnyListWithString("QQ1 COLLECTOR BASE EMITTER BC547"), result)
    self.assertEqual(AnyListWithString(".model BC547 NPN ()"), result)


  def test_ConvertingTwoParts(self):

    inputData = open("../testRessources/transistorAndResistor.sch", 'r').read()
    circuit = EagleSchematic(inputData)

    result = circuit.getSpiceData().split("\n")

    self.assertEqual(AnyListWithString("QQ1 COLLECTOR BASE GND BC547"), result)
    self.assertEqual(AnyListWithString("RR1 COLLECTOR +5V 10k"), result)
    self.assertEqual(AnyListWithString(".model BC547 NPN ()"), result)


