from unittest import TestCase
from pkg_resources import resource_string

import eagleLibrary
from scoville import eagleBoard


class ConversionTest(TestCase):
  def getBoard(self, schematic):
    inputData = resource_string('test', 'testRessources/replacementExamples/' + schematic + '.brd')
    return eagleBoard.EagleBoard(inputData)

  def test_getLibraries(self):
    board = self.getBoard('singleLED')

    libraries = board.getLibraries()
    self.assertEqual(len(libraries.values()), 1)
    self.assertEqual(libraries.keys()[0], 'led')

