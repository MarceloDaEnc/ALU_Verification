
import random
from pyuvm import uvm_sequence
from .seq_item import SeqItem

class ULACoverageSeq(uvm_sequence):
    """
    Generates a sequence that covers all bins in CoverageBins with random data.
    """
    async def body(self):

        item = SeqItem("carry_sum", 4294967295, 1, 0, 0)
        await self.start_item(item)
        await self.finish_item(item)

        item = SeqItem("sum_of_zeros", 0, 0, 0, 1)
        await self.start_item(item)
        await self.finish_item(item)

        item = SeqItem("negative_subtraction", 0, 1, 1, 2)
        await self.start_item(item)
        await self.finish_item(item)

        item = SeqItem("self_subtraction", 10, 10, 1, 3)
        await self.start_item(item)
        await self.finish_item(item)

        item = SeqItem("mul_truncation", 4294967295, 2, 2, 4)
        await self.start_item(item)
        await self.finish_item(item)

        item = SeqItem("mul_full_precision", 4294967295, 4294967295, 2, 5)
        await self.start_item(item)
        await self.finish_item(item)

        item = SeqItem("div_by_zero", 7, 0, 3, 6)
        await self.start_item(item)
        await self.finish_item(item)

        item = SeqItem("div_zero_numerator", 0, 10, 3, 7)
        await self.start_item(item)
        await self.finish_item(item)

        item = SeqItem("div_by_one", 8, 1, 3, 8)
        await self.start_item(item)
        await self.finish_item(item)

        item = SeqItem("div_self", 20, 20, 3, 9)
        await self.start_item(item)
        await self.finish_item(item)

        item = SeqItem("div_small_numerator", 10, 20, 3, 10)
        await self.start_item(item)
        await self.finish_item(item)

        for _ in range (10000):
            item = SeqItem("random", random.randint(0, 4294967295), random.randint(0, 4294967295), random.randint(0, 3), 0)
            await self.start_item(item)
            await self.finish_item(item)


