import unittest

from scoville.circuit import Circuit
from scoville.signal import SignalWithResistance


class SimulationUnitTest(unittest.TestCase):

    def setupCircuit(self):
        circuit = Circuit.fromFile("ALU.cir")

        circuit.setSignal(SignalWithResistance("A", 0.0, 10))
        circuit.setSignal(SignalWithResistance("B", 0.0, 10))
        circuit.setSignal(SignalWithResistance("C", 0.0, 10))
        circuit.setSignal(SignalWithResistance("INV", 0.0, 10))

        circuit.inspectVoltage('XOR')
        circuit.inspectVoltage('NAND')
        circuit.inspectVoltage('NOR')
        circuit.inspectVoltage('CARRY')
        circuit.inspectVoltage('SUM')

        circuit.inspectCurrent('Vs')

        return circuit

    def testAllLow(self):
        circuit = self.setupCircuit()

        circuit.run(200)
        self.assertLess(circuit.getVoltage('XOR'), 0.5)
        self.assertLess(circuit.getVoltage('CARRY'), 0.5)
        self.assertLess(circuit.getVoltage('SUM'), 0.5)
        self.assertGreater(circuit.getVoltage('NAND'), 4.5)
        self.assertGreater(circuit.getVoltage('NOR'), 4.5)
        self.assertLess(circuit.getCurrent('Vs'), 0.1)

    def testAdderSingleBit(self):
        circuit = self.setupCircuit()

        circuit.setSignal(SignalWithResistance("A", 5.0, 10))
        circuit.setSignal(SignalWithResistance("B", 0.0, 10))
        circuit.setSignal(SignalWithResistance("C", 0.0, 10))
        circuit.run(200)
        self.assertLess(circuit.getVoltage('CARRY'), 0.5)
        self.assertGreater(circuit.getVoltage('SUM'), 4.5)
        self.assertLess(circuit.getCurrent('Vs'), 0.1)

        circuit.setSignal(SignalWithResistance("A", 0.0, 10))
        circuit.setSignal(SignalWithResistance("B", 5.0, 10))
        circuit.setSignal(SignalWithResistance("C", 0.0, 10))
        circuit.run(200)
        self.assertLess(circuit.getVoltage('CARRY'), 0.5)
        self.assertGreater(circuit.getVoltage('SUM'), 4.5)
        self.assertLess(circuit.getCurrent('Vs'), 0.1)

        circuit.setSignal(SignalWithResistance("A", 0.0, 10))
        circuit.setSignal(SignalWithResistance("B", 0.0, 10))
        circuit.setSignal(SignalWithResistance("C", 5.0, 10))
        circuit.run(200)
        self.assertLess(circuit.getVoltage('CARRY'), 0.5)
        self.assertGreater(circuit.getVoltage('SUM'), 4.5)
        self.assertLess(circuit.getCurrent('Vs'), 0.1)

    def testAdderTwoBits(self):
        circuit = self.setupCircuit()

        circuit.setSignal(SignalWithResistance("A", 5.0, 10))
        circuit.setSignal(SignalWithResistance("B", 5.0, 10))
        circuit.setSignal(SignalWithResistance("C", 0.0, 10))
        circuit.run(200)
        self.assertGreater(circuit.getVoltage('CARRY'), 4.5)
        self.assertLess(circuit.getVoltage('SUM'), 0.5)
        self.assertLess(circuit.getCurrent('Vs'), 0.1)

        circuit.setSignal(SignalWithResistance("A", 0.0, 10))
        circuit.setSignal(SignalWithResistance("B", 5.0, 10))
        circuit.setSignal(SignalWithResistance("C", 5.0, 10))
        circuit.run(200)
        self.assertGreater(circuit.getVoltage('CARRY'), 4.5)
        self.assertLess(circuit.getVoltage('SUM'), 0.5)
        self.assertLess(circuit.getCurrent('Vs'), 0.1)

        circuit.setSignal(SignalWithResistance("A", 5.0, 10))
        circuit.setSignal(SignalWithResistance("B", 0.0, 10))
        circuit.setSignal(SignalWithResistance("C", 5.0, 10))
        circuit.run(200)
        self.assertGreater(circuit.getVoltage('CARRY'), 4.5)
        self.assertLess(circuit.getVoltage('SUM'), 0.5)
        self.assertLess(circuit.getCurrent('Vs'), 0.1)

if __name__ == '__main__':
    unittest.main()
