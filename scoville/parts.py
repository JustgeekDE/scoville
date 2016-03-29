class GenericVoltageSource:
  def __init__(self, name, netHigh, netGND, voltage):
    self.name = name
    self.netHigh = netHigh
    self.netGND = netGND
    self.voltage = voltage
    self.resistance = 0

  def getSpiceDefinition(self):
    voltageSource = "V{0} {0} GND dc {1}V ac 0V\n".format(self.netHigh, self.voltage)
    resistor = "R{0} {1} GND {2}".format(self.name, self.netGND, self.resistance)
    return voltageSource + resistor


