from pyuvm import *
from .bfm import Bfm

class Monitor(uvm_component):
    """Monitors the DUT's transmission interface (TX)."""
    def __init__(self, name, parent):
        super().__init__(name, parent)

    def build_phase(self):
        self.ap = uvm_analysis_port("ap", self)
        self.bfm = Bfm()

    async def run_phase(self):
        """Starts the monitoring task in the BFM."""
        self.bfm.logger = self.logger 
        await self.bfm.monitor_outputs(self.ap) 