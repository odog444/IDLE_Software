void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(3, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(10, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(analogRead(A0));
  digitalWrite(3, HIGH);
  /*
   * 500 - 1490 useconds will turn motor in reverse
   * 1510 - 2500 useconds will turn motor forward
   */
  // Get microsecond delay from PWM signal
  unsigned long high_duration = pulseIn(10, HIGH);  // Measure the duration of the high pulse
  unsigned long low_duration = pulseIn(10, LOW);    // Measure the duration of the low pulse
  
  unsigned long period = high_duration + low_duration;  // Calculate the total period
  float delayuS = (float)high_duration / period * 100.0;  // Calculate the duty cycle

  delayuS = (delayuS * 20) + 500;
  delayMicroseconds(delayuS);
  digitalWrite(3, LOW);
}