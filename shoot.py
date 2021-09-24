import RPi.GPIO as GPIO
import time

servo_pin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

p = GPIO.PWM(servo_pin, 50)
p.start(2.5)
try:
    while True:
        print(5)
        p.ChangeDutyCycle(2)
        time.sleep(1)
        print(10)
        p.ChangeDutyCycle(10)
        time.sleep(1)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
