from enum import IntEnum

class Operation(IntEnum):
    CARRY_SUM = 0                  # Soma com overflow (carry esperado)
    SUM_OF_ZEROS = 1               # Soma trivial (0 + 0)
    NEGATIVE_SUBTRACTION = 2       # Subtração A < B (gera borrow)
    SELF_SUBTRACTION = 3           # Subtração A - A (resultado 0)
    MUL_TRUNCATION = 4             # Multiplicação com truncamento esperado
    MUL_FULL_PRECISION = 5         # Multiplicação com produto de 64 bits
    DIV_BY_ZERO = 6                # Divisão por zero (erro esperado)
    DIV_ZERO_NUMERATOR = 7         # Divisão 0/x
    DIV_BY_ONE = 8                 # Divisão x/1
    DIV_SELF = 9                   # Divisão x/x (resultado 1, resto 0)
    DIV_SMALLER_NUMERATOR = 10     # Divisão A/B com A < B (resultado 0, resto A)