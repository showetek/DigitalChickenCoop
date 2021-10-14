from classes.sqlConnect import sqlConnect as sC
from classes.sqlConnect import dataSet

class chicken():
    """ Hier ist Platz für Kommentare """

    def __init__(self, chickenID) -> None:
        self.chickenID = chickenID

    def checkStatus(self):
        db = sC()

        try:
            results = db.idAuslesen(self.chickenID)



            print('datensätze gefunden: ' + str(len(results)))

            if len(results) < 2 and len(results) != 0:
                message = str(results[0].chickenID) + ' ist am Ort ' + results[0].arduino + '.'

                print(message)

                return message, results[0].arduino


            if results[0].arduino != results[1].arduino:
                message = str(results[0].chickenID) + ' ist zum Ort ' + results[0].arduino + ' gewechselt.'

                print(message)

                return message, results[0].arduino
            else:
                message = str(results[0].chickenID) + ' ist am Ort ' + results[0].arduino + '.'

                print(message)

                return message, results[0].arduino

        except:
            message = 'Angeforderte ID nicht gefunden.'

            print(message)

            return message, 'null'



class chickens():
    def __init__(self):
        self = self

    def loadAllChicks(self):
        results = sC.catchAllElemets()
        ids = sorted(results)

        return ids

    def checkChicks(self):
        ids = self.loadAllChicks()
        inside = 0

        #for chicken in ids:

            #sC.idAuslesen()







