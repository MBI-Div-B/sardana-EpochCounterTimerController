import time
from sardana import State
from sardana.pool.controller import CounterTimerController

class EpochCounterTimerController(CounterTimerController):
    """The most basic controller intended from demonstration purposes only.
    This is the absolute minimum you have to implement to set a proper counter
    controller able to get a counter value, get a counter state and do an
    acquisition.

    This example is so basic that it is not even directly described in the
    documentation"""
    def AddDevice(self, axis):
        pass

    def DeleteDevice(self, axis):
        pass

    def __init__(self, inst, props, *args, **kwargs):
        """Constructor"""
        super(epochCounterTimerController,
              self).__init__(inst, props, *args, **kwargs)
        self.int_time = 0
        self.start_time = 0

    def ReadOne(self, axis):
        """Get the specified counter value"""
        return self.start_time

    def StateOne(self, axis):
        """Get the specified counter state"""        
        if (time.time() - self.start_time) < self.int_time:
            return State.Moving, "Counter is acquiring"
        else:
            return State.On, "Counter is stopped"
        
    def StartOne(self, axis, value):
        """acquire the specified counter"""
        self.int_time = value
        self.start_time = time.time()

    def StartAll(self):
        pass

    def LoadOne(self, axis, value, repetitions):
        pass

    def StopOne(self, axis):
        """Stop the specified counter"""
        pass