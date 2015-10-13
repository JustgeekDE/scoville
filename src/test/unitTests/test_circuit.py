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
        returnData.append((0, {'a': 1.0, 'b':5.0}))
        returnData.append((1, {'a': 2.0, 'b':2.0}))
        returnData.append((2, {'a': 3.0, 'b':5.0}))
        returnData.append((3, {'a': 4.0, 'b':2.0}))

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