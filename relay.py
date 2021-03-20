import RPi.GPIO as GPIO
import time
import json

#%% Switch function definitions
def turn_on(pin):
    GPIO.output(pin, GPIO.LOW)
    print('Turned On')

def turn_off(pin):
    GPIO.output(pin, GPIO.HIGH)
    print('Turned Off')

#%% Load config file

relayConfigFile = open('relayconfig.json')
relayConfig = json.load(relayConfigFile)

print('Relay Configurations Loaded')

#%% Initialization

GPIO.setmode(GPIO.BCM)

for pin in relayConfig['GPIOPins']:
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
    time.sleep(1)
    GPIO.cleanup()
