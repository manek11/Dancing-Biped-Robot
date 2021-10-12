import time
import board
import pulseio
import servo

###########################################
# pin assignments and initial setup
pwm1 = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
legR = servo.Servo(pwm1)

pwm2 = pulseio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50) #leg2
legL = servo.Servo(pwm2)

pwm3 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
footL = servo.Servo(pwm3)

pwm4 = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)
footR = servo.Servo(pwm4)

#buzzer setup
piezo = pulseio.PWMOut(board.A1 , duty_cycle=0, frequency=440, variable_frequency=True)



###################################
# define basic functions
def reset(): 
    legR.angle = 94
    legL.angle = 90
    footR.angle = 90
    footL.angle = 91

def rotate(limb, min, max, step):
    for x in range(min, max, step):
        limb.angle = x

# define single dance move functions 
def leftFootOut():
    rotate(legL, 90, 180, 5)
    rotate(legL, 180, 90, -5)

def rightFootOut():
    rotate(legR, 90, 10, -5)
    rotate(legR, 10, 90, 5)
    
def leftFootIn():
    rotate(legL, 90, 20, -5)
    rotate(legL, 20, 90, 5)

def rightFootIn():
    rotate(legR, 90, 160, 5)
    rotate(legR, 160, 90, -5)

def jump():
    reset()
    for angle in range(90, 130, 5):  # 0 - 180 degrees, 5 degrees at a time.
        footL.angle = angle
        footR.angle = 90 - (angle - 90)
    for angle in range(130, 90, -5): # 180 - 0 degrees, 5 degrees at a time.
        footL.angle = angle
        footR.angle = 90 - (angle - 90)
    reset()

def rightKick():
    legR.angle = 20
    rotate(footR, 90, 130, 4)
    rotate(footR, 130, 90, -4)
    reset()

def leftKick():
    legL.angle = 160
    rotate(footL, 90, 60, -3)
    rotate(footL, 60, 90, 3)
    reset()

def shuffle():
    for angle in range(90, 60, -5):  # 0 - 180 degrees, 5 degrees at a time.
        legL.angle = angle
        legR.angle = 90 + (angle - 60)
    for angle in range(60, 90, 5): # 180 - 0 degrees, 5 degrees at a time.
        legL.angle = angle
        legR.angle = 90 + (angle - 60)
    reset()    

def wiggle():
    rotate(footL, 90, 130, 5)
    rotate(footR, 90, 60, -5)
    rotate(footL, 130, 90, -5)
    rotate(footR, 60, 90, 5)


def tapLeftFoot():
    reset()
    rotate(footL, 90, 60, -3)
    rotate(footL, 60, 90, 3)
    reset()
    
def tapRightFoot():
    reset()
    rotate(footR, 90, 120, 3)
    rotate(footR, 120, 90, -3)
    reset()
 
def tapBothFeet():
    reset()
    for angle in range(90, 130, 8):  # 0 - 180 degrees, 5 degrees at a time.
        footL.angle = 90 - (angle - 90)
        footR.angle = angle
    for angle in range(130, 90, -8): # 180 - 0 degrees, 5 degrees at a time.
        footL.angle = 90 - (angle - 90)
        footR.angle = angle
    reset()



####################################################
# song frequency arrays
ANTHEM = [196, 277, 196, 220, 247, 165, 165, 233, 196, 174, 208, 131, 131, 156, 147, 165, 185, 174, 196, 233, 123,
            262, 311, 311, 196, 330, 294, 261, 311, 247, 196, 277, 247, 220, 247, 165, 165, 233, 196, 131, 131, 277,
            247, 220, 207, 207, 207]

MARIO = [330, 330, 330, 262, 330, 392, 196, 262, 196, 165, 220, 247, 233, 220, 196, 330, 392, 440, 349, 392, 330, 
            262, 294, 247]

CRIMSON = [196, 247, 294, 370, 392, 370, 294, 247, 196, 262, 294, 392, 294]

CANON = [131, 165, 196, 262, 98, 123, 147, 196, 110, 131, 165, 220, 82, 98, 123, 165, 87, 110, 131, 175, 
            131, 165, 196, 262, 87, 110, 131, 175, 98, 123, 147, 196, 110]

TETRIS = [659, 494, 523, 587, 659, 587, 523, 494, 440, 440, 523, 659, 587, 523, 494, 494, 494, 523, 587, 523,
            494, 494, 494, 523, 587, 659, 523, 440, 440, 587, 587, 698, 880, 784, 698, 659, 659, 523, 659, 587, 
            523, 494, 494, 523, 587, 659, 523, 440, 440, 659, 494, 523, 587, 659, 587, 523, 494, 440, 440, 523, 
            659, 587, 523, 494, 494, 523, 587, 659, 523, 440, 440, 587, 587, 698, 880, 784, 698, 659, 659, 523,
            659, 587, 523, 587, 659, 523, 440, 440]

DEFAULT = [149, 149, 149, 446, 1485, 149, 149, 149, 446, 297, 297, 149, 595, 149, 149, 149, 149, 1931]


###################################
# define buzzer song functions
def play_note(freq):
    piezo.frequency = freq
    piezo.duty_cycle = 65536 // 2  # On 50%
    time.sleep(0.3) # On for 1/4 second
    piezo.duty_cycle = 0 # Off




####################################################
# define 6 main dance moves

#1: slide to intro to All I Want for Christmas is You - Mariah Carey
def dance1():
    reset()
    for i in range(0, 12, 1):
        play_note(CRIMSON[i])
        wiggle()
    reset()


#2: line dance to the MARIO THEME song
def dance2():
    for i in range(0, len(MARIO) - 4, 4):
        play_note(MARIO[i])
        leftFootOut()
        play_note(MARIO[i+1])
        leftFootIn()
        play_note(MARIO[i+2])
        rightFootOut()
        play_note(MARIO[i+3])
        rightFootIn()


#3: karate kick to the USSR ANTHEM
def dance3():
    for i in range(0, len(ANTHEM) - 6, 6):
        play_note(ANTHEM[i])
        leftFootOut()
        play_note(ANTHEM[i+1])
        tapLeftFoot()
        play_note(ANTHEM[i + 2])
        leftKick()

        play_note(ANTHEM[i + 3])
        rightFootOut()
        play_note(ANTHEM[i + 4])
        tapRightFoot()
        play_note(ANTHEM[i + 5])
        rightKick()

#4: tap feet to the beat of Tetris background music
def dance4():
    for i in range(0, len(TETRIS) - 12, 12):
        for j in range(0, 3, 1):
            play_note(TETRIS[i + j])
            tapLeftFoot()
        for j in range(0, 3, 1):  
            play_note(TETRIS[i + 4 + j])
            tapRightFoot()
        for j in range(0, 3, 1):
            play_note(TETRIS[i + 8 + j])
            tapBothFeet()

#5: walk to Pachebel Canon in C
def dance5():
    for i in range(0, len(CANON) - 2, 2):
        play_note(CANON[i])
        leftKick()
        play_note(CANON[i + 1])
        rightKick()

#6: wiggle to the fortnite default song
def dance6():
    for i in range(0, len(DEFAULT) - 2, 2):
        play_note(DEFAULT[i])
        shuffle()

