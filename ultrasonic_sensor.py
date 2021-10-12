import time
import board
from analogio import AnalogIn
import adafruit_hcsr04
 
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D3)
threshold = 0.3

while True:
    try:
        print((sonar.distance,))
        if sonar.distance < threshold:
            print("Detected")
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)