from init_st7789 import tft
import timeutil
import fonts.vector.gothita as gothita
import utime
import st7789

X = 240
Y = 240


def zfill(str, n):
    return '0'*(n-len(str))+str


def drawdatetime(datetime):
    dateString = zfill(str(datetime[1]), 2)+' - '+zfill(str(datetime[2]), 2)
    timeString = zfill(str(datetime[4]), 2)+' : '+zfill(str(datetime[5]), 2)
    tft.fill_rect(0, 0, X, Y, st7789.BLACK)
    tft.draw(gothita, dateString, 43, 60, st7789.WHITE, 1.1)
    tft.draw(gothita, timeString, 15, 130, st7789.WHITE, 1.7)


def loop():
    drawdatetime(timeutil.getdatetime())
    while True:
        datetime = timeutil.getdatetime()
        if datetime[6] == 0:
            drawdatetime(datetime)
        utime.sleep(1)
