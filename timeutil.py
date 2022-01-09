import ntptime
from machine import RTC

ntptime.settime()

def getdatetime():
    return RTC().datetime()
