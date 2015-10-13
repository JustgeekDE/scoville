from unittest import TestCase
from mock import MagicMock
from assertionMatchers import AnyStringWith, Any, AnyStringWithOut, AnyListWithString

from scoville.circuit import Circuit
from scoville.spiceSimulator import SpiceSimulator

__author__ = 'ppeter'



class TestCircuit(TestCase):
    def getExampleDescription(self):
        return open("../testRessources/NAND.cir", 'r').read()

    def getExampleCircuit(self):
        returnData = []
        returnData.append((0, {'v(a)': 1.0, 'v(b)':5.0,'i(a)': 0.0, 'i(b)':6.0}))
        returnData.append((1, {'v(a)': 2.0, 'v(b)':2.0,'i(a)': 0.1, 'i(b)':0.0}))
        returnData.append((2, {'v(a)': 3.0, 'v(b)':5.0,'i(a)': 0.2, 'i(b)':0.0}))
        returnData.append((3, {'v(a)': 4.0, 'v(b)':2.0,'i(a)': 0.3, 'i(b)':6.0}))

        simulator = SpiceSimulator()
        simulator.run = MagicMock(return_value = returnData)

        circuitDescription = self.getExampleDescription()
        circuit = Circuit(circuitDescription)
        circuit.simulator = simulator

        return (circuit, simulator)

    def testShouldCallSimulator(self):
        (circuit, simulator) = self.getExampleCircuit()
        circuit.run()
        self.assertTrue(simulator.run.called)


    def testShouldRemoveComponentsFromSimulation(self):
        (circuit, simulator) = self.getExampleCircuit()

        circuit.use("Qa")
        circuit.run()

        simulator.run.assert_called_once_with(AnyStringWith("Qa"), Any(), Any(), Any())
        simulator.run.assert_called_once_with(AnyStringWithOut("Qb"), Any(), Any(), Any())
        simulator.run.assert_called_once_with(AnyStringWithOut("Ra"), Any(), Any(), Any())
        simulator.run.assert_called_once_with(AnyStringWithOut("Rb"), Any(), Any(), Any())

    def testShouldInspectBothCurrentAndVoltage(self):
        (circuit, simulator) = self.getExampleCircuit()

        circuit.inspect("out")
        circuit.run()

        simulator.run.assert_called_once_with(Any(), AnyListWithString("v(out)"), Any(), Any())
        simulator.run.assert_called_once_with(Any(), AnyListWithString("i(out)"), Any(), Any())

    def testShouldMockSignalWithResistance(self):
        (circuit, simulator) = self.getExampleCircuit()

        circuit.setVoltage("inA", 5.0, 1000)
        circuit.run()

        simulator.run.assert_called_once_with(AnyStringWith("VmockinA inAMockR GND dc 5.0V ac 0V"), Any(), Any(), Any())
        simulator.run.assert_called_once_with(AnyStringWith("RmockinA inAMockR inA 1000"), Any(), Any(), Any())

    def testShouldAllowSignalInspection(self):
        (circuit, simulator) = self.getExampleCircuit()

        circuit.run()

        self.assertEqual(circuit.getVoltage('a'), 4.0)
        self.assertEqual(circuit.getVoltage('b'), 2.0)