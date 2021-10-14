from classes.sqlConnect import sqlConnect as sC
from classes.sqlConnect import dataSet

class chicken():
    """ Hier ist Platz für Kommentare """

    def __init__(self, chickenID) -> None:
        self.chickenID = chickenID

    def checkStatus(self):
        db = sC()

        results = db.auslesen(self.chickenID)

        try:

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



    def go_out(self):
        self.location = 1

    def go_in(self):
        self.location = 0
    
    def get_location(self):
        return self.location

    @property
    def _location(self):
        return self.location