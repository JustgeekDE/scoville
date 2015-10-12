import uuid


class Circuit:
    originalData = ""
    usedParts = []
    inspectedElements = []
    simulationTime = 0

    def __init__(self, circuitData):
        self.originalData = circuitData

    @staticmethod
    def fromFile(fileName):
        with open(fileName, 'r') as circuitFile:
            return Circuit(circuitFile.read())
        return None

    def convertToList(self, input):
        if not (isinstance(input, list)):
            input = [input]
        return input

    def use(self, parts):
        parts = self.convertToList(parts)
        self.usedParts = self.usedParts.extend(parts)

    def inspect(self, signals):
        return ""

    def setVoltage(self, signal, voltage, resistance=0.0):
        return ""

    def run(self, duration=200, steps=1):
        return ""

    def getVoltage(self, signal):
        return ""

    def getMinVoltage(self, signal, start=0, end=None):
        return ""

    def getMaxVoltage(self, signal, start=0, end=None):
        return ""

    def getCurrent(self, signal):
        return ""

    def getMinCurrent(self, signal, start=0, end=None):
        return ""

    def getMaxCurrent(self, signal, start=0, end=None):
        return ""
