from unittest import TestCase
from scoville.spiceSimulator import SpiceSimulator

__author__ = 'ppeter'


class TestSpiceSimulator(TestCase):
    def testShouldAddCorrectFooter(self):
        circuitDescription = ".end"
        self.assertEqual(SpiceSimulator.addControl(circuitDescription, "foo.data", [], 100, 1),
                         ".tran 1ms 100ms\n.control\nset filetype=ascii\nrun\nwrdata foo\n.endc\n.end")

    def testShouldAddFooterAddCorrectPlace(self):
        circuitDescription = "Vs VCC GND dc 5V ac 0V\nQa out aBase aEm BC547B\n.model BC547B NPN ()\n.end"
        self.assertEqual(SpiceSimulator.addControl(circuitDescription, "foo,data", [], 100, 1),
                         "Vs VCC GND dc 5V ac 0V\nQa out aBase aEm BC547B\n.model BC547B NPN ()\n.tran 1ms 100ms\n.control\nset filetype=ascii\nrun\nwrdata foo\n.endc\n.end")

    def testShouldAddCorrectSignals(self):
        circuitDescription = "Vs VCC GND dc 5V ac 0V\nQa out aBase aEm BC547B\n.model BC547B NPN ()\n.end"
        self.assertEqual(SpiceSimulator.addControl(circuitDescription, "foo.data", ["v(A)", "i(a)"], 100, 1),
                         "Vs VCC GND dc 5V ac 0V\nQa out aBase aEm BC547B\n.model BC547B NPN ()\n.tran 1ms 100ms\n.control\nset filetype=ascii\nrun\nwrdata foo v(A) i(a)\n.endc\n.end")

    def testShouldParseReturnDataCorrectly(self):
        exampleData = "0.000000e+00  5.000000e-01  0.000000e+00  1.000000e-01 \n 1.000000e-05  5.100000e-01  1.000000e-05  1.000000e-02 \n 2.000000e-05  5.200000e-01  2.000000e-05  1.000000e-03 \n 4.000000e-05  5.300000e-01  4.000000e-05  1.000000e-04 "
        result = SpiceSimulator.parseData(exampleData, ['a', 'b'])
        self.assertEqual(len(result), 4)

        self.assertEqual(result[0][1]['a'], 0.5)
        self.assertEqual(result[1][1]['a'], 0.51)
        self.assertEqual(result[2][1]['a'], 0.52)
        self.assertEqual(result[3][1]['a'], 0.53)

        self.assertEqual(result[0][1]['b'], 0.1)
        self.assertEqual(result[1][1]['b'], 0.01)
        self.assertEqual(result[2][1]['b'], 0.001)
        self.assertEqual(result[3][1]['b'], 0.0001)
