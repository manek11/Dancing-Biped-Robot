#------------------------------------------------------------------------------------------------------#  
# Authors: Manek, Sanjeev, Parsa, Amir, Stella, Arnold, Rain
#
# Function: Dancing Robot
# 
# Date: 10/02/2020    
#------------------------------------------------------------------------------------------------------#    
import time
import sys
import board
import displayio
import terminalio
import label
from adafruit_st7735r import ST7735R
import digitalio
import adafruit_matrixkeypad
import pulseio
import servo
from analogio import AnalogIn
import adafruit_hcsr04

#------------------------------------------------------------------------------------------------------#
#
# songs code 
#     
#------------------------------------------------------------------------------------------------------#    
piezo = pulseio.PWMOut(board.A1 , duty_cycle=0, frequency=440, variable_frequency=True)

def USSR():

    timeout = time.time() + 30 
    while True:

        if time.time() > timeout:
            break

        for f in (196, 277, 196, 220, 247, 165, 165, 233, 196, 174, 208, 131, 131, 156, 147, 165, 185, 174, 196, 233, 123,
                262, 311, 311, 196, 330, 294, 261, 311, 247, 196, 277, 247, 220, 247, 165, 165, 233, 196, 131, 131, 277,
                247, 220, 207, 207, 207):
            piezo.frequency = f
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(0.25)  # On for 1/4 second
            piezo.duty_cycle = 0  # Off
            time.sleep(0.05)  # Pause between notes
        time.sleep(0.5) 

def mario_theme():
    
    timeout = time.time() + 30 
    while True:
        
        if time.time() > timeout:
            break

        for f in (2637, 2637, 0, 2637, 0, 2093, 2637, 0, 3136, 0, 0, 0, 1568, 0, 0, 0,
                  2093, 0, 0, 1568, 0, 0, 1319, 0, 0, 1760, 0, 1976, 0, 1865, 1760, 0,
                  1568, 2637, 3136, 3520, 0, 2794, 3136, 0, 2637, 0, 2093, 2349, 1976, 0, 0,
                  2093, 0, 0, 1568, 0, 0, 1319, 0, 0, 1760, 0, 1976, 0, 1865, 1760, 0,
                  1568, 2637, 3136, 3520, 0, 2794, 3136, 0, 2637, 0, 2093, 2349, 1976, 0, 0):
            piezo.frequency = f
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(0.25)  # On for 1/4 second
            piezo.duty_cycle = 0  # Off
            time.sleep(0.05)  # Pause between notes
        time.sleep(0.5)

def crimson():

    timeout = time.time() + 30 
    while True:
        
        if time.time() > timeout:
            break

        for f in (196, 247, 294, 370, 392, 370, 294, 247, 196, 262, 294, 392, 294):
            piezo.frequency = f
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(0.25)  # On for 1/4 second
            piezo.duty_cycle = 0  # Off
            time.sleep(0.05)  # Pause between notes
        time.sleep(0.5)

def canon():

    timeout = time.time() + 30 
    while True:
        
        if time.time() > timeout:
            break

        for f in (131, 165, 196, 262, 98, 123, 147, 196, 110, 131, 165, 220, 82, 98, 123, 165, 87, 110, 131, 175,
                  131, 165, 196, 262, 87, 110, 131, 175, 98, 123, 147, 196, 110):
            piezo.frequency = f
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(0.25)  # On for 1/4 second
            piezo.duty_cycle = 0  # Off
            time.sleep(0.05)  # Pause between notes
        time.sleep(0.5)

