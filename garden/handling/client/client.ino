// include needed libraries
#include "DHTesp.h" // Click here to get the library: http://librarymanager/All#DHTesp

// define pin usage
const int LDR_PIN = A0;
const int SOIL_MOISTURE_PIN = A1;
const int DHT_PIN = A2;

// define serial connection variables
const int baudrate = 9600;

// define soil moisture variables
const int dry_soil_value = 620;
const int wet_soil_value = 310;
int soil_moisture_value = 0;

// define humidity instance
int humidity = 0;
int temperature = 0;
DHTesp dht;


// setup and main function
void setup() {
  Serial.begin(baudrate);
  dht.setup(DHT_PIN, DHTesp::DHT22);
}


void loop() {
  delay(100);
  float humidity = dht.getHumidity();
  float temperature = dht.getTemperature();
}


// additional functions
int get_light_intensity() {
  return analogRead(LDR_PIN);
}


float get_soil_moistness() {
  soil_moisture_value = analogRead(SOIL_MOISTURE_PIN);
  return map(soil_moisture_value, dry_soil_value, wet_soil_value, 0, 100);
}
