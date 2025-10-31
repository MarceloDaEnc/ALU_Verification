import cocotb
from cocotb.triggers import Timer, RisingEdge

class Bfm:
    """
    Bus Functional Model (BFM) for the verification environment.
    This class handles all direct interactions with the DUT signals.
    It is implemented as a singleton to ensure a single point of contact with the DUT.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.dut = cocotb.top
            self.dut.clk.value = 0
            self.dut.rst.value = 1
            self.dut.opcode_in.value = 0
            self.dut.A_in.value = 0
            self.dut.B_in.value = 0
            self.clk = 0

    async def clock(self, period):
        """Generates the main clock signal for the DUT."""
        self.clk = 0
        while True:
            await cocotb.triggers.Timer(period / 2, units="ns")
            self.clk = not self.clk
            self.dut.clk.value = self.clk

    async def reset(self):
        """Drives the DUT reset sequence."""
        self.dut.rst.value = 1
        for _ in range(4):
            await cocotb.triggers.RisingEdge(self.dut.clk)
        self.dut.rst.value = 0

    async def send_seq(self, item):
        """Sends a complete sequence of data."""
        await cocotb.triggers.RisingEdge(self.dut.clk)
        self.dut.A_in.value = item.A
        self.dut.B_in.value = item.B
        self.dut.opcode_in.value = item.opcode



    async def monitor_outputs(self, ap):
        """Collects the decoded data that will be used by Scoreboard."""
        self.out_low = 0
        self.out_hi = 0
        self.carry_out = 0
        self.borrow_out = 0
        self.error_out = 0

        for _ in range(5):
            await cocotb.triggers.RisingEdge(self.dut.clk)

        while True:
            await cocotb.triggers.Edge(self.dut.clk)
            await cocotb.triggers.First(cocotb.triggers.Edge(self.dut.A_in), cocotb.triggers.Edge(self.dut.B_in), cocotb.triggers.Edge(self.dut.opcode_in))

            self.out_low = self.dut.result_out_low.value
            self.out_hi = self.dut.result_out_hi.value
            self.carry_out = self.dut.carry.value
            self.borrow_out = self.dut.borrow.value
            self.error_out = self.dut.error_out.value

            ap.write((self.out_low, self.out_hi, self.carry_out, self.borrow_out, self.error_out))

            self.out_low = 0
            self.out_hi = 0
            self.carry_out = 0
            self.borrow_out = 0
            self.error_out = 0