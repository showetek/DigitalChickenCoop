from datetime import datetime
import os, pytz

class logger():

    def __init__(self, log_file) -> None:
        self._log_file = open(os.path.join(os.getcwd(), log_file),'a')
    
    def _write(self, loglevel ,msg) -> None:
        if self._log_file.writable():
            self._log_file.write(f'{datetime.now(pytz.timezone("Europe/Berlin")).strftime("%Z %Y-%m-%d %H:%M:%S")} | {loglevel} | {msg}\n')
        else:
            raise os.error

    def debug(self, msg):
        self._write('DEBUG',msg)

    def info(self, msg):
        self._write('INFO',msg)
    
    def warn(self, msg):
        self._write('WARN',msg)
    
    def error(self, msg):
        self._write('ERROR',msg)

    def critical(self, msg):
        self._write('CRITICAL',msg)
        print(msg)

""" TestProgramm """

log = logger("test.log")

log.debug('This is an debug message')
log.info('This is an info message')
log.warn('This is an warn message')
log.error('This is an error message')
log.critical('This is an critical message')

""" Colors """

csi = '\x1B['
red = csi + '31;1m'
yellow = csi + '33;1m'
end = csi + '0m'

print('Here is a %sred%s word and one in %syellow!%s' % (red, end, yellow, end))

log.critical('This is an %scritical%s message' % (red,end))