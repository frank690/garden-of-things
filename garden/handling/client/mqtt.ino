// include needed libraries
#include <WiFi.h>
#include <PubSubClient.h>  // Click here to get the library: https://github.com/knolleary/pubsubclient
#include <Wire.h>

// define class instances
WiFiClient espClient;
PubSubClient client(espClient);

// define variables to use
long last_message = 0;
char message[50];
int value = 0;


void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}
