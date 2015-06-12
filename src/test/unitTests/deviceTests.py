import unittest
from test.testRessources.testDevices import TestTransistor


class MyTestCase(unittest.TestCase):

  def testShouldHaveCorrectSpiceModelAfterParsing(self):
    transistor = TestTransistor("Q1")

    self.assertEqual(transistor.getSpiceModel(), ".model BC547B NPN ()")

  def testShouldHaveCorrectSpiceDataAfterParsing(self):
    transistor = TestTransistor("Q1")
    transistor.connect("BaseSignal", "G$1", "BASE")
    transistor.connect("EmitterSignal", "G$1", "EMITTER")
    transistor.connect("CollectorSignal", "G$1", "COLLECTOR")

    self.assertEqual(transistor.getSpiceData(), "QQ1 CollectorSignal BaseSignal EmitterSignal BC547B")

  def testShouldAssignDifferentSignalsForUnconnectedPins(self):
    transistor = TestTransistor("Q1")
    transistor.connect("BaseSignal", "G$1", "BASE")
    transistor.connect("EmitterSignal", "G$1", "EMITTER")
    transistor.connect("CollectorSignal", "G$1", "COLLECTOR")

    baseSignal = transistor.getSignal("G$1", "BASE")
    emitterSignal = transistor.getSignal("G$1", "EMITTER")
    collectorSignal = transistor.getSignal("G$1", "COLLECTOR")

    self.assertIsNotNone(baseSignal)
    self.assertIsNotNone(collectorSignal)
    self.assertIsNotNone(emitterSignal)

    self.assertNotEqual(baseSignal, "")
    self.assertNotEqual(collectorSignal, "")
    self.assertNotEqual(emitterSignal, "")

    self.assertNotEqual(baseSignal, emitterSignal)
    self.assertNotEqual(baseSignal, collectorSignal)
    self.assertNotEqual(emitterSignal, collectorSignal)


if __name__ == '__main__':
  unittest.main()
