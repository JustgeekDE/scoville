import uuid

class Device:
  id = "GenericDevice"
  spiceModelName = "generic"
  spiceModelData = ""

  def __init__(self, name):
    self.name = name
    self.signals = {}

  def connect(self, signalName, gate, pin):
    key = (gate, pin)
    self.signals[key] = signalName

  def getSignal(self, gate, pin):
    key = (gate, pin)
    if key in self.signals.keys():
      return self.signals[key]
    return "NC" + str(uuid.uuid4())

  def getSpiceData(self):
    return ""

  def getSpiceModel(self):
    return ".model " + self.spiceModelName + " " + self.spiceModelData
