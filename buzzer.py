import time
import board
import pulseio

piezo = pulseio.PWMOut(board.A1 , duty_cycle=0, frequency=440, variable_frequency=True)

def USSR_anthem():
    while True:
        for f in (196, 277, 277, 196, 196, 220, 247, 247, 165, 165, 233, 233, 196, 196, 174, 208, 208, 131, 131, 156, 156, 147, 147,
                  165, 185, 185, 174, 174, 196, 233, 233, 123, 123, 262, 311, 311, 196, 330, 294, 261, 311, 247, 196, 277, 247, 220,
                  247, 165, 165, 233, 196, 131, 131, 277, 247, 220, 207, 207, 207):
            piezo.frequency = f
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(0.25)  # On for 1/4 second
            piezo.duty_cycle = 0  # Off
            time.sleep(0.05)  # Pause between notes
        time.sleep(0.5)

#Mario main theme melody
#Source: https://www.princetronics.com/supermariothemesong/
def mario_theme():
    while True:
            for f in (330, 330, 0, 330, 0, 262, 330, 0, 392, 0, 0,  0, 196, 0, 0, 0,
                    262, 0, 0, 196, 0, 0, 165, 0, 0, 220, 0, 247, 0, 233, 220, 0,
                    196, 330, 392, 440, 0, 349, 392, 0, 330, 0, 262, 294, 247, 0, 0):
                piezo.frequency = f
                piezo.duty_cycle = 65536 // 2  # On 50%
                time.sleep(0.25)  # On for 1/4 second
                piezo.duty_cycle = 0  # Off
                time.sleep(0.05)  # Pause between notes
            time.sleep(0.5)

# all i want for christmas intro
# Source: https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0109830
def crimson():
    while True:
        for f in (196, 247, 294, 370, 392, 370, 294, 247, 196, 262, 294, 392, 294):
            piezo.frequency = f
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(0.25)  # On for 1/4 second
            piezo.duty_cycle = 0  # Off
            time.sleep(0.05)  # Pause between notes
        time.sleep(0.5)

# pachebel Canon in C
def canon():
    while True:
        for f in (131, 165, 196, 262, 98, 123, 147, 196, 110, 131, 165, 220, 82, 98, 123, 165, 87, 110, 131, 175, 
                131, 165, 196, 262, 87, 110, 131, 175, 98, 123, 147, 196, 110):
            piezo.frequency = f
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(0.25)  # On for 1/4 second
            piezo.duty_cycle = 0  # Off
            time.sleep(0.05)  # Pause between notes
        time.sleep(0.5)

def meganolovania():
    while True:
        for f in (294, 294, 587, 440, 415, 392, 349, 294, 349, 392, 261, 261, 261, 261, 587, 440, 415, 392, 349, 294,
                  349, 392, 247, 247, 587, 440, 415, 392, 349, 294, 349, 392, 233, 233, 233, 233, 587, 440, 415, 392,
                  349, 294, 349, 392, 294, 294, 587, 440, 415, 392, 349, 294, 249, 392, 261, 261, 261, 261, 587, 440,
                  415, 392, 349, 294, 349, 392, 247, 247, 587, 440, 415, 392, 349, 294, 349, 392, 233, 233, 233, 233,
                  588, 440, 415, 392, 349, 294, 349, 392):
            piezo.frequency = f
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(0.12)  # On for 1/4 second
            piezo.duty_cycle = 0  # Off
            time.sleep(0.005)  # Pause between notes
        time.sleep(0.5)
