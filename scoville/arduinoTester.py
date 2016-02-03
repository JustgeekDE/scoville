import serial, time

class ArduinoInterface:
  def __init__(self, serialPort, baudrate=115200):
    self.serialInterface = serial.Serial(port=serialPort, baudrate=baudrate, timeout=1)

    self.signalMap = {}
    self.outputMap = {}
    self.voltageMap = {}
    self.data = {}


  def setSignal(self, signal, outputPin):
    self.signalMap[signal.name] = outputPin
    self.outputMap[outputPin] = signal.value

  def inspectVoltage(self, voltageName, inputPin):
    self.voltageMap[inputPin] = voltageName
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
    self.serialInterface.close()

  def flushInput(self):
    self._command('a0;')
    endTime = time.time() + 0.1
    while time.time() < endTime:
     self.serialInterface.read()

  def _command(self, command):
    self.serialInterface.flushInput()
    self.serialInterface.flushOutput()
    self.serialInterface.write("foo;")
    self.serialInterface.write(command)
    self.serialInterface.write(command)
    self.serialInterface.flush()
    pass

  def _setOutputs(self):
    for pin in self.outputMap.keys():
      value = 'l'
      if self.outputMap[pin] > 2.5:
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
