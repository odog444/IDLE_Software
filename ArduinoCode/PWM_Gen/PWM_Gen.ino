// Lin actuator pins
const int pwmPin = 9;
const int pin1 = 8;
const int pin2 = 7;
const int pin3 = 6;

// Drum motor pin
const int drumPWMpin = 3;

int counter = 0;

String message;

float msDelay = 1500;

void setup() {
  Serial.begin(115200);
  while(!Serial){}

  // Lin act.
  pinMode(pwmPin, OUTPUT);
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);

  // Drum motor
  pinMode(drumPWMpin, OUTPUT);
}

void loop() {
  if(Serial.available() > 0){
    message = Serial.readStringUntil('\n');
    Serial.println(String(message.c_str()));
  }else{
    message = "No command sent";
  }

  // Init variables for drum
  int messageFloat = message.toInt();

  if (message == "UP"){
    setIn();
    Serial.println("UP commanded");
  } else if (message == "DOWN"){
    setOut();
    Serial.println("DOWN commanded");
  }else if(messageFloat != 0){
    if(message == "0"){
      msDelay = 500;
    }else{
      msDelay = (messageFloat * 2) + 500;
    }
  }else{
    //Serial.println("Undefined command received: " + message);
    digitalWrite(pwmPin, LOW);
  }
  delay(10);

  // Drive drum motor
  digitalWrite(3, HIGH);
  /*
  * 500 - 1490 useconds will turn motor in reverse
  * 1510 - 2500 useconds will turn motor forward
  */
  delayMicroseconds(msDelay);
  digitalWrite(3, LOW);
  Serial.println(msDelay);
}
void setIn(){
    // Set logic to move the LA Out
  digitalWrite(pwmPin, HIGH);
  digitalWrite(pin1, LOW);
  digitalWrite(pin2, HIGH);
  digitalWrite(pin3, HIGH);
}
void setOut(){
  // Set logic to move LA In
  digitalWrite(pwmPin, HIGH);
  digitalWrite(pin1, HIGH);
  digitalWrite(pin2, LOW);
  digitalWrite(pin3, HIGH);
}
