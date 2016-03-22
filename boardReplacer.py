#!/usr/bin/env python

if __name__ == '__main__':
    pass

import argparse
from scoville import eagleBoard

parser = argparse.ArgumentParser(description='Profile xcode build run')
parser.add_argument('-i', dest='inputFile', action='store', help='input schematic')
parser.add_argument('-o', dest='outputFile', action='store', help='output name')
parser.add_argument('-r', dest='replacementFile', action='store', help='replacement schematic')
parser.add_argument('-p', dest='packageName', action='store', help='name of package to replace')

args = parser.parse_args()

def openBoard(filename):
  file = open(filename, "r")
  return eagleBoard.EagleBoard(file.read())

def saveBoard(filename, schematic):
  file = open(filename, "w")
  file.write(schematic.toString())


inputBoard = openBoard(args.inputFile)
replacementBoard = openBoard(args.replacementFile)

inputBoard.replaceByPackage(args.packageName, replacementBoard)

saveBoard(args.outputFile, inputBoard)

