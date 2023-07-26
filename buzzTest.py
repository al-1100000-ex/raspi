import RPi.GPIO as GPIO
import time

buzzerPin = 12
lightPin = 11


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT)
    GPIO.setup(lightPin, GPIO.OUT)
    GPIO.setup(lightPin, GPIO.LOW)


def loop():
    buzz = True
    while True:
        if buzz:
            GPIO.output(buzzerPin, GPIO.LOW)
            GPIO.output(lightPin, GPIO.HIGH)
            print('buzz')
        else:
            GPIO.output(buzzerPin, GPIO.HIGH)
            GPIO.output(lightPin, GPIO.LOW)
            print('stop')
        time.sleep(1)
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
