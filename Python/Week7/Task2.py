# 2. Create class Clock and it's subclass AlarmClock. 
# Test clocks in main. 
# There has to be ticking and alarming methods...

class Clock:

    type = 'time'

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def setHours(self, hours):
            self.hours = hours
    def setMinutes(self, minutes):
            self.minutes = minutes
    def setSeconds(self, seconds):
            self.seconds = seconds
    
    def getTime(self):
        time = str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
        return time

class Alarm(Clock):

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def setHours(self, hours):
            self.hours = hours
    def setMinutes(self, minutes):  
            self.minutes = minutes
    def setSeconds(self, seconds):
            self.seconds = seconds
    
    def getAlarm(self):
        alarm = str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
        return alarm

time = Clock(0,0,0)
alarm = Alarm(7,30,0)

def MainClock():
    menu = 0

    while menu != 4: 
        print("\n1. Set time")
        print("2. Set alarm")
        print("3. Start clock")
        print("4. Exit")
        menu = int(input("\n(1-4):"))

        #Set time
        if menu == 1:
            hours = int(input("Hours: "))
            minutes = int(input("Minutes: "))
            seconds = int(input("Seconds: "))
            if hours > 23 or minutes > 59 or seconds > 59:
                print("Error")
                input("Press enter to continue")
            else:
                time.setHours(hours)
                time.setMinutes(minutes)
                time.setSeconds(seconds)
                print("Time has been set to: "+ time.getTime())
                input("Press enter to continue")
        #Set alarm
        if menu == 2:
            hours = int(input("Hours: "))
            minutes = int(input("Minutes: "))
            seconds = int(input("Seconds: "))
            if hours > 23 or minutes > 59 or seconds > 59:
                print("Error")
                input("Press enter to continue")
            else:
                alarm.setHours(hours)
                alarm.setMinutes(minutes)
                alarm.setSeconds(seconds)
                print("Alarm has been set to: "+ alarm.getAlarm())
                input("Press enter to continue")       
        #Start clock
        if menu == 3:
            while time.getTime() != alarm.getAlarm():
                if time.getTime() == "23:59:59":
                    time.setHours(00)
                    time.setMinutes(00)
                    time.setSeconds(00)
                elif time.minutes == 59 and time.seconds == 59:
                    time.setHours(time.hours +1)
                    time.setMinutes(00)
                    time.setSeconds(00)
                elif time.seconds == 59:
                    time.setMinutes(time.minutes +1)
                    time.setSeconds(00)                   
                else:
                    time.setSeconds(time.seconds + 1)
            print("Alarm! Time is: " + time.getTime())


MainClock()