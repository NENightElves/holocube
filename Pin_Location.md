# Pin Location

|st7789|esp32|
|--|--|
|GND|GND|
|VCC|3V3|
|SCL|D18|
|SDA|D23|
|RES|D22|
|DC|D21|
|CS|D5|
|BLC|D4|

# Python Code
```
from machine import Pin, SPI
import st7789

spi = SPI(2, baudrate=30000000, polarity=1, phase=1, sck=Pin(18), mosi=Pin(23))
tft = st7789.ST7789(spi, 240, 240,
                    reset=Pin(22, Pin.OUT),
                    cs=Pin(5, Pin.OUT),
                    dc=Pin(21, Pin.OUT),
                    backlight=Pin(4, Pin.OUT),
                    rotation=0)
tft.init()
```
