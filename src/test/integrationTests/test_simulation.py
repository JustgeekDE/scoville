from unittest import TestCase
from scoville.spiceSimulator import SpiceSimulator


class SimulationUnitTest(TestCase):
  def testSimulatesSingleNand(self):
    simulator = SpiceSimulator()

    circuit = open("../testRessources/NAND.cir", 'r').read()
    data = simulator.run(circuit, ["v(out)", "i(Vs)"], 5, 1)

    self.assertGreater(len(data), 5)
    self.assertEqual(data[0][1]['v(out)'], 5.0)
    self.assertEqual(data[-1][1]['v(out)'], 5.0)


