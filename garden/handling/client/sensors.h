// include needed libraries
#include "DHT.h"
#define DHT_TYPE DHT22  // DHT 22  (AM2302)

// define pin usage
const int LDR_PIN = A4;
const int SOIL_MOISTURE_PIN = A15;
const int DHT_PIN = A5;

// define soil moisture variables
int soil_moisture_value = 0;

// define humidity instance
int humidity = 0;
int temperature = 0;

DHT dht(DHT_PIN, DHT_TYPE);

// define some functions to read sensor values
int get_light_intensity() {
  return analogRead(LDR_PIN);
}

float get_soil_moistness() {
  soil_moisture_value = analogRead(SOIL_MOISTURE_PIN);
  return map(soil_moisture_value, dry_soil_value, wet_soil_value, 0, 100);
}

float get_humidity() {
    return dht.readHumidity();
}

float get_temperature() {
    return dht.readTemperature();
}

String append_value_to_string(String old_string, String topic, float value) {
    delay(50);
    if (old_string.length() > 0) {
        return old_string + ", " + topic + ": " + String(value, float_precision);
    }
    return topic + ": " + String(value, float_precision);
}

String get_sensor_values() {
    String values = "";
    values = append_value_to_string(values, "temperature", get_temperature());
    values = append_value_to_string(values, "humidity", get_humidity());
    values = append_value_to_string(values, "moisture", get_soil_moistness());
    values = append_value_to_string(values, "sun_intensity", get_light_intensity());
    return "{" + values + "}";
}
