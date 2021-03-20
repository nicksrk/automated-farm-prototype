import RPi.GPIO as GPIO
import time

#%% Switch function definitions
def turn_on(pin):
    GPIO.output(pin, GPIO.HIGH)
    print('Turned On')

def turn_off(pin):
    GPIO.output(pin, GPIO.LOW)
    print('Turned Off')

#%% Initialization
relayPin = [1] #Enter the relay pins being used
GPIOPin = [27] #Enter corresponding GPIO pin numbers

print('Relay and GPIO pins mapped.')

GPIO.setmode(GPIO.BCM)

for pin in GPIOPin:
	GPIO.setup(pin, GPIO.OUT)

time.sleep(1)
print('GPIOs Initiated.')

#%% Schedule

try:
    while True:
        turn_on(GPIOPin[0])
        time.sleep(10)
        turn_off(GPIOPin[0])
        time.sleep(10)
except KeyboardInterrupt:
    print('Stopping process')
    turn_off(GPIOPin[0])
    time.sleep(5)
    GPIO.cleanup()