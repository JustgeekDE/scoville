from unittest import TestCase
from helper.eagleSchematic import EagleSchematic
from assertionMatchers import AnyStringWith


class ConversionTest(TestCase):
  def ignore_ConvertingSingleTransistor(self):

    inputData = open("../testRessources/singleTransistor.sch", 'r').read()
    circuit = EagleSchematic(inputData)

    result = circuit.getSpiceData()

    self.assertEqual(AnyStringWith("QQ1"), result)
    self.assertGreater(len(result), 5)


