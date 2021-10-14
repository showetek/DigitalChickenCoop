//Lib
#include <SoftwareSerial.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266mDNS.h>
#include <ESP8266HTTPClient.h>

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

//X509List cert(cert_DigiCert_High_Assurance_EV_Root_CA);

void post(String sensor, String chick_id, String arduino_id){
  WiFiClient client;
  Serial.print("Connecting to ");
  Serial.println(host);

  //Serial.printf("Using certificate: %s\n", cert_DigiCert_High_Assurance_EV_Root_CA);
  //client.setTrustAnchors(&cert);

  if (!client.connect(host,port)) {
    Serial.println("Connection failed");
    return;
  }
  // http://192.168.3.1:5000/sensor/123456/A
  String url = "/sensor/123456/A";
  Serial.print("Requesting URL: ");
  Serial.println(url);

  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" +
               "Connection: close\r\n\r\n");

  Serial.println("Request sent");
  while (client.connected()) {
    String line = client.readStringUntil('\n');
    if (line == "\r") {
      Serial.println("Headers received");
      break;
    }
  }
  String line = client.readStringUntil('\n');
  if (line.startsWith("{\"state\":\"success\"")) {
    Serial.println("esp8266/Arduino CI successful!");
  } else {
    Serial.println("esp8266/Arduino CI has failed");
  }
  Serial.println("Reply was:");
  Serial.println("==========");
  Serial.println(line);
  Serial.println("==========");
  Serial.println("Closing connection");
}

void connect_to_wifi() {
  WiFi.begin(ssid, password); //WIFI Verbinden
  Serial.println("");

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
  Serial.begin(9600);         //Serielle Verbindung mit Monitor
  connect_to_wifi();
  String sensor = "sensor";
  String chick_id = "123456";
  String arduino_id = "A";
  post(sensor, chick_id, arduino_id);
}

//Mainloop des Hauptprogrammes
void loop() {}