def tetris():

    timeout = time.time() + 30 
    while True:
        
        if time.time() > timeout:
            break
        delay = [444, 222, 222, 222, 111, 111, 222, 222, 444, 222, 222, 444, 222, 222, 444, 111, 111, 222, 444,
                 444, 444, 444, 888, 444, 222, 222, 444, 222, 222, 444, 222, 222, 444, 222, 222, 444, 111, 111,
                 222, 444, 444, 444, 444, 888, 444, 222, 222, 222, 111, 111, 222, 222, 444, 222, 222, 444, 222,
                 222, 444, 222, 222, 444, 444, 444, 444, 888, 444, 222, 222, 444, 222, 222, 444, 222, 222, 444,
                 222, 222, 444, 222, 222, 444, 444, 444, 444, 888]
        duration = [444, 222, 222, 222, 111, 111, 222, 222, 444, 222, 222, 444, 222, 222, 444, 111, 111, 222, 444,
                    444, 444, 444, 888, 444, 222, 222, 444, 222, 222, 444, 222, 222, 444, 222, 222, 444, 111, 111,
                    222, 444, 444, 444, 444, 888, 444, 222, 222, 222, 111, 111, 222, 222, 444, 222, 222, 444, 222,
                    222, 444, 222, 222, 444, 444, 444, 444, 888, 444, 222, 222, 444, 222, 222, 444, 222, 222, 444,
                    222, 222, 444, 222, 222, 444, 444, 444, 444, 888]
        freq = [659, 494, 523, 587, 659, 587, 523, 494, 440, 440, 523, 659, 587, 523, 494, 494, 494, 523, 587, 659,
                523, 494, 494, 494, 523, 587, 659, 523, 440, 440, 587, 587, 698, 880, 784, 698, 659, 659, 523, 659,
                587, 523, 494, 494, 523, 587, 659, 523, 440, 440, 659, 494, 523, 587, 659, 587, 523, 494, 440, 440,
                523, 659, 587, 523, 494, 494, 523, 587, 659, 523, 440, 440, 587, 587, 698, 880, 784, 698, 659, 659,
                523, 659, 587, 523, 587, 659, 523, 440, 440]
        for f in range(0, len(freq)):
            piezo.frequency = freq[f]
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(duration[f] / 1000)  # On for 1/4 second
            piezo.duty_cycle = 0  # Off
            time.sleep(delay[f] / 1000)  # Pause between notes
        time.sleep(0.5)

def default():

    timeout = time.time() + 30 
    while True:
        
        if time.time() > timeout:
            break

        delay = [149, 149, 149, 446, 1485, 149, 149, 149, 446, 297, 297, 149, 595, 149, 149, 149, 149, 1931]
        duration = [149, 149, 149, 446, 297, 149, 149, 149, 446, 297, 297, 149, 149, 149, 149, 149, 149, 149]
        freq = [349, 415, 466, 466, 415, 349, 415, 466, 466, 415, 349, 311, 349, 466, 415, 349, 311, 349]
        for f in range(0, len(freq)):
            piezo.frequency = freq[f]
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(duration[f] / 1000)  # On
            piezo.duty_cycle = 0  # Off
            time.sleep(delay[f] / 1000)  # Pause between notes
        time.sleep(0.5)
        

#------------------------------------------------------------------------------------------------------#
# 
# display code  
#    
#------------------------------------------------------------------------------------------------------# 
def reset():
    displayio.release_displays()
    spi = board.SPI()
    tft_cs = board.D5
    tft_dc = board.D9
    display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7)
    display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)
    global splash
    display.show(splash)
    color_bitmap = displayio.Bitmap(128, 128, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF # White
    bg_white = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_white)

def textshow(textin, bgcolor, xc, yc, timein):
    text_area = label.Label(terminalio.FONT, text=textin, color=bgcolor)
    text_area.x = xc
    text_area.y = yc
    splash.append(text_area)
    for i in range(timein):
        pass
        time.sleep(1)

def textout(textin, bgcolor, xc, yc):
    text_area = label.Label(terminalio.FONT, text=textin, color=bgcolor)
    text_area.x = xc
    text_area.y = yc
    splash.append(text_area)

#------------------------------------------------------------------------------------------------------#
# 
# sonar code   
#  
#------------------------------------------------------------------------------------------------------#    
 
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D3)
threshold = 0.3

def sonar():
    try:
        # reads value 4 times as to guarentee no false readings
        num_detected = 0
        for x in range(0, 3):
            print("Distance: " + str(sonar.distance))
            if sonar.distance < threshold:
                print("Detected!")
                num_detected += 1
            time.sleep(0.01)
        return num_detected < 3
    except RuntimeError:
        print("Retrying!")
    return False

#------------------------------------------------------------------------------------------------------#
# 
# dance code
#     
#------------------------------------------------------------------------------------------------------#        

pwm1 = pulseio.PWMOut(board.D10, frequency=50) #leg1
legL = servo.ContinuousServo(pwm1)

pwm2 = pulseio.PWMOut(board.D11, frequency=50) #leg2
legR = servo.ContinuousServo(pwm2)

pwm3 = pulseio.PWMOut(board.D12, frequency=50)
footL = servo.ContinuousServo(pwm3)

pwm4 = pulseio.PWMOut(board.D13, frequency=50)
footR = servo.ContinuousServo(pwm4)

###################################
# define basic dance move functions 

# rotates right foot outwards and back in
def rightShuffle():
    footR.throttle = 0.0
    
    angle = -0.5
    while angle < 0.5:  # 0 - 180 degrees, 5 degrees at a time.
        legR.throttle = angle
        time.sleep(0.05)
        angle = angle + 0.1
    while angle >= -0.5:  # 0 - 180 degrees, 5 degrees at a time.
        legR.throttle = angle
        time.sleep(0.05)
        angle = angle - 0.1
    
    footR.throttle = 0.0
    

