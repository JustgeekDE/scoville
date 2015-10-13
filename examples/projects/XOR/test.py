import unittest

from scoville.circuit import Circuit
from scoville.signal import SignalWithResistance, DelayedSignal


class SimulationUnitTest(unittest.TestCase):

    def setupCircuit(self):
        circuit = Circuit.fromFile("XOR.cir")

        circuit.setSignal(SignalWithResistance("A", 0.0, 10))
        circuit.setSignal(SignalWithResistance("B", 0.0, 10))

        circuit.inspectVoltage('AND')
        circuit.inspectVoltage('NOR')
        circuit.inspectVoltage('XOR')

        circuit.inspectCurrent('Vs')

        return circuit

    def testAllLow(self):
        circuit = self.setupCircuit()

        circuit.run(200)
        self.assertLess(circuit.getVoltage('AND'), 0.5)
        self.assertGreater(circuit.getVoltage('NOR'), 4.5)
        self.assertLess(circuit.getVoltage('XOR'), 0.5)
        self.assertLess(circuit.getCurrent('Vs'), 0.1)


if __name__ == '__main__':
    unittest.main()
