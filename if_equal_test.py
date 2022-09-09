from naginata import *

def equal_test():
    circ = Circuit()
    
    reg1 = Register(3)
    reg2 = Register(3)
        
    circ.g_add(GName.X, reg1.qubits[1])
    circ.g_add(GName.X, reg1.qubits[2])

    circ.g_add(GName.X, reg2.qubits[1])
    circ.g_add(GName.X, reg2.qubits[2])

    circ.c_extend(if_equal(reg2, reg1))
    
    circ.g_add_reg(GName.MEASUREMENT, reg2)

    return circ

export_qasm("if_equal.qasm", equal_test())