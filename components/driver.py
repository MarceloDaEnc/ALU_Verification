from pyuvm import *
from .bfm import Bfm

class Driver(uvm_driver):
    """
    Drives the sequence items to the DUT via the BFM.
    """
    def build_phase(self):
        self.ap = uvm_analysis_port("ap", self)

    def start_of_simulation_phase(self):
        self.bfm = Bfm()

    async def run_phase(self):
        while True:
            item = await self.seq_item_port.get_next_item()
        
            await self.bfm.send_seq(item)
            
            self.ap.write(item)
            self.seq_item_port.item_done()