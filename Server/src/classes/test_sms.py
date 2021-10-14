from sms import SIM800L
sim800l=SIM800L('/dev/serial0')

sms="Hello there"
#sim800l.send_sms(dest.no,sms)
sim800l.send_sms('+4915256187271',sms)