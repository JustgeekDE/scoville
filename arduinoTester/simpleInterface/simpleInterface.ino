#define ANALOG_READ_INTERVALL 10

#define COMMAND_BUFFER_LENGTH 64
char commandBuffer[COMMAND_BUFFER_LENGTH];
uint8_t commandBufferIndex = 0;

bool outputAnalogValues = 0;

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
}

bool setPinState(uint8_t pin, char state) {
  switch(state) {
    case 'l':
      pinMode(pin, OUTPUT);
      digitalWrite(pin, LOW);
      return 1;

    case 'h':
      pinMode(pin, OUTPUT);
      digitalWrite(pin, HIGH);
      return 1;

    case 'z':
      pinMode(pin, INPUT);
      digitalWrite(pin, LOW);
      return 1;
    
    case 'p':
      pinMode(pin, INPUT);
      digitalWrite(pin, HIGH);
      return 1;

    default:
      return 0;
  }
}

bool handleSetCommand(char* command) {
  // should have the form x=y 
  if(strlen(command) < 3) {
    return 0;
  }

  uint8_t pin = command[0] - '0';
  char state = command[2];
  return setPinState(pin, state);
}

bool handleCommands(char* command) {
  size_t commandLength = strlen(command);
  if (commandLength < 1) {
    return 0;
  }
  
  switch(command[0]) {
    case 's':
      return handleSetCommand(&command[1]);
      
    case 'a':
      outputAnalogValues = command[1] - '0';
      return 1;
      
    default:
      return 0;
  }
  return 0;
}

void readInput() {
  while (Serial.available() > 0) {
    char incomming = Serial.read();
    if (incomming == ';') {
      commandBuffer[commandBufferIndex] = 0;
      commandBufferIndex = 0;
      if (!handleCommands(commandBuffer)) {
        Serial.print("Unknown command:\n\t");
        Serial.println(commandBuffer);
      }
    } else {
      commandBuffer[commandBufferIndex] = incomming;
      commandBufferIndex = (commandBufferIndex + 1) % COMMAND_BUFFER_LENGTH;
    }
  }
}

void analogValues() {
  static unsigned long lastRead = 0;
  unsigned long now = millis();
  if (outputAnalogValues && (lastRead + ANALOG_READ_INTERVALL < now)) {
    lastRead = now;
    Serial.print(analogRead(A0));
    Serial.print(";");
    Serial.print(analogRead(A1));
    Serial.print(";");
    Serial.print(analogRead(A2));
    Serial.print(";");
    Serial.print(analogRead(A4));
    Serial.print("\r\n");
  }
}

void loop() {
  readInput();
  analogValues();
}


