import time
import RPi.GPIO as GPIO
from lcd import LCD;
from ultrasonic import Ultrasonic;
ULTRASONIC_TIMEOUT = 0.5

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 13
GPIO_ECHO    = 19

print "Ultrasonic Measurement"

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def loop():
    global lcd
    lcd = LCD()
    us = Ultrasonic(GPIO_TRIGGER, GPIO_ECHO)
    while True:
        distance = us.distance()
        if distance:
            lcd.message('distance:\n                ')
            print('distance:%0.2fcm' % distance)
            #lcd.clear()
            lcd.message('distance:\n%0.2fcm' % distance)
        else:
            print('Error')
        time.sleep(0.2)

def destroy():
    lcd.destroy()
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        destroy()