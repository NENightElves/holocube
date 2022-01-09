import ntptime
import utime
from machine import RTC

ntptime.settime()


def getdatetime(utc_shift):
    return utime.localtime(utime.mktime(utime.localtime())+utc_shift*3600)
