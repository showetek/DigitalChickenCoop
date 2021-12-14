![Logo](https://repository-images.githubusercontent.com/387586940/826129f9-3b9d-497d-8a9d-7a84d2fa6e60)

# **Projektbeschreibung**

Source code zur Digitalisierung des Hühnerstalls. Dieses Repository umfasst das komplette Software-backend des Projektes. Die Projektstruktur besteht dabei aus mehreren einzelnen IoT-Boards, welche jeweils eigene Aufgaben übernehmen, wie unter anderem ``Registrierung der RFID-Chips``, ``Ansteuerung der Tür`` und ``Futterausgabe``. 
Dabei sind diese alle zu einem zentralen Server über den Raspberry Pi verbunden. Dieser übernimmt die Kommunikation zwischen den einzelnen IoT-Boards unter Bereitstellung eines eigenen Wlan-Netzes, sowie die Bereitstellung einer Benutzerschnittstelle.

Der Programmierstil folgt dabei dem OOP (Object-oriented programming) Prinzip.

>This project is licensed under the [MIT License](https://github.com/showetek/DigitalChickenCoop/blob/main/LICENSE)

### Usefull Links:

* [Code of conduct](https://github.com/showetek/DigitalChickenCoop/blob/main/CODE_OF_CONDUCT.md)
* [Contributing](https://github.com/showetek/DigitalChickenCoop/blob/main/CONTRIBUTING.md)
* [GitHub Pages](https://showetek.github.io/DigitalChickenCoop/)

## **Aktuell entwickelt von**:

*Die Software des Projektes wird zurzeit in zwei Teams entwickelt:*

### Server

* [Torben Heine](https://github.com/showetek)
* [Paul Paysan](https://github.com/PaulPaysan)
* [Alexander Meinecke](https://github.com/alexxd2002)

### IoT

* [Gerald Roboom](https://github.com/geraldroboom)
* [Felix Knierim](https://github.com/felixknierim)
* Finn-Jerik Thieße

## **Dependencies**:

*Folgende externe Bibliotheken werden weitergehend im Code genutzt:*  

### Server

* [Flask web application framework](https://github.com/pallets/flask)
* [serial](https://pypi.org/project/serial/)
* [pytz](https://github.com/stub42/pytz)

+ Weitere Informationen finden sich [hier](https://github.com/showetek/DigitalChickenCoop/network/dependencies)

### IoT

* [Arduino core for ESP8266 WiFi chip](https://github.com/esp8266/Arduino)
* [Arduino library for MFRC522 and other RFID RC522 based modules](https://github.com/miguelbalboa/rfid)

## **Boards**:

*In unserem Projekt benutzen wir folgende Boards:*

### Server

* Raspberry Pi 3 Model B+ running ``Raspberry Pi OS (32 Bit)``

### IoT

* Arduino Uno
* LOLIN WeMos D1 R2 WiFi ESP8266

## **Installing**

**Python 3.9.0 or higher is required**

To install the server just follow these three simple steps:

1. Download this repositorie using ``git clone https://github.com/showetek/DigitalChickenCoop.git``

2. Install the required libraries using:

```sh
# Linux
python3 -m pip install -U -r requirements.txt
```

3. Run the script using:

```sh
# Linux
python3 main.py
```

Note: Dies ist nur die Installation der Serversoftware, zusätzlich muss der Raspberry Pi für das Wlan-Netz konfiguriert sein und die einzelnen Programme der IoT-Boards müssen entsprechend installiert sein.

--tags arduino; automation; raspberry-pi-3; chicken-coop;
