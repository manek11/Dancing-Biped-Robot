import time
import board
import displayio
import terminalio
import label
from adafruit_st7735r import ST7735R

# Release any resources currently in use for the displays
displayio.release_displays()

# board & pin setup
spi = board.SPI()
tft_cs = board.D5
tft_dc = board.D9

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7)
display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)

# Draw a label
text = "It's Party Time!"
text_area = label.Label(terminalio.FONT, text=text, color=0xfff200)
# Set the location
text_area.x = 25
text_area.y = 64
#show text
display.show(text_area)

# show for 2 seconds
for i in range(2):
    pass
    time.sleep(1)


# erase current text and reset board & pins
displayio.release_displays()
spi = board.SPI()
tft_cs = board.D5
tft_dc = board.D9
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7)
display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)

# Draw new text label 
text = "Hello, \nI am Wilson \nthe dancing robot!"
text_area = label.Label(terminalio.FONT, text=text, color=0xfff200)
# Set the location
text_area.x = 10
text_area.y = 55
# show new text label
display.show(text_area)

# show for 5 seconds
for i in range(5):
    pass
    time.sleep(1)


# erase current text 
displayio.release_displays()
spi = board.SPI()
tft_cs = board.D5
tft_dc = board.D9
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7)
display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)

# Draw new text label
text = "Press a key: \n 1: shuffle \n 2: kick \n 3: moonwalk \n 4: wobble \n 5: squat \n 6: spin"
text_area = label.Label(terminalio.FONT, text=text, color=0xfff200)
# Set the location
text_area.x = 10
text_area.y = 60
#show new text
display.show(text_area)

# show this text for the rest of time 
while True:
    pass
    #TODO rest of servo, dance, buzzer, etc code goes in this while loop ... 
