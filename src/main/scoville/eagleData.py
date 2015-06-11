class EagleBoard:
  def __init__(self):
    self.devices = {}
    self.deviceTypes = {}

  def addDeviceType(self, device):
    try:
      self.deviceTypes[device.id] = device
    except:
      pass