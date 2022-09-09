from naginata import *

def network_test() -> Circuit:
    """ Manual topology mapping qnn example """

    circ = Circuit()
    oracle_part = Circuit()
    
    weight1 = Register(2)
    weight2 = Register(2)
    weight3 = Register(2)
    input1 = Register(2)
    input2 = Register(2)
    threshold_reg = Register(6)
    i1w1 = Register(4)
    i2w2 = Register(4)
    i2w2_sum_mul_w3 = Register(6)
    grover_regs = []
    grover_qubits = []
    grover_regs.append(weight1)
    grover_regs.append(weight2)
    grover_regs.append(weight3)
    grover_qubits.extend(weight1)
    grover_qubits.extend(weight2)
    grover_qubits.extend(weight3)
    
    circ.g_add_reg(GName.X, input1)
    circ.g_add(GName.X, input2[1])
    
    circ.g_add_reg(GName.X, [threshold_reg[1], threshold_reg[2]])

    circ.g_add_reg(GName.H, grover_qubits)
    
    oracle_part.c_extend(multiplier(input1, weight1, i1w1))
    oracle_part.c_extend(multiplier(input2, weight2, i2w2))
    
    oracle_part.c_extend(adder(i2w2, i1w1))
    
    oracle_part.c_extend(multiplier_asymmetric(i1w1, weight3, i2w2_sum_mul_w3))
    
    oracle_part.c_extend(if_equal(i2w2_sum_mul_w3, threshold_reg))
    
    cz_oracle_gate_controls = i2w2_sum_mul_w3[:]
    cz_oracle_gate_target = cz_oracle_gate_controls.pop()
    
    circ.c_extend(oracle_part)

    circ.c_extend(multi_control_gate_3cx(GName.CZ, cz_oracle_gate_target, cz_oracle_gate_controls))

    circ.c_extend(oracle_part.reverse_non_destr())
    
    circ.g_add_reg(GName.H, grover_qubits)
    circ.g_add_reg(GName.X, grover_qubits)

    grover_reg_copy = grover_qubits[:]
    
    grover_reg_copy_target = grover_reg_copy.pop()

    circ.c_extend(multi_control_gate_3cx(GName.CZ, grover_reg_copy_target, grover_reg_copy))

    circ.g_add_reg(GName.X, grover_qubits)
    circ.g_add_reg(GName.H, grover_qubits)
    circ.g_add_reg(GName.MEASUREMENT, grover_qubits)

    return circ

export_qasm("qnn_static.qasm", network_test())