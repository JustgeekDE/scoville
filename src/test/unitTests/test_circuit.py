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
        simulator = SpiceSimulator()
        simulator.run = MagicMock(return_value = [])

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


