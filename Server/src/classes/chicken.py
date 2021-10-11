class chicken():
    """ Hier ist Platz für Kommentare """

    def __init__(self, location) -> None:
        self.location = location

    def go_out(self):
        self.location = 1

    def go_in(self):
        self.location = 0
    
    def get_location(self):
        return self.location

    @property
    def _location(self):
        return self.location