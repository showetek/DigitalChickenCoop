import sqlite3

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
    

    sqliteCon = sqlite3.connect('Datebase_python.db')
    cursor = sqliteCon.cursor()
    query_select_all = "SELECT * FROM Protokoll WHERE id = {i}".format(i = id)
    cursor.execute(query_select_all)
    tablerows = cursor.fetchone() 
    #Hier fetchone um eine Zeile, wo dies gillt das auszulesen
    
    print("Number of all rows: ", len(tablerows))
    print("All rows in the table mytable: ")

    current_ds = dataSet(tablerows[0] , tablerows[1] , tablerows[2] , tablerows[3])

    print("id: ", tablerows[0])
    print("Zeit: ", tablerows[1]) 
    print("Datum: ", tablerows[2])
    print("Status: ", tablerows[3])
    print("------\n")
        
    cursor.close()
    sqliteCon.close()

    return current_ds

def insert():

    sqliteCon = sqlite3.connect('Datebase_python.db')
    cursor = sqliteCon.cursor()

    query_insert_into = """INSERT INTO Protokoll (id, Zeit, Datum, Status) Values ({id},{z},{d},{s})""".format(id = 2,z= '1', d= '1',s= 1)
                
    count = cursor.execute(query_insert_into)
    sqliteCon.commit()
    cursor.close