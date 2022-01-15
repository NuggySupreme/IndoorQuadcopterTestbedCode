#include <Wire.h>
// each power supply is addressed from 0-3, using 7 bits. uses last 3 bits to address
byte powerSupplyAddresses[] = {
  B1010000,
  B1010001,
  B1010010,
  B1010011
};

// OFF and ON constents for power supply. 
// 8 bits, first bit for off(1) or on(0), last bit
// must be 1 to 
byte OFF = B10000001;
byte ON = B00000001;
// Register address for power supply
byte Power_Register = 0x7C; // Power Control Register

// runs on init startup
void setup() {
  Wire.begin(); // Initiate the Wire library
  Serial.begin(9600);
  delay(100);
  // Startup sequence: turns each bank on one at a time, then off.
  for (int i = 0; i < 4; i++) {
    turnOn(powerSupplyAddresses[i]);
    delay(1000);
  }
  for(int i = 0; i < 4; i++) {
    turnOff(powerSupplyAddresses[i]);
    delay(1000);
  }
}

// runs continuously after setup
void loop() {
  Serial.println("Which bank would you like to target? Please enter 0, 1, 2, 3.");
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
   }
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
