import cocotb
from pyuvm import *
from .utils import alu_32_bit_golden_model

class Scoreboard(uvm_component):
    """
    Compares expected results with actual DUT results.
    """
    def build_phase(self):
        self.cmd_fifo = uvm_tlm_analysis_fifo("cmd_fifo", self)
        self.result_fifo = uvm_tlm_analysis_fifo("result_fifo", self)
        self.cmd_get_port = uvm_get_port("cmd_get_port", self)
        self.result_get_port = uvm_get_port("result_get_port", self)
        self.cmd_export = self.cmd_fifo.analysis_export
        self.result_export = self.result_fifo.analysis_export
        self.fail_count = 0

    def connect_phase(self):
        self.cmd_get_port.connect(self.cmd_fifo.get_export)
        self.result_get_port.connect(self.result_fifo.get_export)

    async def run_phase(self):
        while True:
            item = await self.cmd_get_port.get()
            (actual_out_low, actual_out_hi, actual_carry, actual_borrow, actual_error) = await self.result_get_port.get()
            if (actual_out_low == 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' or actual_out_hi == 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' or actual_carry == 'x' or actual_borrow == 'x' or actual_error == 'x'):
                actual_out_low = actual_out_hi = None
                actual_carry = 0
                actual_borrow = 0
                actual_error = 1
            else:
                actual_out_low   = int(actual_out_low)
                actual_out_hi    = int(actual_out_hi)
                actual_carry     = int(actual_carry)
                actual_borrow    = int(actual_borrow)
                actual_error     = int(actual_error)
            golden_outputs = alu_32_bit_golden_model(item.opcode, item.A, item.B)
            if (golden_outputs["result_out_low"] == actual_out_low and golden_outputs["result_out_hi"] == actual_out_hi and golden_outputs["carry"] == actual_carry
                and golden_outputs["borrow"] == actual_borrow and golden_outputs["error_out"] == actual_error):
                self.logger.info(f"✅ PASSED: {item}")
            else:
                self.logger.error(f"❌ FAILED: {item}")
                self.logger.error(
                    f"    └─ Expected: Result_Low={golden_outputs["result_out_low"]}, Result_Hi={golden_outputs["result_out_hi"]}, Carry={golden_outputs["carry"]}, Borrow={golden_outputs["borrow"]}, Error={golden_outputs["error_out"]}\n"
                    f"       Got:      Result_Low={actual_out_low}, Result_Hi={actual_out_hi}, Carry={actual_carry}, Borrow={actual_borrow}, Error={actual_error}"
                )
                self.fail_count += 1

    
    def report_phase(self):
        """Prints a final summary of the test results."""
        cocotb.log.info(f"\n+--------------------+")
        cocotb.log.info(f"| Final Fail Count: {self.fail_count:d} |")
        cocotb.log.info(f"+--------------------+")
        if self.fail_count > 0:
            assert False, f"{self.fail_count} failures detected in scoreboard"