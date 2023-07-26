import RPi.GPIO as GPIO

buzzerPin = 11


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT)


def loop():
    while True:
        GPIO.output(buzzerPin, GPIO.LOW)
        print('buzz')


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
