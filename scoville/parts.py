class GenericVoltageSource:
  def __init__(self, name, netHigh, netGND, voltage):
    self.name = name
    self.netHigh = netHigh
    self.netGND = netGND
    self.voltage = voltage

  def getSpiceDefinition(self):
    voltageSource = "Vmock{0} {0} GND dc {1}V ac 0V\n".format(self.netHigh, self.value)
    resistor = "R{0} {1} GND 1".format(self.name, self.netGND)
    return voltageSource + resistor


