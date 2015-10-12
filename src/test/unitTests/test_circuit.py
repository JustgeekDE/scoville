from unittest import TestCase
from mock import MagicMock

from scoville.circuit import Circuit
from scoville.spiceSimulator import SpiceSimulator

__author__ = 'ppeter'

class TestCircuit(TestCase):
    def getExamplecircuit(self):
        return open("../testRessources/NAND.cir", 'r').read()



    def testShouldCallSimulator(self):
        simulator = SpiceSimulator()
        simulator.run = MagicMock(return_value = [])

        circuitDescription = self.getExamplecircuit()
        circuit = Circuit(circuitDescription)
        circuit.simulator = simulator

        circuit.run()

        self.assertTrue(simulator.run.called)


    # def testShouldRemoveComponentsFromSimulation(self):
    #     circuitDescription = self.getExamplecircuit()
    #
    #     circuit = Circuit(circuitDescription)
    #     circuit.use("Qa")



