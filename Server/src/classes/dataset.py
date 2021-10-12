#from qlConnect.py import sqlConnect as sC
import sqlConnect

class dataSet:
    def __init__(self, chickenID, date, time, status):
        self.date = date
        self.time = time
        self.chickenID = chickenID
        self.status = status


    def uploadDataSet(self):
        newCon = sC()
        newCon.insert(self)
        print('dataSet uploaded')


    def checkStatus(self):
        #hier muss die db abgerufen werden
        print()
