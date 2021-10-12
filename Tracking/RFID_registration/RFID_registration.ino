#include <SPI.h> // SPI-Bibiothek hinzufügen

#include <MFRC522.h> // RFID-Bibiothek hinzufügen

#define SS_PIN 10 // SDA an Pin 10 (bei MEGA anders)

#define RST_PIN 9 // RST an Pin 9 (bei MEGA anders)

MFRC522 mfrc522(SS_PIN, RST_PIN); // RFID-Empfänger benennen



void setup() {
  pinMode(7, OUTPUT);
  Serial.begin(9600); // Serielle Verbindung starten (Monitor)

  SPI.begin(); // SPI-Verbindung aufbauen

  mfrc522.PCD_Init(); // Initialisierung des RFID-Empfängers

}

void loop() {
  if (mfrc522.PICC_IsNewCardPresent()) // Wenn eine Karte in Reichweite ist...

  {

    digitalWrite(7, HIGH);
    delay(1000);
    digitalWrite(7, LOW);

  }
}
