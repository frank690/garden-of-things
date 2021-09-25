// general settings
const int nap_time = 10000;  // 10s naps in between broadcasting values
const int baud_rate = 9600;
const int float_precision = 3;

// connection settings
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
const char* mqtt_server = "YOUR_MQTT_SERVER_IP";
const int mqtt_port = 1883;
String esp32_name = "YOUR_ESP_NAME";

// define soil moisture variables
const int dry_soil_value = 3500;  // put sensor into dry soil and get reference value
const int wet_soil_value = 1600;  // put sensor into (very) wet soil and get reference value
