import RPi.GPIO as GPIO
import time
import json
from artificialLighting import artificialLight

#%% Switch function definitions
def turn_on(pin, deviceName = ''):
    GPIO.output(pin, GPIO.LOW)
    print(deviceName + 'Turned On')

def turn_off(pin, deviceName = ''):
    GPIO.output(pin, GPIO.HIGH)
    print(deviceName + 'Turned Off')

#%% Load config file

relayConfigFile = open('relayconfig.json')
relayConfig = json.load(relayConfigFile)

print('Relay Configurations Loaded')

#%% Relay Initialization

GPIO.setmode(GPIO.BCM)

for pin in relayConfig['GPIOPins']:
	GPIO.setup(pin, GPIO.OUT)
    turn_off(pin)

time.sleep(1)
print('GPIOs Initiated.')

#%% Schedule

relayNumber = 1
GPIOPins = relayConfig['GPIOPins']

try:
    while True:
        turn_on(GPIOPins[relayNumber - 1])
        time.sleep(10)
        turn_off(GPIOPins[relayNumber - 1])
        time.sleep(10)
except KeyboardInterrupt:
    print('Stopping process')
    turn_off([GPIOPins[relayNumber - 1]])
    time.sleep(1)
    GPIO.cleanup()

#%% Light

#lightRelayPin = 2
#lightObject = artificialLight(GPIOPins[lightRelayPin - 1], "06:00", "18:00", "LED Lamp")