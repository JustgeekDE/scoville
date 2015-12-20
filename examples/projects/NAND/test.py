import unittest

from scoville.circuit import Circuit
from scoville.signal import SignalWithResistance, DelayedSignal


class SimulationUnitTest(unittest.TestCase):
    def testLowLowShouldResultInHigh(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("inA", 0.0, 10))
        circuit.setSignal(SignalWithResistance("inB", 0.0, 10))
        circuit.inspectVoltage('out')

        circuit.run(200)
        self.assertGreater(circuit.getVoltage('out'), 4.5)

    def testLowHighShouldResultInHigh(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("inA", 0.0, 10))
        circuit.setSignal(SignalWithResistance("inB", 5.0, 10))
        circuit.inspectVoltage('out')

        circuit.run(200)
        self.assertGreater(circuit.getVoltage('out'), 4.5)

    def testHighLowShouldResultInHigh(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("inA", 5.0, 10))
        circuit.setSignal(SignalWithResistance("inB", 0.0, 10))
        circuit.inspectVoltage('out')

        circuit.run(200)
        self.assertGreater(circuit.getVoltage('out'), 4.5)

    def testHighHighShouldResultInLow(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("inA", 5.0, 10))
        circuit.setSignal(SignalWithResistance("inB", 5.0, 10))
        circuit.inspectVoltage('out')

        circuit.run(200)
        self.assertLess(circuit.getVoltage('out'), 0.5)

    def testShouldSwitchOnIn100ns(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("inA", 5.0, 10))
        circuit.setSignal(DelayedSignal("inB", value=0.0, delay=100, resistance=10, startValue=5.0))
        circuit.inspectVoltage('out')

        circuit.run(200, 0.1)
        self.assertGreater(circuit.getMinVoltage('out', 100.1, 200), 4.5)

    def testShouldSwitchOffIn100ns(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("inA", 5.0, 10))
        circuit.setSignal(DelayedSignal("inB", 5.0, 100, 10))
        circuit.inspectVoltage('out')

        circuit.run(200, 0.1)
        self.assertGreater(circuit.getMinVoltage('out', 0, 100), 4.5)
        self.assertLess(circuit.getMaxVoltage('out', 100.1, 200), 0.5)

    def testShouldNotUseTooMuchCurrent(self):
        circuit = Circuit.fromFile("NAND.cir")

        circuit.setSignal(SignalWithResistance("inA", 5.0, 10))
        circuit.setSignal(SignalWithResistance("inB", 5.0, 10))
        circuit.inspectCurrent('Vs')

        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), .001)

        circuit.setSignal(SignalWithResistance("inA", 0.0, 10))
        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), 0.001)

        circuit.setSignal(SignalWithResistance("inB", 0.0, 10))
        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), 0.001)

        circuit.setSignal(SignalWithResistance("inA", 5.0, 10))
        circuit.run(200)
        self.assertLess(circuit.getMaxCurrent('Vs'), 0.001)


if __name__ == '__main__':
    unittest.main()
