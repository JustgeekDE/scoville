from scoville.spiceSimulator import SpiceSimulator


class Circuit:
    originalData = ""
    usedParts = []
    inspectedElements = []
    simulationTime = 0
    simulator = SpiceSimulator()

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
        self.usedParts.extend(parts)

    def inspect(self, signals):
        return ""

    def setVoltage(self, signal, voltage, resistance=0.0):
        return ""

    def run(self, duration=200, steps=1):
        strippedData = self.removeParts(self.originalData, self.usedParts)
        self.simulator.run(strippedData, self.inspectedElements, duration, steps)

    def removeParts(self, circuit, partsToKeep):
        result = ""
        for line in circuit.splitlines():
            line = line.strip()
            if line.startswith('.') or line.startswith('*'):
                result += "\n" + line
                continue
            if any(part+" " in line for part in partsToKeep):
                result += "\n" + line
                continue
        return result

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
