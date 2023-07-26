import RPi.GPIO as GPIO
import time

buzzerPin = 11


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT)


def loop():
    buzz = True
    while True:
        if buzz:
            GPIO.output(buzzerPin, GPIO.LOW)
            print('buzz')
        else:
            GPIO.output(buzzerPin, GPIO.HIGH)
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
