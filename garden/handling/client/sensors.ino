// include needed libraries
#include "DHTesp.h" // Click here to get the library: http://librarymanager/All#DHTesp
#include <string>

// define pin usage
const int LDR_PIN = 8;
const int SOIL_MOISTURE_PIN = 14;
const int DHT_PIN = 9;

// define soil moisture variables
int soil_moisture_value = 0;

// define humidity instance
int humidity = 0;
int temperature = 0;
DHTesp dht;

// define some functions to read sensor values
int get_light_intensity() {
  return analogRead(LDR_PIN);
}

float get_soil_moistness() {
  soil_moisture_value = analogRead(SOIL_MOISTURE_PIN);
  return map(soil_moisture_value, dry_soil_value, wet_soil_value, 0, 100);
}

float get_humidity() {
    return dht.getHumidity();
}

float get_temperature() {
    return dht.getTemperature();
}

char[] append_value_to_string(char[] old_string, char[] topic, float value) {
    if (strlen(old_string) > 0) {
        return old_string + ", " + topic + ": " + to_string(value);
    }
    return topic + ": " + to_string(value);
}

string get_sensor_values() {
    string values = "";
    values = append_value_to_string(values, "temperature", get_temperature());
    values = append_value_to_string(values, "humidity", get_humidity());
    values = append_value_to_string(values, "moisture", get_soil_moistness());
    values = append_value_to_string(values, "light_intensity", get_light_intensity());
    return "{" + values + "}";
}
