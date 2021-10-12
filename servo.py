    
# PWM pins A1, D13, D12,D9, D10, D7, D11
import time
import board
import pulseio
import servo
 
pwm1 = pulseio.PWMOut(board.D10, frequency=50) #leg1
my_servo1 = servo.ContinuousServo(pwm1)

pwm2 = pulseio.PWMOut(board.D11, frequency=50) #leg2
my_servo2 = servo.ContinuousServo(pwm2)

pwm3 = pulseio.PWMOut(board.D12, frequency=50)
my_servo3 = servo.ContinuousServo(pwm3)

pwm4 = pulseio.PWMOut(board.D13, frequency=50)
my_servo4 = servo.ContinuousServo(pwm4)
 
while True:
    my_servo1.throttle = 1.0
    my_servo2.throttle = 1.0
    time.sleep(1.0)
    my_servo3.throttle = 1.0
    my_servo1.throttle = 1.0
    my_servo2.throttle = 1.0
    my_servo3.throttle = 0.3
    time.sleep(1.0)
    my_servo4.throttle = 0.1
    my_servo1.throttle = 0.1
    my_servo2.throttle = 0.0
    my_servo4.throttle = 0.3
    my_servo1.throttle = -1.0
    my_servo2.throttle = -1.0
    time.sleep(1.0)
    my_servo1.throttle = 0.1
    time.sleep(3.0)
    
    ############################33
    import time
import board
import pulseio
  
# Initialize PWM output for the servo (on pin A1):
servo1 = pulseio.PWMOut(board.D12, frequency=50) #foot A1, D13, D12,D9, D10, D7, D11
servo2 = pulseio.PWMOut(board.D13, frequency=50) #foot
servo3 = pulseio.PWMOut(board.D10, frequency=50) #leg
servo4 = pulseio.PWMOut(board.D9, frequency=50)  #leg

 
# Create a function to simplify setting PWM duty cycle for the servo:
def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle
 
# Main loop will run forever moving between 1.0 and 2.0 mS long pulses:
while True:
    servo1.duty_cycle = servo_duty_cycle(1.0)
    servo2.duty_cycle = servo_duty_cycle(0.3)
    servo3.duty_cycle = servo_duty_cycle(1.0)
    servo4.duty_cycle = servo_duty_cycle(0.3)
    time.sleep(1.0)
    servo1.duty_cycle = servo_duty_cycle(2.0)
    servo2.duty_cycle = servo_duty_cycle(1.0)
    servo3.duty_cycle = servo_duty_cycle(2.0)
    servo4.duty_cycle = servo_duty_cycle(1.0)
 
########################
    
import time
import board
import pulseio
import servo
 
#pwm1 = pulseio.PWMOut(board.D10, frequency=50) #RIGHT LEG
#my_servo1 = servo.ContinuousServo(pwm1)

#pwm2 = pulseio.PWMOut(board.D11, frequency=50)  #LEFT LEG
#my_servo2 = servo.ContinuousServo(pwm2)

#pwm3 = pulseio.PWMOut(board.D12, frequency=50) #rigHT FOOT
#my_servo3 = servo.ContinuousServo(pwm3)

#pwm4 = pulseio.PWMOut(board.D13, frequency=50) #left foot
#my_servo4 = servo.ContinuousServo(pwm4)
 
while True:
    my_servo3.throttle = 1.0
    time.sleep(1.0)
    my_servo3.throttle = -1.0
    time.sleep(1.0)
