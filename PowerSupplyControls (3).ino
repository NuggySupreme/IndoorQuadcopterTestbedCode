#include <Wire.h>
// each power supply is addressed from 0-3, using 7 bits. uses last 3 bits to address
byte powerSupplyAddresses[] = {
  B1010000,
  B1010001,
  B1010010,
  B1010011
};

// OFF and ON constants for power supply. 
// Bit 7 must be 1 for I2C mode. Bit 0 is On/Off
byte OFF = B10000000;
byte ON = B10000001;
// Register address for power supply
byte Power_Register = 0x7C; // Power Control Register

// runs on init startup
void setup() {
  Wire.begin(); // Initiate the Wire library
  Serial.begin(9600);
  delay(100);
  // Startup sequence: turns each bank on one at a time, then off.
  for (int i = 0; i < 4; i++) {
    turnOff(powerSupplyAddresses[i]);
    delay(1000);
  }

  /*
  byte high, low, out;

   
  //out = readByte(powerSupplyAddresses[0], Power_Register);
  //Serial.print("Control Register:");
  //Serial.println(out, BIN);

  //Set to output 12V (0x04B0) - 6V is 0x0258
  sendByte(powerSupplyAddresses[2], 0x71, 0x02);
  sendByte(powerSupplyAddresses[2], 0x70, 0x58);

  //Set to max current of 35 Amps (0x0DAC)
  sendByte(powerSupplyAddresses[2], 0x73, 0x0D);
  sendByte(powerSupplyAddresses[2], 0x72, 0xAC);

  //Tell changes to take effect
  sendByte(powerSupplyAddresses[2], 0x7C, B10000101);

  turnOn(powerSupplyAddresses[2]);
  */

  /*
  high = readByte(powerSupplyAddresses[0], 0x71);
  low = readByte(powerSupplyAddresses[0], 0x70);
  Serial.print("Voltage Set to:");
  Serial.print(high, HEX);
  Serial.println(low, HEX);

  high = readByte(powerSupplyAddresses[0], 0x73);
  low = readByte(powerSupplyAddresses[0], 0x72);
  Serial.print("Current Set to:");
  Serial.print(high, HEX);
  Serial.println(low, HEX);

  //Bit 3 will be 1 if there was an error
  out = readByte(powerSupplyAddresses[0], 0x7C);
  Serial.print("Control Register After Command:");
  Serial.println(out, BIN);

  */
  /*delay(1000);
  //outputs the current values
  high = readByte(powerSupplyAddresses[0], 0x61);
  low = readByte(powerSupplyAddresses[0], 0x60);
  Serial.print("Voltage Output:");
  Serial.print(high, HEX);
  Serial.println(low, HEX);

  high = readByte(powerSupplyAddresses[0], 0x63);
  low = readByte(powerSupplyAddresses[0], 0x62);
  Serial.print("Current Output:");
  Serial.print(high, HEX);
  Serial.println(low, HEX);*/

  
  //Sets each bank at different voltage
  //[0] = 4V
  setVoltage(powerSupplyAddresses[0], 0x01, 0x90);
  setCurrent(powerSupplyAddresses[0], 0x0D, 0xAC);
  applyChanges(powerSupplyAddresses[0]);

  //[1] = 6V
  setVoltage(powerSupplyAddresses[1], 0x02, 0x58);
  setCurrent(powerSupplyAddresses[1], 0x0D, 0xAC);
  applyChanges(powerSupplyAddresses[1]);

  //[2] = 8V
  setVoltage(powerSupplyAddresses[2], 0x03, 0x20);
  setCurrent(powerSupplyAddresses[2], 0x0D, 0xAC);
  applyChanges(powerSupplyAddresses[2]);

  //[3] = 12V
  setVoltage(powerSupplyAddresses[3], 0x04, 0xB0);
  setCurrent(powerSupplyAddresses[3], 0x0D, 0xAC);
  applyChanges(powerSupplyAddresses[3]);


  for (int i = 0; i < 4; i++) {
    turnOn(powerSupplyAddresses[i]);
    //Serial.print(readByte(powerSupplyAddresses[i], 0x7C), BIN);
    delay(1000);
  }

  
}

// runs continuously after setup
void loop() {

  for (int i = 0; i < 4; i++) {
    Serial.print("Module ");
    Serial.print(i);
    Serial.print(" V:");
    Serial.print(readByte(powerSupplyAddresses[i], 0x61), HEX);
    Serial.print(" ");
    Serial.print(readByte(powerSupplyAddresses[i], 0x60), HEX);
    Serial.print("     I:");
    Serial.print(readByte(powerSupplyAddresses[i], 0x63), HEX);
    Serial.print(" ");
    Serial.println(readByte(powerSupplyAddresses[i], 0x62), HEX);
  }
  delay(100);
  /*Serial.println("Which bank would you like to target? Please enter 0, 1, 2, 3.");
  while(!Serial.available()) {
    
  }
  int bank = Serial.parseInt();
  Serial.read();

  Serial.println("Would you like to turn this bank on or off? Please enter 0 for on and 1 for off");
  while(!Serial.available()) {
    
  }
   bool on = Serial.parseInt() == 0;
   Serial.read();
   if(on) {
      turnOn(powerSupplyAddresses[bank]);
   } else {
      turnOff(powerSupplyAddresses[bank]);
   }*/


   
}

// turns off power supply at given address
void turnOff(byte powerSupply) {
  Wire.beginTransmission(powerSupply);
  Wire.write(Power_Register);
  Wire.write(OFF);
  Wire.endTransmission();
}

// turns on power supply at given address
void turnOn(byte powerSupply) {
  Wire.beginTransmission(powerSupply);
  Wire.write(Power_Register);
  Wire.write(ON);
  Wire.endTransmission();
}

void sendByte(byte powerSupply, byte reg, byte data) {
  Wire.beginTransmission(powerSupply);
  Wire.write(reg);
  Wire.write(data);
  Wire.endTransmission();
}

// Reads a byte located at Register reg
byte readByte(byte powerSupply, byte reg) {
  Wire.beginTransmission(powerSupply);
  Wire.write(reg);
  Wire.endTransmission(false);
  Wire.requestFrom(powerSupply, 1);
  byte out = Wire.read();
  Wire.endTransmission(); 
  return out;
}



//Theres a better way to do these but Im tired
void setVoltage(byte powerSupply, byte voltageH, byte voltageL){ //see documentation to see how to determine values
  sendByte(powerSupply, 0x71, voltageH);
  sendByte(powerSupply, 0x70, voltageL);
}

void setCurrent(byte powerSupply, byte currentH, byte currentL){ //see documentation to see how to determine values
  sendByte(powerSupply, 0x73, currentH);
  sendByte(powerSupply, 0x72, currentL);
}

bool applyChanges(byte powerSupply){
  byte regVal = readByte(powerSupply, 0x7C);
  regVal = regVal | B00000100;

  sendByte(powerSupply, 0x7C, regVal);

  regVal = (readByte(powerSupply, 0x7C) & B00001000)>>3;

  bool good = true;
  if(regVal)
    good = false;

  return good;
}

