#include <Wire.h>
int counter = 0;

// Addreses of each temp sensor (3) and accelerometer
const int U1Temp = 0x48; // Temp sensor below accelerometer, middle right of board
const int U3Temp = 0x4F; // Temp sensor at top left of board
const int U4Temp = 0x4D; // Temp sensor at bottom left of board
int accelMeter = 0x1D; // Accelerometer

void tempSensorConfig(int sensorAddr){
  Wire.beginTransmission(sensorAddr);
  // Select configuration register
  Wire.write(0x01);
  // Set continuous conversion, comparator mode, 12-bit resolution
  Wire.write(0x60);
  // Stop I2C Transmission
  Wire.endTransmission();  
}

float calcTemp(int sensorAddr){
  unsigned int data[2];
  
  // Start I2C Transmission
  Wire.beginTransmission(sensorAddr);
  // Select data register
  Wire.write(0x00);
  // Stop I2C Transmission
  Wire.endTransmission();

  // Request 2 bytes of data
  Wire.requestFrom(sensorAddr, 2);

  // Read 2 bytes of data
  // cTemp msb, cTemp lsb
  if(Wire.available() == 2)
  {
    data[0] = Wire.read();
    data[1] = Wire.read();
  }

  float cTemp = (((data[0] * 256) + (data[1] & 0xF0)) / 16) * 0.0625;
  return cTemp;
}

void setup() 
{
  // Initialise I2C communication as MASTER
  Wire.begin();
  // Initialise Serial communication, set baud rate = 9600
  Serial.begin(9600);
  while(!Serial){}

  // ****** Temperature sensor configuration ****** //
  tempSensorConfig(U1Temp);
  tempSensorConfig(U3Temp);
  tempSensorConfig(U4Temp);


  // ****** ADXL367Z Config ****** //
  // If address of ADXL happens to be different than defined, use that address
  byte error, address;
  int deviceCount = 0;

  // Serial.println("Scanning...");

  for (address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    error = Wire.endTransmission();

    if (error == 0) {
      // Print address it found
      // Serial.print("Device found at address 0x");
      if (address < 16) Serial.print("0");
      // Serial.print(address, HEX);
      // Serial.println();
      deviceCount++;
      // Check that the given address isn't one of the 3 temp sensors
      if(address != U1Temp && address != U3Temp && address != U4Temp){
         accelMeter = address;
//        Serial.print("Non-Temp device found, Accel address is 0x");
//        Serial.println(address, HEX);
        // Serial.print(", and for reading, has become 0x");
        // Serial.println((address << 1) + 1, HEX);
      }
    } else if (error == 4) {
//      Serial.print("Unknown error at address 0x");
      if (address < 16) Serial.print("0");
//      Serial.println(address, HEX);
    }
  }
  
  // Configure 0x2D register, the POWER_CTL register by setting 
  int POWER_CTL;
  Wire.beginTransmission(accelMeter);
  Wire.write(0x2D); // Address for register
  Wire.requestFrom(accelMeter, 1);
//  if (Wire.available() == 1) {
//    POWER_CTL = Wire.read();
//    Serial.print("Register value read is ");
//    Serial.println(POWER_CTL, BIN);
//  }else{
//    Serial.println("Wire not available");
//    Serial.println(Wire.available());
//  }
  Wire.endTransmission();

  // Logical Rshift twice and Lshift back to clear RHS 7 bits (so basically everything except for reserved bit), then + BIN 10 or DEC 2 for measurement mode as per datasheet
  POWER_CTL = (((unsigned int)POWER_CTL >> 7) << 7) + 2; // "unsigned int" to typecast POWER_CTL, which makes the Rshift to behave as logical rather than arithmetic
//  Serial.print("Measurement Mode activated, new POWER_CTL value is ");
//  Serial.println(POWER_CTL, BIN);

  // Write new POWER_CTL value to POWER_CTL register
  Wire.beginTransmission(accelMeter);
  Wire.write(0x2D); // Address for register
  Wire.write(POWER_CTL);
  Wire.endTransmission();

  delay(300); 
}

void loop()
{
    
  // Convert temperature data
  float cTempU1 = calcTemp(U1Temp);
  float cTempU3 = calcTemp(U3Temp);
  float cTempU4 = calcTemp(U4Temp);

  int cTempU1_int = cTempU1;

  // Gather and convert Accelerometer data, must be split into 3 seperate begin/endTrans because requesting more than 1 bit off a single read will trigger high
  unsigned int accelData[3];
  // X axis
  Wire.beginTransmission(accelMeter);
  Wire.write(0x08); // x-axis
  Wire.requestFrom(accelMeter, 1);

  if(Wire.available() == 1){
    accelData[0] = Wire.read();
  }

  Wire.endTransmission();

  // Y axis
  Wire.beginTransmission(accelMeter);
  Wire.write(0x09); // y-axis
  Wire.requestFrom(accelMeter, 1);

  if(Wire.available() == 1){
    accelData[1] = Wire.read();
  }

  // Z axis
  Wire.beginTransmission(accelMeter);
  Wire.write(0x0A); // z-axis
  Wire.requestFrom(accelMeter, 1);

  if(Wire.available() == 1){
    accelData[2] = Wire.read();
  }

//  int acc_vec [] = {accelData[0], accelData[1], accelData[2]};

  Wire.endTransmission();

  Wire.endTransmission();

  // Output data to serial monitor
//  Serial.print("Temperature in Celsius for U1, U3, and U4: ");
  Serial.println("Temp:");
  Serial.print(cTempU1);
  Serial.print(", ");
  Serial.print(cTempU3);
  Serial.print(", ");
  Serial.println(cTempU4);

//  Serial.print("Acceleration data in XYZ: ");
  Serial.println("Acceleration");
  for(int i = 0; i < 3; i++){
    Serial.print(accelData[i]); // ############### Work is needed to interpret raw accel data into angles ####################
    if(i != 2){Serial.print(",");}
  }
  Serial.println();
 

// Arduino sending data to Raspberry Pi:
//// Tx should be blinking
//  if (Serial.available()>0){
////    String message = Serial.readStringUntil('\n');
////    message = message + " " + String(counter);
////    counter++;
////    Serial.println(message);
//    
//      Serial.print("Acceleration data in XYZ: ");
//      for(int i = 0; i < 3; i++){
//        Serial.print(accelData[i]); // ############### Work is needed to interpret raw accel data into angles ####################
//        if(i != 2){Serial.print(", ");}
//    }
//    Serial.println();
//    Serial.println();
//}
 delay(750);

// Bidirectional communication:
// Rx and Tx should both be blinking
//  if (Serial.available()>0){
//    String message = Serial.readStringUntil('\n');
//    message = message + " " + String(counter);
//    counter++;
//    Serial.println(message);
//  }


}
