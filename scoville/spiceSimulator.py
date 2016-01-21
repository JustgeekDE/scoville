import os, subprocess
from tempfile import mkstemp

NS_PER_SECOND = 1000000


class SpiceSimulator:
  def run(self, circuit, signals, duration, step):
    descCircuit, circuitPath = mkstemp()
    descData, dataPath = mkstemp('.data')

    circuit = SpiceSimulator.addControl(circuit, dataPath, signals, duration, step)

    circuitFile = open(circuitPath, 'w')
    circuitFile.write("\n" + circuit)
    circuitFile.close()

    returnCode = subprocess.call('ngspice ' + circuitPath, shell=True, stdout=subprocess.PIPE)
    # assert returnCode == 0, "Execution of spice failed"

    dataFile = open(dataPath, 'r')
    data = dataFile.read()

    os.close(descCircuit)
    os.close(descData)
    os.remove(circuitPath)
    os.remove(dataPath)

    data = SpiceSimulator.parseData(data, signals)

    return data

  @staticmethod
  def addControl(circuit, outputFile, signals, duration, step):
    outputFile = outputFile[:-len('.data')]
    controlBlock = ""

    controlBlock += ".tran " + str(step) + "ns " + str(duration) + "ns\n"
    controlBlock += ".control\nset filetype=ascii\nrun\n"
    controlBlock += "wrdata " + outputFile
    for signal in signals:
      controlBlock += " " + signal
    controlBlock += "\n.endc"
    circuit = circuit.replace(".end", controlBlock + "\n.end")
    return circuit

  @staticmethod
  def parseData(dataBlob, signals):
    result = []
    for line in dataBlob.split("\n"):
      temp = {}
      data = line.split()
      if len(data) == (2 * len(signals)):
        timestamp = float(data[0]) * NS_PER_SECOND
        i = 0
        for signal in signals:
          temp[signal] = float(data[(i * 2) + 1])
          i += 1
        result.append((timestamp, temp))

    return result
