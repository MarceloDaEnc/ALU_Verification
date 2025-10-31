module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/alu_32_bit.fst");
    $dumpvars(0, alu_32_bit);
end
endmodule
