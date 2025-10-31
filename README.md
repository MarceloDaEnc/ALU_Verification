# ALU_Verification

Este repositório contém um ambiente de verificação funcional desenvolvido em Python, utilizando as bibliotecas Cocotb e pyuvm, para validar o comportamento de uma ULA (Unidade Lógica e Aritmética) de 32 bits escrita em Verilog.

O objetivo é garantir que a ULA opere corretamente para todas as operações aritméticas e lógicas especificadas, incluindo soma, subtração, multiplicação e divisão, por meio de testes dirigidos e aleatórios.

# Tecnologias Utilizadas

    Python 3.10+

    Cocotb — Framework de verificação baseado em co-rotinas para testbenches Python.

    pyuvm — Implementação da metodologia UVM (Universal Verification Methodology) em Python.

    Icarus Verilog — Simulador Verilog.

    Make — Para automação de build e execução dos testes.

# Como Executar

Clone o repositório:

    git clone https://github.com/<usuario>/ALU_Verification.git
    cd ALU_Verification

Instale as dependências:

    pip install cocotb pyuvm

Execute a simulação:

    make 

# 👨‍💻 Autores

Desenvolvido por Marcelo Rodrigues Soares

Universidade Federal de São Carlos (UFSCar)

Projeto de verificação digital com Cocotb + pyuvm