import sqlite3

#from Server.src.classes.db import db_connector

con = sqlite3.connect('database.db') #Hier den Namen der Datenbank eintragen

cur = con.cursor()

def tabelle_create():
    # Erstellt eine Tabelle NAMENS PROTOKOLL!!
    cur.execute('''CREATE TABLE Protokoll10
               (id, Zeit, Datum, Status)''')


def insert():
    # Eine Reihe Daten eintragen
    cur.execute("INSERT INTO Protokoll10 (id, Zeit, Datum, Status)VALUES ('1', '1115' , '2021-10-11' , '1')")

def select():
    #Text aus der Datenbank auslesen
    cur.execute("SELECT 'id' FROM Protokoll10 WHERE Status = '1'")

tabelle_create()
insert()
print(select())

#Speichert die Änderungen
con.commit()

#schließt die Verbindung nach dem Speichern
con.close()
