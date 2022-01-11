//Lib
#include <SoftwareSerial.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266mDNS.h>

//Define
#ifndef STASSID
#define STASSID "Chicken-Intranet"
#define STAPSK  "1234567890"
#endif

//Const Var
const char* ssid     = STASSID;
const char* password = STAPSK;
const char* host = "192.168.1.15";
const uint16_t port = 5000;

void post(String sensor, String chick_id, String arduino_id){
  WiFiClient client;
  String line;
  Serial.println("Connecting to server: " + String(host));
  
  // Connecting with the Server
  if (!client.connect(host,port)) {
    Serial.println("Connection failed");
    return;
  }

  Serial.println("Sending: " + sensor + chick_id + arduino_id);

  // Opening URL to send data
  String url = "/" + sensor + "/" + chick_id + "/" + arduino_id;
  client.print(String("GET ") + url + " HTTP/1.1\r\nHost: " + host + "\r\nConnection: close\r\n\r\n");

  // TODO auslesen der rückgabe um zu bestätigen dass senden erfolgreich war
  Serial.println("Respons:");
  while (client.connected()){
    line = client.readStringUntil('\r');
    Serial.print(line);
  }

  client.stop();
  Serial.println("\nDisconnected");
}

void connect_to_wifi() {
  WiFi.begin(ssid, password); //WIFI Verbinden
  Serial.println("Connecting to WIFI ");

  //Auf Verbindung warten
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }
}

//Setup
void setup()
{            
  Serial.begin(9600);
  connect_to_wifi();
  String command = "sensor";          // sort of action, for sending data always sensor
  String chick_id = "123456";         // chicken_id registered by the RFID chips
  String arduino_id = "A";            // id of this arduino
  post(command, chick_id, arduino_id); // data is getting send
}

//Mainloop des Hauptprogrammes
void loop() {}
