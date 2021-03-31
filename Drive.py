# Each Drive object will consist of:
#   - Source path
#   - Target path
#   - Sleep timer (to be used in async task)
#       + Note: Time units can be specified. Default sleep time is 1 day (script runs once a day)

class Drive:
    def __init__(self, source, target, sleep_timer=1, time_units=4):
        self.source = source
        self.target = target

        if time_units == 1:
            # Time in seconds
            self.sleep_timer = sleep_timer
        elif time_units == 2:
            # Time in minutes
            self.sleep_timer = sleep_timer * 60
        elif time_units == 3:
            # Time in hours
            self.sleep_timer = sleep_timer * 3600
        else:
            # Time in days
            self.sleep_timer = sleep_timer * 86400

    def setSourcePath(self, source):
        self.source = source
    
    def getSourcePath(self):
        return self.source

    def setTargetPath(self, target):
        self.target = target

    def getTargetPath(self):
        return self.target

    def setSleepTimer(self, time):
        self.sleep_timer = time * 60

    def getSleepTimer(self):
        return sleep_timer

    def setTimeUnits(self, units):
        if units == 1:
            # Time in seconds
            self.sleep_timer = sleep_timer
        elif units == 2:
            # Time in minutes
            self.sleep_timer = sleep_timer * 60
        elif units == 3:
            # Time in hours
            self.sleep_timer = sleep_timer * 3600
        else:
            # Time in days
            self.sleep_timer = sleep_timer * 86400

    def getTimeUnits(self):
        return self.time_units