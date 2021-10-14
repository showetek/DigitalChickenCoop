#include <SPI.h> // SPI-Bibiothek hinzufügen

#include <MFRC522.h> // RFID-Bibiothek hinzufügen

#define SS_PIN 10 // SDA

#define RST_PIN 9 

MFRC522 mfrc522[2];

void setup() {
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  Serial.begin(9600); 

  SPI.begin(); 

  mfrc522[0].PCD_Init(10, RST_PIN);
  mfrc522[1].PCD_Init(2, RST_PIN); 

}

void loop() {
  if (mfrc522[0].PICC_IsNewCardPresent()) {
    long code=0;      // variable "code" erstellen, um später den Code des Senders abzuspeichern
    
    for (byte i = 0; i < mfrc522[0].uid.size; i++){
      code=((code+mfrc522[0].uid.uidByte[i])*10);      // Der empfangene Code wird ausgelesen und in eine hexadezimale Zahl umgewandelt. In Variable code abgespeichert.
    }
    Serial.print(code);      //Der Code des RFID-Senders wird im seriellen Monitor angezeigt.
    digitalWrite(5, HIGH);
    delay(1000);
    digitalWrite(5, LOW);
    }



    if (mfrc522[1].PICC_IsNewCardPresent()) {
    long code=0;      // variable "code" erstellen, um später den Code des Senders abzuspeichern
    
    for (byte i = 0; i < mfrc522[1].uid.size; i++){
      code=((code+mfrc522[1].uid.uidByte[i])*10);      // Der empfangene Code wird ausgelesen und in eine hexadezimale Zahl umgewandelt. In Variable code abgespeichert.
    }
    Serial.print(code);      //Der Code des RFID-Senders wird im seriellen Monitor angezeigt.
    digitalWrite(6, HIGH);
    delay(1000);
    digitalWrite(6, LOW);
    }
 

}
  
