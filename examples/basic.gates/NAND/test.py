import unittest

from scoville.circuit import Circuit
from scoville.signal import SignalWithResistance, DelayedSignal


class SimulationUnitTest(unittest.TestCase):
    def testLowLowShouldResultInHigh(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("A", 0.0, 10))
        circuit.setSignal(SignalWithResistance("B", 0.0, 10))
        circuit.inspectVoltage('NAND')

        circuit.run(200)
        self.assertGreater(circuit.getVoltage('NAND'), 4.5)

    def testLowHighShouldResultInHigh(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("A", 0.0, 10))
        circuit.setSignal(SignalWithResistance("B", 5.0, 10))
        circuit.inspectVoltage('NAND')

        circuit.run(200)
        self.assertGreater(circuit.getVoltage('NAND'), 4.5)

    def testHighLowShouldResultInHigh(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("A", 5.0, 10))
        circuit.setSignal(SignalWithResistance("B", 0.0, 10))
        circuit.inspectVoltage('NAND')

        circuit.run(200)
        self.assertGreater(circuit.getVoltage('NAND'), 4.5)

    def testHighHighShouldResultInLow(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("A", 5.0, 10))
        circuit.setSignal(SignalWithResistance("B", 5.0, 10))
        circuit.inspectVoltage('NAND')

        circuit.run(200)
        self.assertLess(circuit.getVoltage('NAND'), 0.5)

    def testShouldNotUseTooMuchCurrent(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("A", 5.0, 10))
        circuit.setSignal(SignalWithResistance("B", 5.0, 10))
        circuit.inspectCurrent('Vs')

        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), .001)

        circuit.setSignal(SignalWithResistance("A", 0.0, 10))
        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), 0.001)

        circuit.setSignal(SignalWithResistance("B", 0.0, 10))
        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), 0.001)

        circuit.setSignal(SignalWithResistance("A", 5.0, 10))
        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), 0.001)

    def testShouldSwitchOffIn100ns(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("A", 5.0, 10))
        circuit.setSignal(DelayedSignal("B", 5.0, 100, 10))
        circuit.inspectVoltage('NAND')

        circuit.run(200, 0.1)
        self.assertLess(circuit.getMaxVoltage('NAND', 100.1, 200), 0.5)

    def testShouldSwitchOnIn100ns(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("A", 5.0, 10))
        circuit.setSignal(DelayedSignal("B", value=0.0, delay=100, resistance=10, startValue=5.0))
        circuit.inspectVoltage('NAND')

        circuit.run(200, 0.1)
        self.assertGreater(circuit.getMinVoltage('NAND', 100.1, 200), 4.5)


if __name__ == '__main__':
    unittest.main()
