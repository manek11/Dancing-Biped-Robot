import time
import board
import pulseio
import servo

import adafruit_hcsr04

# piezo buzzer setup
piezo = pulseio.PWMOut(board.A1, duty_cycle=0, frequency=440, variable_frequency=True)

# servo setup
pwm1 = pulseio.PWMOut(board.D10, frequency=50)
legL = servo.Servo(pwm1)

pwm2 = pulseio.PWMOut(board.D11, frequency=50)
legR = servo.Servo(pwm2)

pwm3 = pulseio.PWMOut(board.D12, frequency=50)
footR = servo.Servo(pwm3)

pwm4 = pulseio.PWMOut(board.D13, frequency=50)
footL = servo.Servo(pwm4)

music = 1

###################################
# frequency lists for the six songs

ANTHEM = [392, 523, 392, 440, 494, 330, 330,
          440, 392, 349, 392, 262, 262,
          294, 294, 330, 349, 349, 392, 440, 494, 523, 587,
          659, 587, 523, 587, 494, 392,
          523, 494, 440, 494, 330, 330,
          440, 392, 349, 392, 262, 262,
          523, 494, 440, 392, 494, 523, 587,
          659, 587, 523, 494, 523, 587, 392, 392, 494, 523, 587,
          523, 494, 440, 392, 440, 494, 330, 330, 392, 440, 494,
          523, 440, 494, 523, 440, 494, 523, 440, 523, 698,
          698, 659, 587, 523, 587, 659, 523, 523,
          587, 523, 494, 440, 494, 523, 440, 440,
          523, 494, 440, 392, 262, 392, 440, 494, 523]

MARIO = [659, 659, 659, 523, 659, 784, 392, 523, 392, 330, 440, 494, 466, 440, 392, 659, 784, 880, 698, 784, 659,
         523, 587, 494, 523, 392, 330, 440, 494, 466, 440, 392, 659, 784, 880, 698, 784, 659, 523, 587, 494]

STRANGER = [131, 165, 196, 247, 262, 247, 196, 165]

ALLSTAR = [466, 369, 369, 311, 369, 369, 369, 311, 369, 369, 369, 466, 466, 369, 369, 311, 369, 369, 369, 311,
         369, 369, 369, 466, 369, 466, 554, 494, 554, 622, 740, 831, 740, 369, 369, 415, 369, 466, 415, 415,
         369, 415, 311]

TETRIS = [659, 494, 523, 587, 659, 587, 523, 494, 440, 440, 523, 659, 587, 523, 494, 494, 494, 523, 587, 523,
          494, 494, 494, 523, 587, 659, 523, 440, 440, 587, 587, 698, 880, 784, 698, 659, 659, 523, 659, 587,
          523, 494, 494, 523, 587, 659, 523, 440, 440, 659, 494, 523, 587, 659, 587, 523, 494, 440, 440, 523,
          659, 587, 523, 494, 494, 523, 587, 659, 523, 440, 440, 587, 587, 698, 880, 784, 698, 659, 659, 523,
          659, 587, 523, 587, 659, 523, 440, 440]

DEFAULT = [349, 415, 466, 466, 415, 349, 415, 466, 466, 415, 349, 311, 349, 466, 415, 349, 311, 349]


def playSong(song, delay):
    for i in range(len(song)):
        piezo.frequency = song[i]
        piezo.duty_cycle = 65536 // 2  # On 50%
        time.sleep(delay)  # On


def playNote(freq, delay):
    piezo.frequency = freq
    piezo.duty_cycle = 65536 // 2  # On 50%
    time.sleep(delay)  # On


############################
# basic dance move functions

def rotate(limb, min, max, step, start, song):
    i = start
    for x in range(min, max + step, step):
        limb.angle = x
        if music == 1:
            playNote(song[i % len(song)], 0.3)
        else:
            time.sleep(0.3)
        i += 1
    return i


