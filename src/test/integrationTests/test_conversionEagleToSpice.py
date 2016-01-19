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


