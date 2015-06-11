from main.scoville.device import Device

class TestTransistor(Device):
  id = "NPN_Transistor"
  spiceModelName = "BC547B"
  spiceModelData = "NPN ()"

  def getSpiceData(self):
    base = self.getSignal("G$1", "BASE")
    collector = self.getSignal("G$1", "COLLECTOR")
    emitter = self.getSignal("G$1", "EMITTER")
    return "Q"+ self.name + " " + collector + " " + base + " " + emitter + " " + self.spiceModelName
