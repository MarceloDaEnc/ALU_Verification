from pyuvm import *
from .seq_item import SeqItem
from .defs import Operation

CoverageBins = [
    Operation.CARRY_SUM,
    Operation.SUM_OF_ZEROS,
    Operation.NEGATIVE_SUBTRACTION,
    Operation.SELF_SUBTRACTION,
    Operation.MUL_TRUNCATION,
    Operation.MUL_FULL_PRECISION,
    Operation.DIV_ZERO_NUMERATOR,
    Operation.DIV_BY_ZERO,
    Operation.DIV_BY_ONE,
    Operation.DIV_SELF,
    Operation.DIV_SMALLER_NUMERATOR
]

class Coverage(uvm_subscriber):
    """
    Collects and verifies functional coverage for the PIE environment.
    """
    def end_of_elaboration_phase(self):
        self.cvg = set()

    def write(self, item):
        if isinstance(item, SeqItem):
            coverage_bin = (
                item.type
            )
            self.cvg.add(coverage_bin)

    def report_phase(self):
        try:
            disable_errors = ConfigDB().get(self, "", "DISABLE_COVERAGE_ERRORS")
        except UVMConfigItemNotFound:
            disable_errors = False

        if not disable_errors:
            coverage_bins_set = set(CoverageBins)
            missed_bins = coverage_bins_set - self.cvg
            if len(missed_bins) > 0:
                self.logger.error("Functional coverage error!")
                self.logger.error(f"  -> Bins not covered: {missed_bins}")
                assert False
            else:
                self.logger.info("✅ Functional coverage reached all bins.")
                assert True