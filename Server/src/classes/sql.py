import sqlite3
from datetime import datetime


#from src.classes.dataset import dataSet
class dataSet:
    def __init__(self, chickenID, date, time, status):
        self.date = date
        self.time = time
        self.chickenID = chickenID
        self.status = status


    def uploadDataSet(self):
        #hier kommt die datenbank hin
        print()

    def checkStatus(self):
        #hier muss die db abgerufen werden
        print()



        

  
def auslesen(id):
    
#Erster Teil nach Datum sotieren
    sqliteCon = sqlite3.connect('Datebase_python.db')
    cursor = sqliteCon.cursor()
    query_select_all = "SELECT * FROM Protokoll WHERE id = {i} ORDER BY Datum DESC".format(i = id)
    cursor.execute(query_select_all)
    tablerows = cursor.fetchone() 
    #Hier fetchone um die neuste Zeile, wo dies gillt das auszulesen
    
    print("Number of all rows: ", len(tablerows))
    print("All rows in the table mytable: ")
      
    print("Datum: ", tablerows[2])
    datum = tablerows[2]
    cursor.close()
    sqliteCon.close()

#Zweiter Teil zum Sortieren nach Datum
    sqliteCon = sqlite3.connect('Datebase_python.db')
    cursor = sqliteCon.cursor()
    query_select_all = "SELECT * FROM Protokoll WHERE id = {i} AND Datum = '{d}' ORDER BY Zeit DESC".format(i = id, d= datum)
    cursor.execute(query_select_all)
    tablerows = cursor.fetchall() 
   #Hier fetchall um alle Zeilen, wo dies gillt auszulesen
    
    print("Number of all rows: ", len(tablerows))
    print("All rows in the table mytable: ")

    for row in tablerows:
        current_ds = dataSet(row[0] , row[1] , row[2] , row[3])
        print("id: ", row[0])
        print("Zeit: ", row[1]) 
        print("Datum: ", row[2])
        print("Status: ", row[3])
        print("------\n")
        
    cursor.close()
    sqliteCon.close()

    return current_ds





def insert(id, status):

    now = datetime.now() #derzeitiges Datum und Uhrzeit
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H-%M") 

    sqliteCon = sqlite3.connect('Datebase_python.db')
    cursor = sqliteCon.cursor()

    query_insert_into = """INSERT INTO Protokoll (id, Zeit, Datum, Status) Values ({i},'{z}','{d}',{s})""".format(i = id,z= time, d= date,s= status)
                
    count = cursor.execute(query_insert_into)
    sqliteCon.commit()
    cursor.close




