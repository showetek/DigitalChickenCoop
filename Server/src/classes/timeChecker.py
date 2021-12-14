import threading
from binhex import openrsrc
from datetime import datetime, timedelta
import multitimer


class timeChecker:
    def __init__(self):
        self = self


    def checkTime(self):
        now = datetime.now()
        startTime = now + timedelta(seconds=60)
        print()
        delay = (startTime - now).total_seconds()
        #t = threading.Timer(delay,self.test,args=None, kwargs=None)
        t = multitimer.MultiTimer(delay,self.timeChecker,args=None, kwargs=None,count=-1,runonstart=True)
        t.start()


    def test(self):
        print(datetime.now())

    def timeChecker(self):
        now = datetime.now().strftime('%H:%M')
        print(now)


        closeTime = '19:00'
        openTime = '7:00'

        if closeTime == now:
            #türbefehl schließen
            print('Tür schließen')

        if openTime == now:
            #türbefehl öffnen
            print('Tür öffnen')




