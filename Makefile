# Makefile
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/rtl/*.v
TOPLEVEL = alu_32_bit
MODULE = tests.test_ULA

# Specify log file for simulation output
SIM_LOG_FILE = $(PWD)/testbench.log

# Enable VCD waveform dump
export WAVES = 1

# Include Cocotb simulation rules
include $(shell cocotb-config --makefiles)/Makefile.sim