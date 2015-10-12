import os
from tempfile import mkstemp

class SpiceSimulator:
  @staticmethod
  def run(circuit, signals):
    descCircuit, circuitPath = mkstemp()
    descData, dataPath = mkstemp()

    circuit = SpiceSimulator.addControl(circuit, dataPath, signals)

    circuitFile = open(circuitPath, 'w')
    circuitFile.write(circuit)
    circuitFile.close()

    dataFile = open(dataPath, 'w')
    data = dataFile.read()

    os.close(descCircuit)
    os.close(descData)
    os.remove(circuitPath)
    os.remove(dataPath)

    return data

  @staticmethod
  def addControl(circuit, outputFile, signals):
    controlBlock = ".control\nset filetype=ascii\nrun"
    controlBlock += "\nwrdata "+outputFile
    for signal in signals:
      controlBlock += " "+signal
    controlBlock += "\n.endc"
    circuit = circuit.replace(".end", controlBlock+"\n.end")
    return circuit

  @staticmethod
  def parseData(dataBlob, signals):
    result = []
    for line in dataBlob.split("\n"):
      temp = {}
      data = line.split()
      timestamp = data[0]
      i = 0
      for signal in signals:
        temp[signal] = float(data[(i*2) + 1])
        i += 1
      result.append((timestamp, temp))

    return result
