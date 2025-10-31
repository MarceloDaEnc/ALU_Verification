module alu_32_bit (
    input clk,
    input rst,

    // Entradas
    input [1:0]  opcode_in, // 00:ADD, 01:SUB, 10:MUL, 11:DIV
    input [31:0] A_in,
    input [31:0] B_in,
    
    // Saídas
    output reg [31:0] result_out_low,
    output reg [31:0] result_out_hi,
    output reg carry, // 1 se result_out_low > 0xFFFFFFFF
    output reg borrow, // 1 se result_out_low < 0
    output reg error_out  // 1 se B=0 na divisão
);

    // O 'coração' da ULA (Implementação simplificada)
    always @(posedge clk) begin
        if (rst) begin
            result_out_low <= 32'd0;
            result_out_hi <= 32'd0;
            carry <= 1'b0;
            borrow <= 1'b0;
            error_out  <= 1'b0;
        end else begin
            // Reseta os erros
            result_out_low <= 32'd0;
            result_out_hi <= 32'd0;
            carry <= 1'b0;
            borrow <= 1'b0;
            error_out <= 1'b0;

            case (opcode_in)
                // ADD: {Carry, Soma}
                2'b00: {carry, result_out_low} <= A_in + B_in;
                
                // SUB: {Borrow, Subtração}
                2'b01: {borrow, result_out_low} <= A_in - B_in;

                // MUL: Resultado de 64 bits
                2'b10: {result_out_hi, result_out_low} <= A_in * B_in;

                // DIV: {Resto, Quociente}
                2'b11: begin
                    if (B_in == 32'd0) begin
                        error_out <= 1'b1; // Erro: Divisão por zero!
                        result_out_low <= 32'hX; // Indefinido
                        result_out_hi <= 32'hX; // Indefinido
                    end else begin
                        result_out_low <= A_in / B_in; // Quociente
                        result_out_hi <= A_in % B_in; // Resto
                    end
                end
                
                default: begin
                    result_out_low <= 32'hX;
                    result_out_hi <= 32'hX;
                end
            endcase
        end
    end

endmodule