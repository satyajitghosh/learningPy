'''Main Purpose of Bridge pattern is to decouple Abstraction from Implementation.
Both the abstracted part and the implemented part can develop separately.'''

from abc import ABC,abstractmethod

class Appliance(ABC):
    '''Appliance can have any number of functions which can be called internally.
    They must have start and stop.'''
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Switch(ABC):
    def __init__(self,app:Appliance):
        self.app = app
    @abstractmethod
    def on(self):
        pass
    @abstractmethod
    def off(self):
        pass

class Pump(Appliance):
    def primepump(self):
        print('priming pump')
    def turnvalve(self):
        print('Turning valve')
    def start(self):
        self.turnvalve()
        self.primepump()
        print('Starting Pump')
    def stop(self):
        self.turnvalve()
        print('Stopping Pump')

class Heater(Appliance):
    def checkcoil(self):
        print('priming pump')
    def start(self):
        self.checkcoil()
        print('Starting Heater')
    def stop(self):
        print('Stopping heater')


class SiemensSwitch(Switch):
    def configcheck(self):
        print(f'Siemens Switch with app {self.app}')
    def on(self):
        self.app.start()
    def off(self):
        self.app.stop()

class ABBSwitch(Switch):
    def configcheck(self):
        print(f'Siemens Switch with app {self.app}')
    def on(self):
        self.app.start()
    def off(self):
        self.app.stop()


'''There's huge benefit from this.
The Appliances can be developed independently from switches.
as long as both classes have the respective necessary functions
that have been defined in their respective interfaces.'''

def client():
    mypump = Pump()
    myswitch = SiemensSwitch(mypump)
    myswitch.on()
    myswitch.off()