def double_rotate(limb1, limb2, min, max, step, start, song):
    i = start
    for x in range(min, max + step, step):
        limb1.angle = x
        limb2.angle = x
        playNote(song[i % len(song)], 0.3)
        i += 1
    return i

def tapFoot(start, song, limb):
    if limb == footL:
        start = rotate(footL, 90, 60, -10, start, song)
        start = rotate(footL, 60, 90, 10, start, song)
    else:
        start = rotate(footR, 100, 130, 10, start, song)
        start = rotate(footR, 130, 100, -10, start, song)
    return start

def kick(start, song, limb):
    if limb == legR:
        limb.angle = 160
        start = rotate(footR, 100, 60, -10, start, song)
        start = rotate(footR, 60, 100, 10, start, song)
        limb.angle = 90
    else:
        limb.angle = 20
        start = rotate(footL, 90, 130, 10, start, song)
        start = rotate(footL, 130, 90, -10, start, song)
        limb.angle = 90
    return start

def footIn(start, song, limb):
    if limb == legR:
        start = rotate(limb, 90, 10, -10, start, song)
        start = rotate(limb, 10, 90, 10, start, song)
    else:
        start = rotate(limb, 90, 170, 10, start, song)
        start = rotate(limb, 170, 90, -10, start, song)
    return start

def footOut(start, song, limb):
    if limb == legR:
        start = rotate(limb, 90, 160, 10, start, song)
        start = rotate(limb, 160, 90, -10, start, song)
    else:
        start = rotate(legL, 90, 20, -10, start, song)
        start = rotate(legL, 20, 90, 10, start, song)
    return start


def wiggle(start, song):
    start = rotate(footL, 90, 130, 10, start, song)
    start = rotate(footR, 100, 60, -10, start, song)
    start = rotate(footL, 130, 90, -10, start, song)
    start = rotate(footR, 60, 100, 10, start, song)
    return start


def shuffle(start, song):
    for angle in range(90, 30, -15):  # 0 - 180 degrees, 5 degrees at a time.
        start = double_rotate(legL, legR, angle, angle, -15, start, song)
    for angle in range(30, 90, 15):  # 180 - 0 degrees, 5 degrees at a time.
        start = double_rotate(legL, legR, angle, angle, 15, start, song)
    for angle in range(90, 120, 15):  # 0 - 180 degrees, 5 degrees at a time.
        start = double_rotate(legL, legR, angle, angle, -15, start, song)
    for angle in range(120, 90, -15):  # 180 - 0 degrees, 5 degrees at a time.
        start = double_rotate(legL, legR, angle, angle, 15, start, song)
    return start


def reset():
    footR.angle = 97
    footL.angle = 92
    legR.angle = 90
    legL.angle = 90
    time.sleep(0.1)


###################################################################
# 6 dance moves created as a combination of the smaller moves above

def dance1():
    start = 0
    for i in range(3):
        start = wiggle(start, STRANGER)


def dance2():
    start = 0
    for i in range(2):
        start = footOut(start, MARIO, legL)
        start = footIn(start, MARIO, legL)
        start = footOut(start, MARIO, legR)
        start = footIn(start, MARIO, legR)


def dance3():
    start = 0
    start = footOut(start, ANTHEM, legL)
    start = tapFoot(start, ANTHEM, footL)
    start = kick(start, ANTHEM, legL)

    start = footOut(start, ANTHEM, legR)
    start = tapFoot(start, ANTHEM, footR)
    start = kick(start, ANTHEM, legR)
    reset()


def dance4():
    start = 0
    for j in range(3):
        start = tapFoot(start, TETRIS, footL)
    for j in range(3):
        start = tapFoot(start, TETRIS, footR)


def dance5():
    start = 0
    for i in range(3):
        start = kick(start, ALLSTAR, legL)
        start = kick(start, ALLSTAR, legR)


def dance6():
    start = 0
    for i in range(3):
        start = shuffle(start, DEFAULT)
