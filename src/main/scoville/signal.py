class GenericSignal:
  def __init__(self, name, value):
    self.name = name
    self.value = value

  def getSpiceDefinition(self):
    return "Vmock{0} {0} GND dc {1}V ac 0V\n".format(self.name, self.value)


class SignalWithResistance(GenericSignal):
  def __init__(self, name, value, resistance):
    self.name = name
    self.value = value
    self.resistance = resistance

  def getSpiceDefinition(self):
    result = "Vmock{0} {0}MockR GND dc {1}V ac 0V\n".format(self.name, self.value)
    result += "Rmock{0} {0}MockR {0} {1}\n".format(self.name, self.resistance)
    return result


class DelayedSignal(GenericSignal):
  def __init__(self, name, value, delay, startValue=0, resistance=0.0):
    self.name = name
    self.value = value
    self.delay = delay
    self.startValue = startValue
    self.resistance = resistance

  def getSpiceDefinition(self):
    result = "Vmock{0} {0}MockR GND PULSE({3}V {1}V {2}ms)\n".format(self.name, self.value, self.delay, self.startValue)
    result += "Rmock{0} {0}MockR {0} {1}\n".format(self.name, self.resistance)
    return result
