import time
import board
import pulseio
import servo

from analogio import AnalogIn
import adafruit_hcsr04

class RobotDance:
    # frequency lists for dance songs
    ANTHEM = [196, 277, 196, 220, 247, 165, 165, 233, 196, 174, 208, 131, 131, 156, 147, 165, 185, 174, 196, 233, 123,
            262, 311, 311, 196, 330, 294, 261, 311, 247, 196, 277, 247, 220, 247, 165, 165, 233, 196, 131, 131, 277,
            247, 220, 207, 207, 207]

    MARIO = [2637, 2637, 0, 2637, 0, 2093, 2637, 0, 3136, 0, 0,  0, 1568, 0, 0, 0,
                2093, 0, 0, 1568, 0, 0, 1319, 0, 0, 1760, 0, 1976, 0, 1865, 1760, 0,
                1568, 2637, 3136, 3520, 0, 2794, 3136, 0, 2637, 0, 2093, 2349, 1976, 0, 0,
                2093, 0, 0, 1568, 0, 0, 1319, 0, 0, 1760, 0, 1976, 0, 1865, 1760, 0,
                1568, 2637, 3136, 3520, 0, 2794, 3136, 0, 2637, 0, 2093, 2349, 1976, 0, 0]

    CRIMSON = [196, 247, 294, 370, 392, 370, 294, 247, 196, 262, 294, 392, 294]

    CANON = [131, 165, 196, 262, 98, 123, 147, 196, 110, 131, 165, 220, 82, 98, 123, 165, 87, 110, 131, 175, 
                131, 165, 196, 262, 87, 110, 131, 175, 98, 123, 147, 196, 110]

    TETRIS = [659, 494, 523, 587, 659, 587, 523, 494, 440, 440, 523, 659, 587, 523, 494, 494, 494, 523, 587, 523,
                494, 494, 494, 523, 587, 659, 523, 440, 440, 587, 587, 698, 880, 784, 698, 659, 659, 523, 659, 587, 
                523, 494, 494, 523, 587, 659, 523, 440, 440, 659, 494, 523, 587, 659, 587, 523, 494, 440, 440, 523, 
                659, 587, 523, 494, 494, 523, 587, 659, 523, 440, 440, 587, 587, 698, 880, 784, 698, 659, 659, 523,
                659, 587, 523, 587, 659, 523, 440, 440]

    DEFAULT = [149, 149, 149, 446, 1485, 149, 149, 149, 446, 297, 297, 149, 595, 149, 149, 149, 149, 1931]

    THRESHOLD = 0.3

    ###########################################
    # pin assignments and initial setup
    def __init__(self):
        #buzzer setup
        self.piezo = pulseio.PWMOut(board.A1 , duty_cycle=0, frequency=440, variable_frequency=True)

        #servo setup
        pwm1 = pulseio.PWMOut(board.D10, frequency=50) #leg1
        self.legL = servo.ContinuousServo(pwm1)

        pwm2 = pulseio.PWMOut(board.D11, frequency=50) #leg2
        self.legR = servo.ContinuousServo(pwm2)

        pwm3 = pulseio.PWMOut(board.D12, frequency=50)
        self.footL = servo.ContinuousServo(pwm3)

        pwm4 = pulseio.PWMOut(board.D13, frequency=50)
        self.footR = servo.ContinuousServo(pwm4)

        # ultrasonic sensor pin initialization
        self.sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D3)

    ###########################################
    # plays a single note on piezo buzzer using given frequency
    def play_note(self, freq):
        self.piezo.frequency = freq
        self.piezo.duty_cycle = 65536 // 2  # On 50%
        time.sleep(0.25) # On for 1/4 second
        self.piezo.duty_cycle = 0 # Off
    

    ###################################
    # define basic dance move functions 

    # rotates right foot outwards and back in
    def rightShuffle(self):
        self.footR.throttle = 0.0
        
        angle = -0.5
        while angle < 0.5:  # 0 - 180 degrees, 5 degrees at a time.
            self.legR.throttle = angle
            time.sleep(0.05)
            angle = angle + 0.1
        while angle >= -0.5:  # 0 - 180 degrees, 5 degrees at a time.
            self.legR.throttle = angle
            time.sleep(0.05)
            angle = angle - 0.1
        
        self.footR.throttle = 0.0
        

    # rotates left foot outwards and back in
    def leftShuffle(self):
        self.footL.throttle = 0.1
        
        angle = -0.3
        while angle < 0.8:  # 0 - 180 degrees, 5 degrees at a time.
            self.legL.throttle = angle
            time.sleep(0.05)
            angle = angle + 0.1
        while angle >= -0.3:  # 0 - 180 degrees, 5 degrees at a time.
            self.legL.throttle = angle
            time.sleep(0.05)
            angle = angle - 0.1
        
        self.footL.throttle = 0.1


    # rotate both feet outwards at the same time (simultaneous leftShuffle and rightShuffle)
    def butterfly(self): 
        self.footR.throttle = 0.0
        self.footL.throttle = 0.1

        angle = -0.5
        while angle < 0.5:  # 0 - 180 degrees, 5 degrees at a time.
            self.legR.throttle = angle
            self.legL.throttle = angle + 0.2
            time.sleep(0.05)
            angle = angle + 0.1
        while angle >= -0.5:  # 0 - 180 degrees, 5 degrees at a time.
            self.legR.throttle = angle
            self.legL.throttle = angle + 0.2
            time.sleep(0.05)
            angle = angle - 0.1
        
        self.footR.throttle = 0.0
        self.footL.throttle = 0.1


    # lift upwards by pointing both feet
    def jump(self):
        self.legR.throttle = 0.1
        self.legL.throttle = 0.1
        self.footR.throttle = 0.1
        self.footL.throttle = 0.1
        time.sleep(2)
        
        angle = 0.1
        while angle < 0.4:  # 0 - 180 degrees, 5 degrees at a time.
            self.footL.throttle = angle
            self.footR.throttle = 0.1  - angle
            time.sleep(0.1)
            angle = angle + 0.05
        time.sleep(1)
        while angle >= 0.1:  # 0 - 180 degrees, 5 degrees at a time.
            self.footL.throttle = angle
            self.footR.throttle = 0.1 - angle
            time.sleep(0.1)
            angle = angle - 0.05


    # moves right leg forward and back down
    def rightKick(self):
        self.legR.throttle = -0.8
        
        angle = 0.0
        while angle < 0.7:  # 0 - 180 degrees, 5 degrees at a time.
            self.footR.throttle = angle
            time.sleep(0.05)
            angle = angle + 0.1
        while angle >= -0.1:  # 0 - 180 degrees, 5 degrees at a time.
            self.footR.throttle = angle
            time.sleep(0.05)
            angle = angle - 0.1
        
        self.legR.throttle = -0.8
