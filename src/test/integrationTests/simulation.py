import unittest
from circuit.spiceSimulator import SpiceSimulator


class SimulationUnitTest(unittest.TestCase):
    def testSimulatesSingleNand(self):
        circuit = open("../testRessources/NAND.cir", 'r').read()
        data = SpiceSimulator.run(circuit, ["v(out)", "i(Vs)"], 5, 1)

        self.assertGreater(len(data), 5)
        self.assertEqual(data[0][1]['v(out)'], 5.0)
        self.assertEqual(data[-1][1]['v(out)'], 5.0)


if __name__ == '__main__':
    unittest.main()
