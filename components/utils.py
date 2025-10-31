def alu_32_bit_golden_model(opcode_in, A_in, B_in):
    MASK_32 = 0xFFFFFFFF
    A = A_in & MASK_32
    B = B_in & MASK_32
    
    # Inicialização das saídas
    result_out_low = 0
    result_out_hi = 0
    carry = 0
    borrow = 0
    error_out = 0
    
    # ---------------------------------
    # Simulação do 'case (opcode_in)'
    # ---------------------------------
    
    if opcode_in == 0b00:  # ADD: {carry, result_out_low} <= A_in + B_in
        full_sum = A + B
        result_out_low = full_sum & MASK_32
        carry = (full_sum >> 32) & 1
        
    elif opcode_in == 0b01:  # SUB: {borrow, result_out_low} <= A_in - B_in
        result_out_low = (A - B) & MASK_32
        borrow = 1 if A < B else 0
        
    elif opcode_in == 0b10:  # MUL: {result_out_hi, result_out_low} <= A_in * B_in
        full_mul = A * B
        result_out_low = full_mul & MASK_32
        result_out_hi = (full_mul >> 32) & MASK_32
        
    elif opcode_in == 0b11:  # DIV: {Resto, Quociente}
        if B == 0:
            # Erro: Divisão por zero
            error_out = 1
            result_out_low = None 
            result_out_hi = None
        else:
            result_out_low = (A // B) & MASK_32
            result_out_hi = (A % B) & MASK_32
            
    else:  # default:
        result_out_low = None
        result_out_hi = None

    # Retorna um dicionário para facilitar a verificação
    return {
        "result_out_low": result_out_low,
        "result_out_hi": result_out_hi,
        "carry": carry,
        "borrow": borrow,
        "error_out": error_out
    }