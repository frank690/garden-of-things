#include "settings.h"
#include "mqtt.h"
#include "sensors.h"

// setup and main function
void setup() {
  Serial.begin(baud_rate);
  delay(50);
  
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);

  dht.begin();
}

void loop() {
  delay(1000);
  
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  
  client.publish("sffrenzy", (char*) get_sensor_values().c_str());
}
