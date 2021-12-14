//Lib
#include <SoftwareSerial.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
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
const char* host = "192.168.3.1";
const uint16_t port = 5000;

void post() {
  WiFiClient client;
  HTTPClient http;
  http.begin(client, "http://" + String(host) + "/api/login");
  http.addHeader("Content-Type", "text/plain");
  int httpCode = http.POST("Message from ESP8266");
  String payload = http.getString();

  Serial.println(httpCode);
  Serial.println(payload);
  http.end();
  
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

//HIer motor ansteuern
void openDoor(){
  Serial.println("The door opens now.");
}

void closeDoor(){
  Serial.println("The door closes now.");
}

//Setup
void setup()
{       
  Serial.begin(9600);
  connect_to_wifi();
  post();
}

//Mainloop des Hauptprogrammes
void loop(){}