# rotates left foot outwards and back in
def leftShuffle():
    footL.throttle = 0.1
    
    angle = -0.3
    while angle < 0.8:  # 0 - 180 degrees, 5 degrees at a time.
        legL.throttle = angle
        time.sleep(0.05)
        angle = angle + 0.1
    while angle >= -0.3:  # 0 - 180 degrees, 5 degrees at a time.
        legL.throttle = angle
        time.sleep(0.05)
        angle = angle - 0.1
    
    footL.throttle = 0.1


# lift upwards by pointing both feet
def jump():
    legR.throttle = 0.1
    legL.throttle = 0.1
    footR.throttle = 0.1
    footL.throttle = 0.1
    time.sleep(2)
    
    angle = 0.1
    while angle < 0.4:  # 0 - 180 degrees, 5 degrees at a time.
        footL.throttle = angle
        footR.throttle = 0.1  - angle
        time.sleep(0.1)
        angle = angle + 0.05
    time.sleep(1)
    while angle >= 0.1:  # 0 - 180 degrees, 5 degrees at a time.
        footL.throttle = angle
        footR.throttle = 0.1 - angle
        time.sleep(0.1)
        angle = angle - 0.05


# moves right leg forward and back down
def rightKick():
    legR.throttle = -0.8
    
    angle = 0.0
    while angle < 0.7:  # 0 - 180 degrees, 5 degrees at a time.
        footR.throttle = angle
        time.sleep(0.05)
        angle = angle + 0.1
    while angle >= -0.1:  # 0 - 180 degrees, 5 degrees at a time.
        footR.throttle = angle
        time.sleep(0.05)
        angle = angle - 0.1
    
    legR.throttle = -0.8


# moves left leg forward and back down
def leftKick():
    legL.throttle = 0.9
    
    angle = 0.3
    while angle > -0.7:  # 0 - 180 degrees, 5 degrees at a time.
        footL.throttle = angle
        time.sleep(0.05)
        angle = angle - 0.1
    while angle <= 0.3:  # 0 - 180 degrees, 5 degrees at a time.
        footL.throttle = angle
        time.sleep(0.05)
        angle = angle + 0.1
    
    legL.throttle = 0.9


# takes a step forward by lifting right foot
def rightStep():
    footL.throttle = 0.1
    legL.throttle = 0.0
    
    footR.throttle = 0.1
    legR.throttle = 0.1
    time.sleep(3)
    
    angleL = 0.1
    while angleL >= -0.2:  # 0 - 180 degrees, 5 degrees at a time.
        footR.throttle = angleL
        time.sleep(0.05)
        angleL = angleL - 0.05
        
    angleF = 0.1
    while angleF >= -0.4:  # 0 - 180 degrees, 5 degrees at a time.
        legR.throttle = angleF
        time.sleep(0.05)
        angleF = angleF - 0.1


# takes a step forward by lifting left foot
def leftStep():
    footL.throttle = 0.1
    legL.throttle = 0.0
    
    footR.throttle = 0.1
    legR.throttle = 0.1
    time.sleep(3)
    
    angleL = 0.1
    while angleL <= 0.3:  # 0 - 180 degrees, 5 degrees at a time.
        footL.throttle = angleL
        time.sleep(0.05)
        angleL = angleL - 0.05
        
    angleF = 0.1
    while angleF >= -0.4:  # 0 - 180 degrees, 5 degrees at a time.
        legL.throttle = angleF
        time.sleep(0.05)
        angleF = angleF - 0.1


def tiltLeft():
    print("right kick")
    for i in range(3):
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)

def tiltright():
    print("right kick")
    for i in range(3):
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)


##############################################
# define dance moves as sequences of basic moves
def walk():
    for i in range(6):
        if not sonar():
            break
        tiltLeft()
        time.sleep(0.05)
        if not sonar():
            break
        tiltright()
        time.sleep(0.05)

def shuffle():
    for i in range(6):
        if not sonar():
            break
        leftShuffle()
        time.sleep(0.05)
        if not sonar():
            break
        rightShuffle()
        time.sleep(0.05)

def dance1():
    pass
def dance2():
    pass
def dance3():
    pass
def dance4():
    pass
def dance5():
    pass
def dance6():
    pass
    
#------------------------------------------------------------------------------------------------------#
# 
# keypad code   
#  
#------------------------------------------------------------------------------------------------------#    

