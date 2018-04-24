import time
import RPi.GPIO as GPIO
from lcd import*;
ULTRASONIC_TIMEOUT = 0.5

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 13
GPIO_ECHO    = 19

print "Ultrasonic Measurement"

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    GPIO.output(GPIO_TRIGGER, False)

    time.sleep(0.5)

    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.01)
    GPIO.output(GPIO_TRIGGER, False)

    timeout_start = time.time()
    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()
        period = start - timeout_start
        if period > ULTRASONIC_TIMEOUT:
            return False
    #print('start: %s'%start)
    timeout_start = time.time()
    stop = 0
    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()
        period = stop - timeout_start
        if period > ULTRASONIC_TIMEOUT:
            return False
    #print('stop: %s'%stop)

    elapsed = stop-start
    dis = elapsed * 34300
    dis = dis / 2
    return dis

def loop():
    global lcd
    lcd = LCD()
    while True:
        d = distance()
        lcd.message('distance:\n                ')
        print('distance:%0.2fcm' % d)
        #lcd.clear()
        lcd.message('distance:\n%0.2fcm' % d)
        time.sleep(0.2)

def destroy():
    lcd.destroy()
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        destroy()