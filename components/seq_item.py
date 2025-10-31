from pyuvm import uvm_sequence_item

class SeqItem(uvm_sequence_item):
    """
    Represents a single transaction.
    """
    def __init__(self, name, A, B, opcode, type):
        super().__init__(name)
        self.A = A
        self.B = B
        self.opcode = opcode
        self.type = type

    def __str__(self):
        A_hex = f"0x{self.A:X}"
        B_hex = f"0x{self.B:X}"
        s = (f"A: {A_hex:<10} | "
             f"B: {B_hex:<10} | "
             f"OpCode: {self.opcode:<6}")
        return s