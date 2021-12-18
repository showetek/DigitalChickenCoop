from datetime import datetime
import os, pytz

class logger():

    def __init__(self, log_file, loglevel:int = 0) -> None:
        self.log_file = log_file
        self._loglevel = loglevel
    
    def _write(self, loglevel ,msg) -> None:
        self._log_file = open(os.path.join(os.getcwd(), self.log_file),'a') #open
        if self._log_file.writable():
            self._log_file.write(f'{datetime.now(pytz.timezone("Europe/Berlin")).strftime("%Z %Y-%m-%d %H:%M:%S")} | {loglevel} | {msg}\n')
            self._log_file.close()

    def set_loglevel(self, loglevel):
        self._loglevel = loglevel

    #10
    def debug(self, msg):
        if self._loglevel <= 10:
            self._write('DEBUG   ',msg)
    #20
    def info(self, msg):
        if self._loglevel <= 20:
            self._write('INFO    ',msg)
    #30 
    def warn(self, msg):
        if self._loglevel <= 30:
            self._write('WARN    ',msg)
    #40
    def error(self, msg):
        if self._loglevel <= 40:
            self._write('ERROR   ',msg)
    #50
    def critical(self, msg):
        if self._loglevel <= 50:
            self._write('CRITICAL',msg)

""" TestProgramm """

if __name__ == '__main__':
    log = logger("test.log",20)

    log.debug('This is an debug message')
    log.info('This is an info message')
    log.warn('This is an warn message')
    log.error('This is an error message')
    log.critical('This is an critical message')

""" Colors """

#csi = '\x1B['
#red = csi + '31;1m'
#yellow = csi + '33;1m'
#end = csi + '0m'

#print('Here is a %sred%s word and one in %syellow!%s' % (red, end, yellow, end))

#log.critical('This is an %scritical%s message' % (red,end))