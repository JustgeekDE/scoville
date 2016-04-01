from unittest import TestCase
from pkg_resources import resource_string

import eagleLibrary
from scoville import eagleSchematic


class LibraryTest(TestCase):
  def getSchematic(self, schematic):
    inputData = resource_string('test', 'testRessources/replacementExamples/' + schematic + '.sch')
    return eagleSchematic.EagleSchematic(inputData)

  def test_mergingLibrariesShouldMergePackages(self):
    schematicA = self.getSchematic('singleGateFromLibrary')
    schematicB = self.getSchematic('differentGateFromLibrary')

    libraryA = schematicA.getLibraries()['p.peter-gator']
    libraryB = schematicB.getLibraries()['p.peter-gator']

    libraryA.merge(libraryB)

    self.assertIn('<package name="NAND"', libraryA.toString())
    self.assertIn('<package name="OR"', libraryA.toString())

    self.assertIn('<symbol name="NAND"', libraryA.toString())
    self.assertIn('<symbol name="OR"', libraryA.toString())

    self.assertIn('<deviceset name="NAND"', libraryA.toString())
    self.assertIn('<deviceset name="OR"', libraryA.toString())

  def test_mergingTwoDifferenLibrariesShouldntMergePackages(self):
    schematicA = self.getSchematic('singleGateFromLibrary')
    schematicB = self.getSchematic('differentGateFromLibrary')

    libraryA = schematicA.getLibraries()['p.peter-gator']
    libraryB = schematicB.getLibraries()['p.peter-gator']

    libraryB.name = 'foo'
    libraryA.merge(libraryB)

    self.assertIn('<package name="NAND"', libraryA.toString())
    self.assertNotIn('<package name="OR"', libraryA.toString())

