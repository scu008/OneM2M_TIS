from tis.oneM2M import *
from sense_hat import *

# Warning!! In each class, one must implement only one class among get and control methods 


# Uplink(for monitoring and measurement) class
class Sensor(Thing):
    
    # Initialize
    def __init__(self):
        self.protocol = 'up'
        self.sense = SenseHat()
        self.interval = 0.5
        self.topic = ['Humidity']
        self.name = 'Sensor'
    
    # Thing dependent get function
    def get(self, key):
        
        if 'Humidity' == key:
            return self.sense.get_humidity()
        elif 'Temperature' == key:
            return self.sense.get_temperature()
        elif 'Pressure' == key:
            return self.sense.get_pressure()
        else :
            pass
    
    
    
# Downlink(for control and signal check) class  
class Panel(Thing):
    
    # Initialize
    def __init__(self):
        self.protocol = 'down'
        self.sense = SenseHat()
        self.topic = ['panel']
        self.name = 'Panel'
    
    
    # Thing dependent control function (need to format type of value)
    def control(self, key, value):

        if 'letter' == key:
            print('From server - letter : ', value)
            self.sense.show_letter( value )
            
        elif 'panel' == key:
            print('From server - panel : ', value)
            self.sense.show_message( value )
            
        else:
            pass
