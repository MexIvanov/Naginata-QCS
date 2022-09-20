# Naginata-QCS
Naginata - Quantum Circuit Synthesizer is aimed to assist in development of complex quantum algorithms and circuits

The program enables users to use pre-difined circuits as components for building more complex circuits

## Available functions
Some of these functions could generate reversed forms of their operations by running them with argument qreverse=True.
See "qnn_static_test.py" and "qnn_generation_tests.py" for usage examples

1) adder - generates an adder for two registers of simmilar size, uses no ancilla qubits
2) multiplier - multiplies two registers of simmilar (x) size, outputs result in a register of 2*x size
3) multiplier_asymmetric - multiplies two registers of different size (xs - size of smaller register), outputs result in a register of 3*xs size (helps to save size)
4) if_equal - checks bit by bit if two registers of simmilar size are equal, returns result into the target register
5) multi_control_gate_3cx - generates a gate with more than 3 controls, using 4 qubit Toffoli gates and ancilla qubits
6) multi_target_gate - generates a sequence of gates that are controlled by same control qubits, but have different targets
7) build_param_network - builds a circuit for training a perceptron of specified topology, see qnn_generation_tests.py for reference
8) Toffoli_4q or gate "GName.CCCX" - 4 qubit Toffoli with no ancilla qubits 
9) export_qasm - export specified circuit to specified file

## Example circuits
1) Running "qnn_static_test.py" returns a file with a training circuit for a simple example neural network (perceptron). The purpose of this usage example is to show how circuits could be built using the pre-defined "building blocks" in "naginata.py"

2) Running "qnn_generation_tests.py" returns 3 files with training circuits for 3 simple example neural networks (perceptrons).
