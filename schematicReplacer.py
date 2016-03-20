#!/usr/bin/env python

if __name__ == '__main__':
    pass

import argparse
from scoville import eagleSchematic

parser = argparse.ArgumentParser(description='Profile xcode build run')
parser.add_argument('-i', dest='inputFile', action='store', help='input schematic')
parser.add_argument('-o', dest='outputFile', action='store', help='output name')
parser.add_argument('-r', dest='replacementFile', action='store', help='replacement schematic')
parser.add_argument('-p', dest='partName', action='store', help='name of part to replace')

args = parser.parse_args()

def openSchematic(filename):
  file = open(filename, "r")
  return eagleSchematic.EagleSchematic(file.read())

def saveSchematic(filename, schematic):
  file = open(filename, "w")
  file.write(schematic.toString())


inputSchematic = openSchematic(args.inputFile)
replacementSchematic = openSchematic(args.replacementFile)

inputSchematic.replace(args.partName, replacementSchematic)

saveSchematic(args.outputFile, inputSchematic)

