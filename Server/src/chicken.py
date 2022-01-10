from classes.sqlConnect import sqlConnect as sC
from classes.sqlConnect import dataSet


#Klasse verwaltet Hühner
class chicken():
    """ Hier ist Platz für Kommentare """

    def __init__(self, chickenID) -> None:
        self.chickenID = chickenID

    #Überprüft Aufenthaltsstatus eines spez. Huhns
    def checkStatus(self):
        db = sC()

        try:
            results = db.idAuslesen(self.chickenID)



            #print('Datensätze gefunden: ' + str(len(results)))

            if len(results) < 2 and len(results) != 0:
                message = str(results[0].chickenID) + ' ist am Ort ' + results[0].arduino + '.'

                #print(message)

                return message, results[0].arduino


            if results[0].arduino != results[1].arduino:
                message = str(results[0].chickenID) + ' ist zum Ort ' + results[0].arduino + ' gewechselt.'

                #print(message)

                return message, results[0].arduino
            else:
                message = str(results[0].chickenID) + ' ist am Ort ' + results[0].arduino + '.'

                #print(message)

                return message, results[0].arduino

        except:
            message = 'Angeforderte ID nicht gefunden.'

            #print(message)

            return message, 'null'


#Überprüft Status aller Hühner -> Entscheidung der Türschließung bis best. Uhrzeit
class chickens():
    def __init__(self):
        self = self

    def loadAllChicks(self) -> list():
        results: list() = sC().catchAllElemets()
        #Muss noch doppelte ids aussortieren!
        results = sorted(results)
        ids: list() = []

        for id in results:
            if id not in ids:
                ids.append(id)




        return ids

    def checkChicks(self):
        ids = self.loadAllChicks()
        inside = 0

        for id in ids:
            curChicken = chicken(id[0])

            status = curChicken.checkStatus()[1]

            if status == 'A':
                inside += 1

        return inside, len(ids)

    def chickensInside(self):
        results = self.checkChicks()

        if results[0] == results[1]:
            return True
        else:
            return False
