# Setting up input pins
# Board D13 to keypad pin 1
row0 = digitalio.DigitalInOut(board.A4)
row0.direction = digitalio.Direction.INPUT
row0.pull = digitalio.Pull.UP
#Board D12 to keypad pin 2a
row1 = digitalio.DigitalInOut(board.A5)
row1.direction = digitalio.Direction.INPUT
row1.pull = digitalio.Pull.UP
#Board D11 to keypad pin 3
# row2 = digitalio.DigitalInOut(board.D11)
# row2.direction = digitalio.Direction.INPUT
# row2.pull = digitalio.Pull.UP
# #Board D10 to keypad pin 4
# row3 = digitalio.DigitalInOut(board.D10)
# row3.direction = digitalio.Direction.INPUT
# row3.pull = digitalio.Pull.UP

out1 = digitalio.DigitalInOut(board.A2)
out1.direction = digitalio.Direction.OUTPUT
out1.value = False

out2 = digitalio.DigitalInOut(board.A3)
out2.direction = digitalio.Direction.OUTPUT
out2.value = False

# #Board D9 to keypad pin 5
# col0 = digitalio.DigitalInOut(board.D9)
# col0.direction = digitalio.Direction.OUTPUT
# col0.value = False;
# #Board D6 to keypad pin 6
# col1 = digitalio.DigitalInOut(board.D6)
# col1.direction = digitalio.Direction.OUTPUT
# # col1.pull = digitalio.Pull.UP
# col1.value = False;
# #Board D5 to keypad pin 7
# col2 = digitalio.DigitalInOut(board.D5)
# col2.direction = digitalio.Direction.OUTPUT
# col2.value = False;

# col0 = (out1 && !out2)
# col1 = (out2 && !out1)
# col2 = (out1 && out2)

# Membrane 3x4 matrix keypad 
# cols = [digitalio.DigitalInOut(x) for x in (col0, col1, col2)]
#rows = [digitalio.DigitalInOut(x) for x in (board.A4, board.A5)]
 
# define key values using a tuple
keys = ((1, 2, 3),
        (4, 5, 6)#,
        # (7, 8, 9),
        # ('*', 0, '#')
        )
 
# keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

def keypadDecode():
    key = 0
    for i in range(1,4):
        time.sleep(.1)
        if i == 1:
            out2.value = True
            out1.value = False
        if i == 2:
            out1.value = True
            out2.value = False
        if i == 3:
            out1.value = True
            out2.value = True
        key = keypadHelper(i)
        if key != 0:
            return key
    return key

def keypadHelper(col):
    if not row0.value:
        return col
    if not row1.value:
        return col+3
    return 0

def checkPass():
    seq = []
    pwd = [1, 1, 1, 1]
    i = 0

    while True: 
        # keys = keypad.pressed_keys
        keys = keypadDecode()
        if keys: 
            seq.append(keys)
            i = i + 1
            time.sleep(0.4)

        if i >= 4: 
            if seq == pwd: 
                seq = []
                i = 0
                return True
            else: 
                seq = []
                return False

        time.sleep(0.1)
               
#------------------------------------------------------------------------------------------------------#
# 
# gui code
#     
#------------------------------------------------------------------------------------------------------#    
LOADING = 0
PASSCODE = 1
HOME = 2
DANCE = 3
MUSIC = 4
ABOUT = 5
EXIT = 6
REQUEST = 7

