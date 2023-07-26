import RPi.GPIO as GPIO
import time

buzzerPin = 11
lightPin = 12


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT)
    GPIO.setup(lightPin, GPIO.OUT)
    GPIO.setup(lightPin, GPIO.LOW)


def loop():
    buzz = True
    while True:
        sl = 1
        if buzz:  # on
            GPIO.output(buzzerPin, GPIO.LOW)
            GPIO.output(lightPin, GPIO.HIGH)
            sl = 0.1
        else:  # off
            GPIO.output(buzzerPin, GPIO.HIGH)
            GPIO.output(lightPin, GPIO.LOW)
        time.sleep(sl)
        buzz = not buzz


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
