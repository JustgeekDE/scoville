import time

class SignalError(Exception):
    pass

class ArduinoInterface:
  def __init__(self, serialInterface):
    self.serialInterface = serialInterface

    self.signalMap = {}
    self.outputMap = {}
    self.voltageMap = {}
    self.data = {}

  def mapOutput(self, signalName, outputPin):
    self.signalMap[signalName] = outputPin

  def mapInput(self, signalName, inputPin):
    self.voltageMap[inputPin] = signalName

  def setSignal(self, signal):
    if signal.name not in self.signalMap.keys():
      raise SignalError('Signal ' + str(signal.name) + ' is not assigned to any output')
    self.outputMap[signal.name] = signal.value

  def inspectVoltage(self, voltageName):
    if voltageName not in self.voltageMap.values():
      raise SignalError('Signal ' + str(voltageName) + ' is not assigned to any output')
    self.data[voltageName] = []

  def getVoltage(self, voltageName):
    value = float(self.data[voltageName][-1])
    value = 5.0 * (value / 1023.0)
    return value

  def run(self, duration = 500):
    self._setOutputs()
    self.flushInput()
    self._command('a1;')

    inputCounter = 0
    now = time.time()
    endTime = now + (duration / 1000.0)
    while time.time() < endTime:
      line = self.serialInterface.readline().strip()
      if len(line) > 0:
        if self._proccessInput(line):
          inputCounter += 1
    self.serialInterface.write("a0;")

  def flushInput(self):
    self._command('a0;')
    endTime = time.time() + 0.1
    while time.time() < endTime:
     self.serialInterface.read()

  def _command(self, command):
    self.serialInterface.flushInput()
    self.serialInterface.flushOutput()
    self.serialInterface.write(command)
    self.serialInterface.flush()
    pass

  def _setOutputs(self):
    for signalName in self.outputMap.keys():
      if signalName not in self.signalMap.keys():
        raise SignalError('Signal ' + str(signalName) + ' is not assigned to any output')

      pin = self.signalMap[signalName]
      value = 'l'
      if self.outputMap[signalName] > 2.5:
        value = 'h'

      command = "s{pin}={value};".format(pin = pin, value = value)
      self._command(command)

  def _proccessInput(self, inputLine):
    values = inputLine.split(';')
    if len(values) < 2:
      return False

    for i in range(0, len(values)):
      if i < len(self.voltageMap):
        voltageName = self.voltageMap[i]
        self.data[voltageName].append(values[i])
    return True