state = LOADING
while True:

    if state ==  LOADING:
        splash = displayio.Group(max_size=100)
        reset()
        textshow("Loading.....", 0x000000, 30, 64, 1)
        reset()
        textshow("Welcome", 0x000000, 30, 64, 1)
        reset()
        textshow("CPEN 291", 0x000000, 30, 64, 1)
        reset()
        state =  PASSCODE

    if state ==  PASSCODE:
        textout("enter the passcode", 0x000000, 10, 60)
        boolean = False
        boolean = checkPass()
        if boolean:
            boolean = False
            state =  HOME
            reset()
        else:
            reset()
            textshow("wrong passcode", 0x000000, 10, 60, 2)
            #time.sleep(1)
            state = PASSCODE
            reset()
        
    elif state ==  HOME:
        textout("Press a key: \n 1) Dance Menu \n 2) Music \n 3) Exit \n 4) About ", 0x000000, 10, 60)
        keys = 0
        while keys == 0:
            keys = keypadDecode()

        if keys == 1:
            state =  DANCE
            reset()
        elif keys == 2:
            state =  MUSIC
            reset()
        elif keys == 3:
            state =  EXIT
            reset()
        elif keys == 4:
            state =  ABOUT
        else:
            state =  HOME
        
    elif state ==  DANCE:
        textout("Press a key: \n 1) Shuffle \n 2) Kick \n 3) Moonwalk \n 5) Wobble \n 5) Squat \n 6) Spin", 0x000000, 10, 60)
        keys = 0
        while keys == 0:
            keys = keypadDecode()

        if keys == 1:
            dance1()
            state =  REQUEST
            reset()
        elif keys == 2:
            dance2()
            state =  REQUEST
            reset()
        elif keys == 3:
            dance3()
            state =  REQUEST
            reset()
        elif keys == 4:
            dance4()
            state =  REQUEST
            reset()
        elif keys == 5:
            dance5()
            state =  REQUEST
            reset()
        elif keys == 6:
            dance6()
            state =  REQUEST
            reset()
        else:
            state =  DANCE

    elif state ==  ABOUT:
        textshow("About: \n Dancing Robot GUI", 0x000000, 10, 10, 5)
        textshow("press any button to return", 0x000000, 10, 60, 5)
       
        keys =0
        while keys == 0:
            keys = keypadDecode()

        if keys == 1:
            state =  HOME
            reset()
            textshow("Created By: \n 1)Manek \n  2)Sanjeev \n 3)Parsa \n 4)Amir \n 5)Stella \n 6)Arnold \n 7)Rain", 0x000000, 10, 60, 1)
            time.sleep(1)
            reset()
        elif keys == 2:
            state =  HOME
            reset()
            textshow("Created By: \n 1)Manek \n  2)Sanjeev \n 3)Parsa \n 4)Amir \n 5)Stella \n 6)Arnold \n 7)Rain", 0x000000, 10, 60, 1)
            time.sleep(1)
            reset()
        elif keys == 3:
            state =  HOME
            reset()
            textshow("Created By: \n 1)Manek \n  2)Sanjeev \n 3)Parsa \n 4)Amir \n 5)Stella \n 6)Arnold \n 7)Rain", 0x000000, 10, 60, 1)
            time.sleep(1)
            reset()
        elif keys == 4:
            state =  HOME
            reset()
            textshow("Created By: \n 1)Manek \n  2)Sanjeev \n 3)Parsa \n 4)Amir \n 5)Stella \n 6)Arnold \n 7)Rain", 0x000000, 10, 60, 1)
            time.sleep(1)
            reset()
        elif keys == 5:
            state =  HOME
            reset()
            textshow("Created By: \n 1)Manek \n  2)Sanjeev \n 3)Parsa \n 4)Amir \n 5)Stella \n 6)Arnold \n 7)Rain", 0x000000, 10, 60, 1)
            time.sleep(1)
            reset()
        elif keys == 6:
            state =  HOME
            reset()
            textshow("Created By: \n 1)Manek \n  2)Sanjeev \n 3)Parsa \n 4)Amir \n 5)Stella \n 6)Arnold \n 7)Rain", 0x000000, 10, 60, 1)
            time.sleep(1)
            reset()
        else:
            state =  ABOUT

    elif state ==  EXIT:
        textshow("Exiting.....", 0x000000, 30, 64, 3)
        time.sleep(0.5)
        #state =  PASSCODE
        sys.exit()
        #reset()

    elif state ==  REQUEST:
        textout("Press a key: \n 1) Dance  \n 2) Play Music \n 3) Home", 0x000000, 10, 60)
        
        keys = 0
        while keys == 0:
            keys = keypadDecode()

        if keys == 1:
            state =  DANCE
            reset()
        elif keys == 2:
            state =  MUSIC
            reset()
        elif keys == 3:
            state =  HOME
            reset()
        else:
            state =  REQUEST

    elif state ==  MUSIC:
        textout("Press a key: \n 1) USSR \n 2) Mario \n 3) Crimson \n 5) Canon \n 5) Tetris \n 6) Default", 0x000000, 10, 60)

        keys = 0
        while keys == 0:
            keys = keypadDecode()

        if keys == 1:
            USSR()
            state =  REQUEST
            reset()
        elif keys == 2:
            mario_theme()
            state =  REQUEST
            reset()
        elif keys == 3:
            crimson()
            state =  REQUEST
            reset()
        elif keys == 4:
            canon()
            state =  REQUEST
            reset()
        elif keys == 5:
            tetris()
            state =  REQUEST
            reset()
        elif keys == 6:
            default()
            state =  REQUEST
            reset()
        else:
            state =  MUSIC
<<<<<<< HEAD
=======




>>>>>>> fa562d7e378fc819a3176c54d8c78b90128909e2
