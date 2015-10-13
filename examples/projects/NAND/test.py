import unittest
from scoville.circuit import Circuit
from scoville.spiceSimulator import SpiceSimulator


class SimulationUnitTest(unittest.TestCase):
    def testLowLowShouldResultInHigh(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setVoltage('inA', 0.0)
        circuit.setVoltage('inB', 0.0)
        circuit.inspectVoltage('out')

        circuit.run(200)
        self.assertGreater(circuit.getVoltage('out'), 4.5)

    def testLowHighShouldResultInHigh(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setVoltage('inA', 0.0)
        circuit.setVoltage('inB', 5.0)
        circuit.inspectVoltage('out')

        circuit.run(200)
        self.assertGreater(circuit.getVoltage('out'), 4.5)

    def testHighLowShouldResultInHigh(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setVoltage('inA', 5)
        circuit.setVoltage('inB', 0)
        circuit.inspectVoltage('out')

        circuit.run(200)
        self.assertGreater(circuit.getVoltage('out'), 4.5)

    def testHighHighShouldResultInLow(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setVoltage('inA', 5)
        circuit.setVoltage('inB', 5)
        circuit.inspectVoltage('out')

        circuit.run(200)
        self.assertLess(circuit.getVoltage('out'), 0.5)

    def testShouldNotUseTooMuchCurrent(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setVoltage('inA', 5)
        circuit.setVoltage('inB', 5)
        circuit.inspectCurrent('Vs')

        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), 0.1)

        circuit.setVoltage('inA', 0)
        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), 0.1)

        circuit.setVoltage('inB', 0)
        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), 0.1)

        circuit.setVoltage('inA', 5)
        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), 0.001)

if __name__ == '__main__':
    unittest.main()
