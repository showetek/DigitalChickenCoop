import threading
from datetime import datetime, timedelta
import multitimer
from chicken import chickens


class timeChecker:
    def __init__(self, doorStatus):
        self = self
        self.doorStatus = doorStatus

    def checkTime(self):
        now = datetime.now()
        startTime = now + timedelta(seconds=60)
        # print()
        delay = (startTime - now).total_seconds()
        t = threading.Timer(delay, self.test, args=None, kwargs=None)
        t = multitimer.MultiTimer(delay, self.timeChecker, args=None, kwargs=None, count=-1, runonstart=True)
        t.start()

        # while True:
        #   self.timeChecker()

    def test(self):
        print(datetime.now())

    def timeChecker(self):
        now = datetime.now()
        print(now)

        closeTime = 19
        openTime = 7

        chickensInside = chickens().chickensInside()

        if int(now.strftime('%H')) >= int(closeTime) or int(now.strftime('%H')) < int(openTime):

            if chickensInside == True and self.doorStatus == False:
                self.doorStatus = True
                print('Tür schließen')

            if chickensInside == False:
                print('Achtung:     Hühner fehlen!')
                print('Erwartet: ' + str(chickens().checkChicks()[1]))
                print('Gefunden: ' + str(chickens().checkChicks()[0]))
                print('Tür konnte nicht geöffnet werden')
        else:
            if self.doorStatus == True:
                self.doorStatus = False
                print('Tür öffnen')

        if self.doorStatus == True:
            print('Türstatus: geschlossen')
        else:
            print('Türstatus: geöffnet')
