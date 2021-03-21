import relay
import schedule

class artificialLight:
    def __init__(self, GPIOPin, startTime, stopTime):
        self.GPIOPin = GPIOPin
        self.startTime = startTime
        self.stopTime = stopTime
        self.runSchedule()

    def runSchedule(self):
        schedule.every().day.do(self.turnOn)
        schedule.every().day.do(self.turnOff)

    def turnOn(self):
        relay.turn_on(self.GPIOPin)

    def turnOff(self):
        relay.turn_off(self.GPIOPin)