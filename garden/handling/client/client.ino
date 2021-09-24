// define serial connection variables
const int baud_rate = 9600;
const int nap_time = 10000;  // 10s naps in between broadcasting values
const char* name = "NAME_OF_YOUR_ESP32";

// setup and main function
void setup() {
  Serial.begin(baud_rate);
  dht.setup(DHT_PIN, DHTesp::DHT22);

  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  long now = millis();
  if (now - lastMsg > nap_time) {
    lastMsg = now;
    data = get_sensor_values();

    Serial.print("Publishing: ");
    Serial.println(data);
    client.publish(esp32_name, data);
  }
}