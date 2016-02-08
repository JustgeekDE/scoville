from unittest import TestCase
from pkg_resources import resource_string

from scoville.spiceSimulator import SpiceSimulator


class SimulationUnitTest(TestCase):
  def testSimulatesSingleNand(self):
    simulator = SpiceSimulator()

    circuit = resource_string('test', 'testRessources/simulationExamples/NAND.cir')

    data = simulator.run(circuit, ["v(out)", "i(Vs)"], 5, 1)

    self.assertGreater(len(data), 5)
    self.assertEqual(data[0][1]['v(out)'], 5.0)
    self.assertEqual(data[-1][1]['v(out)'], 5.0)


