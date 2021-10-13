from classes.sqlConnect import sqlConnect as sC

class chicken():
    """ Hier ist Platz für Kommentare """

    def __init__(self, chickenID) -> None:
        self.chickenID = chickenID

    def checkStatus(self):
        db = sC()
        results = db.auslesen(self.chickenID)
        print(str(results.count))



    def go_out(self):
        self.location = 1

    def go_in(self):
        self.location = 0
    
    def get_location(self):
        return self.location

    @property
    def _location(self):
        return self.location