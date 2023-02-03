from naginata import *

def GroverNq_test(number_of_qubits, flipped_qbit=2) -> Circuit:
    """ N qubit Grover example - builds a "textbook" example of Grover's algorithm on N qubits
    and flips one of the target value's qubits in the oracle function
    """

    circ = Circuit()
    
    grover_reg = Register(number_of_qubits)
    grover_qubits = grover_reg.qubits
    
    circ.g_add_reg(GName.H, grover_qubits)
    
    cz_oracle_gate_controls = grover_reg[:]
    cz_oracle_gate_target = cz_oracle_gate_controls.pop()
    
    circ.g_add(GName.X, grover_reg[flipped_qbit]) 
    """flip qubit #flipped_qbit (default qubit 2 -> 3rd from the top) 
    thus, the result of measurement should be 1111011 as set by the nCZ gate following after this
    """

    circ.c_extend(multi_control_gate_3cx(GName.CZ, cz_oracle_gate_target, cz_oracle_gate_controls))
    
    circ.g_add(GName.X, grover_reg[flipped_qbit]) #flip qubit #flipped_qbit back to stop it from further affecting the circuit

    circ.g_add_reg(GName.H, grover_qubits)
    circ.g_add_reg(GName.X, grover_qubits)

    circ.c_extend(multi_control_gate_3cx(GName.CZ, cz_oracle_gate_target, cz_oracle_gate_controls))

    circ.g_add_reg(GName.X, grover_qubits)
    circ.g_add_reg(GName.H, grover_qubits)
    circ.g_add_reg(GName.MEASUREMENT, grover_qubits)

    return circ

nq = 7
export_qasm(f"Grover_{nq}q.qasm", GroverNq_test(number_of_qubits=nq, flipped_qbit=2))