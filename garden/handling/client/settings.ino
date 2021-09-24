// --- variables you should modify to fit your use case ---

// general settings
const int nap_time = 10000;  // 10s naps in between broadcasting values

// connection settings
const char* ssid = "REPLACE_WITH_YOUR_SSID";
const char* password = "REPLACE_WITH_YOUR_PASSWORD";
const char* mqtt_server = "YOUR_MQTT_BROKER_IP_ADDRESS";
const char* esp32_name = "NAME_OF_YOUR_ESP32";

// define soil moisture variables
const int dry_soil_value = 620;  // put sensor into dry soil and get reference value
const int wet_soil_value = 310;  // put sensor into (very) wet soil and get reference value
