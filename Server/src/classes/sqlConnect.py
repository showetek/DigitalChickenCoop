import sqlite3
import datetime


#Klasse 'dataSet' strukturiert Daten aus den Sensoranfragen als Protokolleintrag für DB
class dataSet:
    def __init__(self, chickenID, date, time, status, arduino):
        self.date = date
        self.time = time
        self.chickenID = chickenID
        self.status = status
        self.arduino = arduino


    def uploadDataSet(self):
        newCon = sqlConnect()
        newCon.insert(self)
        print('dataSet uploaded')


    def checkStatus(self):
        #hier muss die db abgerufen werden
        print()

#Klasse organisiert DB-Verbindungen, Interaktionen
class sqlConnect:
    def __init__(self):
        #liegt im Ordner src, Zeit den Sensorverlauf
        self.dbName = 'protokoll.db'

    #alle Datensätze werden aus der Protokoll-DB geladen
    def catchAllElemets(self):
        elements = list()
        sqliteCon = sqlite3.connect(self.dbName)
        cursor = sqliteCon.cursor()
        query_select_all = "SELECT id FROM Protokoll"
        cursor.execute(query_select_all)
        ids = cursor.fetchall()

        cursor.close()
        sqliteCon.close()

       #for row in tablerows:
        #  elements.append(tablerows[0])

        return ids

    #Spezielle ID wird ausgelesen
    def idAuslesen(self, id):
        results = list()

        #Erster Teil nach Datum sotieren
        sqliteCon = sqlite3.connect(self.dbName)
        cursor = sqliteCon.cursor()
        query_select_all = "SELECT * FROM Protokoll WHERE id = {i} ORDER BY Datum DESC".format(i = id)
        cursor.execute(query_select_all)
        tablerows = cursor.fetchone()
        #Hier fetchone um die neuste Zeile, wo dies gillt das auszulesen
    
        #print("Number of all rows: ", len(tablerows))
        #print("All rows in the table mytable: ")
      
        #print("Datum: ", tablerows[2])
        datum = tablerows[2]
        cursor.close()
        sqliteCon.close()

    #Zweiter Teil zum Sortieren nach Datum
        sqliteCon = sqlite3.connect(self.dbName)
        cursor = sqliteCon.cursor()
        query_select_all = "SELECT * FROM Protokoll WHERE id = {i} AND Datum = '{d}' ORDER BY Zeit DESC".format(i = id, d= datum)
        cursor.execute(query_select_all)
        tablerows = cursor.fetchall() #Hier fetchall, um alle Zeilen wo Bedingung zutrifft auszulesen



        for row in tablerows:
            current_ds = dataSet(row[0] , row[1] , row[2] , row[3], row[4])
            results.append(current_ds)
            #print("id: ", row[0])
            #print("Zeit: ", row[1])
            #print("Datum: ", row[2])
            #print("Status: ", row[3])
            #print("Arduino: ", row[4])
            #print("------\n")


        cursor.close()
        sqliteCon.close()

        return results




    #fügt neue Protokoll-datens. in DB ein
    def insert(self, newDS: dataSet):

        sqliteCon = sqlite3.connect(self.dbName)
        cursor = sqliteCon.cursor()


        query_insert_into = """INSERT INTO Protokoll (id, Zeit, Datum, Status, arduino) VALUES ({id},'{z}','{d}',{s},'{ar}')""".format(id = str(newDS.chickenID),z= newDS.time, d= newDS.date,s= str(newDS.status), ar= newDS.arduino)

        cursor.execute(query_insert_into)

        sqliteCon.commit()
        cursor.close