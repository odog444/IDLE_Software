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

int messageInt;

float currentSens = 0.0;

void setup() {
  Serial.begin(9600);
  while(!Serial){}

  // Lin act.
  pinMode(pwmPin, OUTPUT);
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);

  // Drum motor
  pinMode(drumPWMpin, OUTPUT);

  pinMode(A0, INPUT);
}

void loop() {
  if(Serial.available() > 0){
    message = Serial.readStringUntil('\n');
    Serial.println(String(message.c_str()));
  }else{
    message = "No command sent";
  }

  // Init variables for drum
  messageInt = message.toInt();

  if (message == "UP"){
    setOut();
    //Serial.println("UP commanded");
  } else if (message == "DOWN"){
    setIn();
    //Serial.println("DOWN commanded");
  }else if(messageInt != 0){
    if(message == "0"){
      msDelay = 500;
    }else{
      msDelay = (messageInt * 2) + 500;
    }
    
  }else if (message == "NONE"){
    digitalWrite(pwmPin, LOW);
 
  }else if (message == "Stop Mode"){
    digitalWrite(pwmPin, LOW);
  }else if (message == "Sleep Mode"){
    digitalWrite(pwmPin, LOW);
 }else{
    //Serial.println("Undefined command received: " + message);
  }
 

  // Drive drum motor
  digitalWrite(3, HIGH);
  /*
  * 500 - 1490 useconds will turn motor in reverse
  * 1510 - 2500 useconds will turn motor forward
  */
  delayMicroseconds(msDelay);
  digitalWrite(3, LOW);
  //Serial.println(msDelay);

  currentSens = ((5 * (float(analogRead(A0)) / 1023)) - 2.5) / 0.015;
  Serial.println(analogRead(A0));
  //Serial.println("Current sensor output: " + String(currentSens));
  Serial.println("Message: " + message + ", Message as Int: " + messageInt + ", msDelay: " + msDelay);
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
