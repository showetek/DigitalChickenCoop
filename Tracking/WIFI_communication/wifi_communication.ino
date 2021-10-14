//Lib
#include <SoftwareSerial.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266mDNS.h>
#include <ESP8266HTTPClient.h>

//Define
#ifndef STASSID
#define STASSID "MDG_Stream"
#define STAPSK  "#Buermende21"
#endif

//Const Var
const char* ssid     = STASSID;
const char* password = STAPSK;
const char* server_adresse = "http://192.168.1.27:5000";

//Var

void post(String action, String chick_id, String arduino_id){
    HTTPClient http;    //Declare object of class HTTPClient
 
    //http.begin(server_adresse + "/" + action + "/" + chick_id + "/" + arduino_id);      //Specify request destination
  /*  http.addHeader("Content-Type", "text/plain");  //Specify content-type header
 
    int httpCode = http.POST("co2_in="+ key1 + ",tmp_in=" + key2 +",");   //Send the request
    String payload = http.getString();                  //Get the response payload
 
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload
 */
    http.end();  //Close connection
}

//Setup
void setup()
{            
  Serial.begin(9600);         //Serielle Verbindung mit Monitor 
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

//Mainloop des Hauptprogrammes
void loop()
{  
  //post("Test", "Test", "Test");
}
