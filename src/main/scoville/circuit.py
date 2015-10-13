from scoville.spiceSimulator import SpiceSimulator


class Circuit:
    originalData = ""
    usedParts = []
    inspectedElements = []
    mocks = []
    simulationTime = 0
    simulator = SpiceSimulator()
    simulationResult = None

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

    def inspect(self, signal):
        self.inspectedElements.append("v("+signal+")")
        self.inspectedElements.append("i("+signal+")")

    def run(self, duration=200, steps=1):
        strippedData = self.removeParts(self.originalData, self.usedParts)
        mocks = self.getMocks()

        circuit = mocks + strippedData
        self.simulationResult = self.simulator.run(circuit, self.inspectedElements, duration, steps)

    def removeParts(self, circuit, partsToKeep):
        result = ""
        for line in circuit.splitlines():
            if self.keepLine(line, partsToKeep):
                result += "\n" + line
        return result

    def keepLine(self, line, partsToKeep):
        line = line.strip()
        if line.startswith('.') or line.startswith('*'):
            return True
        if any(part+" " in line for part in partsToKeep):
            return True
        return False

    def getMocks(self):
        result = ""
        for (signal, voltage, resistance) in self.mocks:
            result += "Vmock{0} {0}MockR GND dc {1}V ac 0V\n".format(signal, voltage)
            result += "Rmock{0} {0}MockR {0} {1}\n".format(signal, resistance)
        return result

    def setVoltage(self, signal, voltage, resistance=0.0):
        self.mocks.append((signal, voltage, resistance))

    def getVoltage(self, signal):
        signal = "v({})".format(signal)
        return self.getSignal(signal)

    def getMinVoltage(self, signal, start=0, end=None):
        signal = "v({})".format(signal)
        min = None
        for (timestamp, data) in self.simulationResult:
            if timestamp >= start and (end == None or timestamp <= end):
                if data[signal] < min or min == None:
                    min = data[signal]
        return min

    def getMaxVoltage(self, signal, start=0, end=None):
        signal = "v({})".format(signal)
        max = None
        for (timestamp, data) in self.simulationResult:
            if timestamp >= start and (end == None or timestamp <= end):
                if data[signal] > max:
                    max = data[signal]
        return max

    def getCurrent(self, signal):
        return ""

    def getMinCurrent(self, signal, start=0, end=None):
        return ""

    def getMaxCurrent(self, signal, start=0, end=None):
        return ""

    def getSignal(self, signal):
        if len(self.simulationResult) > 0:
            (timestamp, signals) = self.simulationResult[-1]
            if signal in signals.keys():
                return signals[signal]
        return None

