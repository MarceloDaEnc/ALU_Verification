# -----------------------------------------------------------------------------
# FILE NAME : test_ULA.py
# AUTHOR : Marcelo Rodrigues Soares
# AUTHOR’S EMAIL : marcelosoares@estudante.ufscar.br
# -----------------------------------------------------------------------------
# RELEASE HISTORY           VERSION DATE          AUTHOR DESCRIPTION
# 1.0                       2025-10-31 marcelo    First Release
# -----------------------------------------------------------------------------

import cocotb
import pyuvm
from pyuvm import *

from components.env import Env
from components.bfm import Bfm
from components.seq import ULACoverageSeq


@pyuvm.test()
class ULATest(uvm_test):
    """
    The main test class that instantiates the environment and executes the sequences.
    """
    def build_phase(self):
        ConfigDB().set(None, "*", "DISABLE_COVERAGE_ERRORS", False)
        self.env = Env.create("env", self)

    def end_of_elaboration_phase(self):
        self.test_seq = ULACoverageSeq.create("test_seq")

    async def run_phase(self):
        self.raise_objection()
        
        bfm = Bfm()
            
        clock_task = cocotb.start_soon(bfm.clock(520))
            
        await bfm.reset()
            
        seqr = ConfigDB().get(self, "", "SEQR")
        await self.test_seq.start(seqr)

        await cocotb.triggers.Timer(100000, units="ns")

        clock_task.kill()

        self.drop_objection()