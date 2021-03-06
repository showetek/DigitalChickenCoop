//Lib
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266mDNS.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WebServer.h>

//Define
#ifndef STASSID
#define STASSID "Chicken-Intranet"
#define STAPSK  "1234567890"
#endif

//Const Var
const char* ssid     = STASSID;
const char* password = STAPSK;

//Webserver erstellen
ESP8266WebServer server(80);

void send_food_status(String status){
    HTTPClient http;    //Declare object of class HTTPClient
 
    http.begin("http://192.168.3.1:5000/api/food");      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header
 
    int httpCode = http.POST("{\"status\":\""+ status +"\"}");   //Send the request
    String payload = http.getString();                  //Get the response payload
 
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload
 
    http.end();  //Close connection
}

void login(String id){
    HTTPClient http;    //Declare object of class HTTPClient
 
    HTTPClient.begin(http, "192.168.1.15:5000/api/login");      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header
 
    //int httpCode = http.POST("{\"ip\":\""+ WiFi.localIP().toString() +"\",\"id\":\""+id+"\"}");   //Send the request
    int httpCode = http.POST("{\"ip\":\"12345\",\"id\":\""+id+"\"}");   //Send the request
    String payload = http.getString();                  //Get the response payload
 
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload
 
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

  
  server.on("/food/", handleForm); //Post-request verarbeiten
  
  
  server.begin();
  //als food einloggen
    login("food");
}

//Mainloop des Hauptprogrammes
void loop()
{
  server.handleClient();
}

//Post-request verarbeiten
void handleForm() {
  if (server.method() != HTTP_POST) {
    server.send(405, "text/plain", "Method Not Allowed");
  } else {
    String message = "";
    for (uint8_t i = 0; i < server.args(); i++) {
      message =  server.arg(i)+"";
    }

    if (message == "feed") {
        openFood();
        closeFood();
        send_food_status("feeded");
    }

    server.send(200, "text/plain", "OK");
  }
}
//HIer motor ansteuern
void openFood(){

}

void closeFood(){

}