1

    # moves left leg forward and back down
    def leftKick(self):
        self.legL.throttle = 0.9
        
        angle = 0.3
        while angle > -0.7:  # 0 - 180 degrees, 5 degrees at a time.
            self.footL.throttle = angle
            time.sleep(0.05)
            angle = angle - 0.1
        while angle <= 0.3:  # 0 - 180 degrees, 5 degrees at a time.
            self.footL.throttle = angle
            time.sleep(0.05)
            angle = angle + 0.1
        
        self.legL.throttle = 0.9


    # takes a step forward by lifting right foot
    def rightStep(self):
        self.footL.throttle = 0.1
        self.legL.throttle = 0.0
        
        self.footR.throttle = 0.1
        self.legR.throttle = 0.1
        time.sleep(3)
        
        angleL = 0.1
        while angleL >= -0.2:  # 0 - 180 degrees, 5 degrees at a time.
            self.footR.throttle = angleL
            time.sleep(0.05)
            angleL = angleL - 0.05
            
        angleF = 0.1
        while angleF >= -0.4:  # 0 - 180 degrees, 5 degrees at a time.
            self.legR.throttle = angleF
            time.sleep(0.05)
            angleF = angleF - 0.1


    #TODO debug/ test this move
    # takes a step forward by lifting left foot
    def leftStep(self):
        self.footL.throttle = 0.1
        self.legL.throttle = 0.0
        
        self.footR.throttle = 0.1
        self.legR.throttle = 0.1
        time.sleep(3)
        
        angleL = 0.1
        while angleL <= 0.3:  # 0 - 180 degrees, 5 degrees at a time.
            self.footL.throttle = angleL
            time.sleep(0.05)
            angleL = angleL - 0.05
            
        angleF = 0.1
        while angleF >= -0.4:  # 0 - 180 degrees, 5 degrees at a time.
            self.legL.throttle = angleF
            time.sleep(0.05)
            angleF = angleF - 0.1



    ##############################################
    # define dance moves as sequences of basic moves

    #Dance 1: walk forward
    def walk(self):
        if (not self.check_distance()):
            return

        for i in range(6):
            self.leftStep()
            self.play_note(self.DEFAULT[i * 2])
            time.sleep(0.5)
            self.rightStep()
            self.play_note(self.DEFAULT[i * 2 + 1])
            time.sleep(0.5)

    #Dance 2: kick feet outwards one at a time
    def shuffle(self):
        if (not self.check_distance()):
            return

        for i in range(4):
            self.leftShuffle()
            self.play_note(self.CANON[i * 2])
            time.sleep(0.05)
            self.rightShuffle()
            self.play_note(self.CANON[i * 2 + 1])
            time.sleep(0.05)

    # Dance 3: kick both feet outwards at the same time then tippy toe
    def ballerina(self):
        if (not self.check_distance()):
            return

        for i in range(4):
            self.butterfly()
            self.play_note(self.CRIMSON[i * 2])
            time.sleep(0.05)
            self.jump()
            self.play_note(self.CRIMSON[i * 2 + 1])
            time.sleep(0.05)

    #Dance 4: line dancing move
    def pigeon(self):
        if (not self.check_distance()):
            return

        for i in range(4):
            self.leftShuffle()
            self.play_note(self.TETRIS[i * 4])
            time.sleep(0.05)
            self.leftKick()
            self.play_note(self.TETRIS[i * 4 + 1])
            time.sleep(0.2)
            self.rightShuffle()
            self.play_note(self.TETRIS[i * 4 + 2])
            time.sleep(0.05)
            self.rightKick()
            self.play_note(self.TETRIS[i * 4 + 3])
            time.sleep(1)

    #Dance 5: up and down
    def excite(self):
        if (not self.check_distance()):
            return

        for i in range(4):
            self.jump()
            self.play_note(self.ANTHEM[i])
            time.sleep(0.1)

    #Dance 6: left karate kick
    def karate(self):
        if (not self.check_distance()):
            return

        for i in range(4):
            self.leftShuffle()
            self.play_note(self.MARIO[i * 3])
            time.sleep(0.1)
            self.jump()
            self.play_note(self.MARIO[i * 3 + 1])
            time.sleep(0.1)
            self.leftKick()
            self.play_note(self.MARIO[i * 3 + 2])
            time.sleep(0.5)

    # function for checking if robot is close to an object
    def check_distance(self):
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

