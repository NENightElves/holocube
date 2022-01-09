from machine import Pin, SPI
import st7789

spi = SPI(2, baudrate=32000000, polarity=1, phase=1, sck=Pin(18), mosi=Pin(23))
tft = st7789.ST7789(spi, 240, 240,
                    reset=Pin(22, Pin.OUT),
                    cs=Pin(5, Pin.OUT),
                    dc=Pin(21, Pin.OUT),
                    backlight=Pin(4, Pin.OUT),
                    rotation=0)
tft.init()
tft.rotation(0)
tft.madctl(0x40)
