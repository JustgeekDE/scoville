from unittest import TestCase
from circuit import spiceSimulator
from circuit.spiceSimulator import SpiceSimulator

__author__ = 'ppeter'


class TestSpiceSimulator(TestCase):

    def testShouldAddCorrectFooter(self):
        circuitDescription = ".end"
        self.assertEqual(SpiceSimulator.addControl(circuitDescription, "foo.dat", []), ".control\nset filetype=ascii\nrun\nwrdata foo.dat\n.endc\n.end")

    def testShouldAddFooterAddCorrectPlace(self):
        circuitDescription = "Vs VCC GND dc 5V ac 0V\nQa out aBase aEm BC547B\n.model BC547B NPN ()\n.tran 1ms 100ms\n.end"
        self.assertEqual(SpiceSimulator.addControl(circuitDescription, "foo.dat", []), "Vs VCC GND dc 5V ac 0V\nQa out aBase aEm BC547B\n.model BC547B NPN ()\n.tran 1ms 100ms\n.control\nset filetype=ascii\nrun\nwrdata foo.dat\n.endc\n.end")

    def testShouldAddCorrectSignals(self):
        circuitDescription = "Vs VCC GND dc 5V ac 0V\nQa out aBase aEm BC547B\n.model BC547B NPN ()\n.tran 1ms 100ms\n.end"
        self.assertEqual(SpiceSimulator.addControl(circuitDescription, "foo.dat", ["v(A)", "i(a)"]), "Vs VCC GND dc 5V ac 0V\nQa out aBase aEm BC547B\n.model BC547B NPN ()\n.tran 1ms 100ms\n.control\nset filetype=ascii\nrun\nwrdata foo.dat v(A) i(a)\n.endc\n.end")

    def testShouldParseReturnDataCorrectly(self):
        exampleData = "0.000000e+00  5.000000e-01  0.000000e+00  1.000000e-01 \n 1.000000e-05  5.100000e-01  1.000000e-05  1.000000e-02 \n 2.000000e-05  5.200000e-01  2.000000e-05  1.000000e-03 \n 4.000000e-05  5.300000e-01  4.000000e-05  1.000000e-04 "
        result = SpiceSimulator.parseData(exampleData, ['a', 'b'])
        self.assertEqual(len(result), 4)

