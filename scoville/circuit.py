import operator
from scoville.spiceSimulator import SpiceSimulator


class Circuit:
  def __init__(self, circuitData):
    self.originalData = circuitData

    self.usedParts = []
    self.inspectedElements = []
    self.mocks = {}
    self.simulator = SpiceSimulator()
    self.simulationResult = None

  @staticmethod
  def fromFile(fileName):
    with open(fileName, 'r', encoding='utf-8') as circuitFile:
      return Circuit(circuitFile.read())
    return None

  def convertToList(self, input):
    if not (isinstance(input, list)):
      input = [input]
    return input

  def use(self, parts):
    parts = self.convertToList(parts)
    self.usedParts.extend(parts)

  def inspectVoltage(self, signal):
    self.inspectedElements.append("v(" + signal + ")")

  def inspectCurrent(self, signal):
    self.inspectedElements.append("i(" + signal + ")")

  def run(self, duration=5, steps=0.01):
    circuit = self.getSimulationCircuit()
    self.simulationResult = self.simulator.run(circuit, self.inspectedElements, duration, steps)

  def getSimulationCircuit(self):
    strippedData = self.removeParts(self.originalData, self.usedParts)
    mocks = self.getMocks()
    circuit = mocks + strippedData
    return circuit

  def removeParts(self, circuit, partsToKeep):
    if len(partsToKeep) < 1:
      return circuit
    result = ""
    for line in circuit.splitlines():
      if self.keepLine(line, partsToKeep):
        result += "\n" + line
    return result

  def keepLine(self, line, partsToKeep):
    line = line.strip()
    if line.startswith('.') or line.startswith('*'):
      return True
    if any(part + " " in line for part in partsToKeep):
      return True
    return False

  def getMocks(self):
    result = ""
    for signal in self.mocks.values():
      result += signal.getSpiceDefinition()
    return result

  def setSignal(self, signal):
    self.mocks[signal.name] = signal

  def getVoltage(self, signal):
    signal = "v({})".format(signal)
    return self.getSignal(signal)

  def getMinVoltage(self, signal, start=0, end=None):
    signal = "v({})".format(signal)
    return self.getSignalForRange(signal, start, end, operator.lt)

  def getMaxVoltage(self, signal, start=0, end=None):
    signal = "v({})".format(signal)
    return self.getSignalForRange(signal, start, end, operator.gt)

  def getCurrent(self, signal):
    signal = "i({})".format(signal)
    return self.getSignal(signal)

  def getMinCurrent(self, signal, start=0, end=None):
    signal = "i({})".format(signal)
    return self.getSignalForRange(signal, start, end, operator.lt)

  def getMaxCurrent(self, signal, start=0, end=None):
    signal = "i({})".format(signal)
    return self.getSignalForRange(signal, start, end, operator.gt)

  def getSignal(self, signal):
    if len(self.simulationResult) > 0:
      (timestamp, signals) = self.simulationResult[-1]
      if signal in signals.keys():
        return abs(float(signals[signal]))
    return None

  def getSignalForRange(self, signal, start, end, compOperation):
    result = None
    for (timestamp, data) in self.simulationResult:
      if timestamp >= start and (end == None or timestamp <= end):
        if result == None or compOperation(data[signal], result):
          result = abs(float(data[signal]))
    return result
