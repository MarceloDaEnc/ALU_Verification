from pyuvm import *
from .driver import Driver
from .monitor import Monitor

class Agent(uvm_agent):
    """
    The agent encapsulates the driver, monitor and sequencer for the interface.
    """
    def build_phase(self):
        self.seqr = uvm_sequencer.create("seqr", self)
        self.driver = Driver.create("driver", self)
        self.monitor = Monitor.create("monitor", self)

    def connect_phase(self):
        self.driver.seq_item_port.connect(self.seqr.seq_item_export)
        
        self.driver_ap = self.driver.ap
        self.monitor_ap = self.monitor.ap