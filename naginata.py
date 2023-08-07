
""" Naginata Quantum Circuit Synthesizer 
by Cesar Pronin (MexIvanov)

"""

from enum import Enum, auto
from typing_extensions import Self
import logging as log


NO_LOGGING = 3
DEBUG_MODE = 2
DEBUG_QASM = 1

""" Setting Logging levels in log.basicConfig:
    DEBUG_MODE -> print the inputs/outputs of custom gates
    DEBUG_QASM -> also print generated QASM code to terminal
    NO_LOGGING -> Disable synthesis logging
"""

log.basicConfig(level=DEBUG_MODE, format="")


class GName(Enum):
    """ Gate name Enum 
    *_dag suffix depicts "dagger" gates
    """

    X = "x"
    Y = "y"
    Z = "z"
    H = "h"
    C = "c"
    CZ = "cz"
    CX = "cx"
    CCX = "ccx"
    CCCX = "cccx"
    CT = "cp(pi/4)"
    CT_dag = "cp(-pi/4)"
    MEASUREMENT = "measure"
    SWAP = "swap"
    CSWAP = "cswap"


class Register:
    """ Describes a Quantum Register that can represend a list of qubits used for a single purpose,
        i.e. storing a numeric value (acting like a variable)
    """

    last_qubit_index = -1

    def __init__(self, n_qubits):  # specify qubit depth
        """Creates a new register of N qubits by allocating new Qubits."""

        self.qubits = []

        for qb in range(Register.last_qubit_index + 1, Register.last_qubit_index + n_qubits + 1):
            self.qubits.append(Qubit(qb))

        Register.last_qubit_index = Register.last_qubit_index + n_qubits

    def __str__(self):
        return str(self.qubits)

    def __repr__(self):
        return self.qubits

    def __iter__(self):
        return iter(self.qubits)
    
    def __len__(self):
        return len(self.qubits)

    def __getitem__(self, obj):
        return self.qubits[obj]

    def form(self, source_qubits):
        """ Forms a register from a qubit index or list of indexes. 
        Returns the register 
        """

        if type(source_qubits) == list:
            for qb in source_qubits:
                self.qubits.append(Qubit(qb))

        else:
            self.qubits.append(Qubit(source_qubits))

        return self


class Qubit:
    """ Describes a Qubit as an indexer for each target/control in a Gate class element. 
        A Qubit can be an ancilla (used only as a reusable buffer for some calculations).
        In this case all gates acting on it must be reversed after the calculation is performed.
        
        Ancilla qubits have their own indexes that get added to the last index of a circuit, after 
        Circuit().plot_ancilla function is called
    """

    def __init__(self, index, is_ancilla=False):
        self.index = index
        self.is_ancilla = is_ancilla

    def __str__(self) -> str:
        return str(self.index)

    def __repr__(self) -> str:
        return str(self.index)

    def qlist(index_list, is_ancilla=False) -> list:
        if type(index_list) == list:
            qubit_list = []

            for idx in index_list:
                if is_ancilla:
                    qubit_list.append(Qubit(idx, is_ancilla=True))
                
                else:
                    qubit_list.append(Qubit(idx))

            return qubit_list


class Gate:
    """ Describes a Quantum Gate - logic element that has a name,
        target qubits it acts on, and
        control qubits that control the action perfomed on targets.
    """

    def __init__(self, name, targets=[], controls=[]):
        self.name = name
        self.targets = targets
        self.controls = controls

    def __str__(self) -> str:
        return str(self)


class Measurement:
    """ Describes a Measurement perfomed at the end of a quantum circuit
        Maps specified qubits to specified classic bits, that will hold
        the output values of the quantum circuit
    """

    def __init__(self, qubit, classic_bit):
        self.qubit = qubit
        self.classic_bit = classic_bit

    def __str__(self) -> str:
        return str(self)


class Circuit:
    """ Describes a Quantum Circuit, 
        which can be extended with gates or another circuit
    """

    def __init__(self):
        self.gates_list = []
        self.measurement_list = []
        self.max_non_ancilla = 0

    def __str__(self) -> str:
        return str(self.gates_list)

    def g_add(self, name, targets=[], controls=[]):
        """ Adds a specified gate to the circuit """

        if name == GName.CCCX:
            self.c_extend(Toffoli_4q(targets, controls))
            return

        if name == GName.MEASUREMENT:
            if controls == []:
                self.measurement_list.append(Measurement(targets, targets))
                return

            self.measurement_list.append(Measurement(targets, controls))
            return

        new_gate = Gate(name, targets, controls)
        self.gates_list.append(new_gate)

        return new_gate

    def g_add_reg(self, name, targets=[]):
        """ Adds a specified single-qubit gate to each target """

        name: GName
        for target in targets:
            self.g_add(name, target)

    def reverse(self):
        """ Replaces the current circuit with its reversed counterpart """

        self.gates_list = reversed(self.gates_list)

    def reverse_non_destr(self):
        """ Returns the reversed circuit, without replacing the current """
        
        rev_circ = Circuit()
        rev_circ.gates_list = list(reversed(self.gates_list))
        return rev_circ

    def c_extend(self, circuit):
        self.gates_list.extend(circuit.gates_list)

    def plot_ancilla(self) -> Self:
        """ Places ancilla qubit indexes to the end of the circuit """
        
        anc_shift = self.get_max_non_ancilla() + 1

        gate: Gate
        for gate in self.gates_list:
            
            target: Qubit
            for target in gen_to_list(gate.targets):
                if target.is_ancilla:
                    target.index += anc_shift
                    target.is_ancilla = False

            control: Qubit
            for control in gen_to_list(gate.controls):
                if control.is_ancilla:
                    control.index += anc_shift
                    control.is_ancilla = False

        return self

    def get_max_non_ancilla(self) -> int:
        """ Gets the maximum used qubit index """

        gate: Gate
        for gate in self.gates_list:
            target: Qubit
            for target in gen_to_list(gate.targets):
                if not target.is_ancilla and (target.index > self.max_non_ancilla):
                    self.max_non_ancilla = target.index

            control: Qubit
            for control in gen_to_list(gate.controls):
                if not control.is_ancilla and (control.index > self.max_non_ancilla):
                    self.max_non_ancilla = control.index

        return self.max_non_ancilla


def gen_to_list(obj):
    if type(obj) != list:
        return [obj]

    return obj


""" Custom gates section """

def Toffoli_4q(target, controls) -> Circuit:
    """ Qiskit 'mct' gate with 3 controls (CCCX)
    or 4 qubit Toffoli gate
    """

    circ = Circuit()
    circ.g_add(GName.H, targets=target)
    circ.g_add(GName.CT_dag, targets=target, controls=controls[0])
    circ.g_add(GName.CX, targets=controls[1], controls=controls[0])
    circ.g_add(GName.CT, targets=target, controls=controls[1])
    circ.g_add(GName.CX, targets=controls[1], controls=controls[0])
    circ.g_add(GName.CT_dag, targets=target, controls=controls[1])
    circ.g_add(GName.CX, targets=controls[2], controls=controls[1])
    circ.g_add(GName.CT, targets=target, controls=controls[2])
    circ.g_add(GName.CX, targets=controls[2], controls=controls[0])
    circ.g_add(GName.CT_dag, targets=target, controls=controls[2])
    circ.g_add(GName.CX, targets=controls[2], controls=controls[1])
    circ.g_add(GName.CT, targets=target, controls=controls[2])
    circ.g_add(GName.CX, targets=controls[2], controls=controls[0])
    circ.g_add(GName.CT_dag, targets=target, controls=controls[2])
    circ.g_add(GName.H, targets=target)

    return circ


def multi_target_gate(gate, targets, control, qreverse=False) -> Circuit:
    """ On multiple target qubits creates a gate, 
    controlled by same control qubit(s). 
    """

    circ = Circuit()
    for qb in targets:
        circ.g_add(gate, targets=qb, controls=control)

    if qreverse:
        circ.reverse()

    return circ


def if_equal(targets, ctrls, qreverse=False) -> Circuit:
    """ Compares target and control qubits. Result is written to target qubits """
    
    log.log(level=DEBUG_MODE, msg=f"If_Equal Targets: {targets}; Controls: {ctrls}")

    circ = Circuit()

    for idx, target in enumerate(targets):
        circ.g_add(GName.CX, target, ctrls[idx])
        circ.g_add(GName.X, target)

    if qreverse:
        circ.reverse()

    return circ


def multi_control_gate_3cx(gate, target, ctrls) -> Circuit:
    """ Multi (N) controlled gate that is created by stacking
    Qiskit 'mct' gates with 3 controls (CCCX) Toffoli gates
    gate can be specified as GName.CX, CY, CZ ...
    """

    log.log(level=DEBUG_MODE, msg=f"multi_control_gate_3cx Gate: {gate}; Targets: {target}; Controls: {ctrls}")

    addBits = len(ctrls)
    circ = Circuit()
    circ.g_add(GName.CCCX, targets=Qubit(0, is_ancilla=True),
               controls=[ctrls[0], ctrls[1], ctrls[2]])

    delta = 0
    for ct in range(3, addBits, 2):
        if delta == 0:
            try:
                circ.g_add(GName.CCCX, targets=Qubit(1, is_ancilla=True), controls=[
                        ctrls[ct], ctrls[ct + 1], Qubit(0, is_ancilla=True)])
            except:
                circ.g_add(GName.CCX, targets=Qubit(1, is_ancilla=True), controls=[
                        ctrls[ct], Qubit(0, is_ancilla=True)])

        else:
            try:
                circ.g_add(GName.CCCX, targets=Qubit(1 + delta, is_ancilla=True),
                           controls=[ctrls[ct], ctrls[ct + 1], Qubit(delta, is_ancilla=True)])

            except:
                circ.g_add(GName.CCX, targets=Qubit(1 + delta, is_ancilla=True),
                           controls=[ctrls[ct], Qubit(delta, is_ancilla=True)])

        delta += 1

    rev_circ = circ.reverse_non_destr()

    circ.g_add(gate, targets=target, controls=Qubit(delta, is_ancilla=True))

    circ.c_extend(rev_circ)

    return circ


def adder(sum1_nq, res_nq, qreverse=False) -> Circuit:
    """ Parametric Quantum Adder 
    based on an example in Craig Gidney's "Quirk" Quantum Simulator
    """
    
    log.log(level=DEBUG_MODE, msg=f"Adder on qubits: {sum1_nq} + {res_nq}; result on qubits: {res_nq}")
    
    circ = Circuit()

    sum1_len = len(sum1_nq)
    res1_len = len(res_nq)

    if sum1_len != res1_len:
        return print("Error: a same amount of qubits has to be alocated to sum1 and res1 ")

    if sum1_len < 2:
        return print("Error: there has to be 2 or more qubits allocated to sum1 and res1 ")

    sum1_last = sum1_len - 1

    #all_non_ctrl - stores all qubits, excluding the center control qubit
    all_non_ctrl = sum1_nq[:]
    all_non_ctrl.pop(sum1_last)
    all_non_ctrl.extend(res_nq)

    circ.c_extend(multi_target_gate(
        GName.CX, all_non_ctrl, sum1_nq[sum1_last]))

    for i in range(sum1_last):
        circ.g_add(GName.CX, targets=res_nq[i], controls=sum1_nq[sum1_last])
        circ.g_add(GName.CSWAP, targets=[
                   sum1_nq[i], sum1_nq[sum1_last]], controls=res_nq[i])

    # center
    circ.g_add(
        GName.CX, targets=res_nq[sum1_last], controls=sum1_nq[sum1_last])
    
    for i in reversed(range(sum1_last)):
        circ.g_add(GName.CSWAP, targets=[
                   sum1_nq[i], sum1_nq[sum1_last]], controls=res_nq[i])
        circ.g_add(GName.CX, targets=res_nq[i], controls=sum1_nq[i])

    circ.c_extend(multi_target_gate(
        GName.CX, all_non_ctrl, sum1_nq[sum1_last], qreverse=True))

    if qreverse:
        circ.reverse()

    return circ


def multiplier(m1_reg, m2_reg, res_reg, qreverse=False) -> Circuit:
    """ Parametric Quantum Multiplier.
    Based on classic long multiplication combined with quantum adders
    """

    log.log(level=DEBUG_MODE, msg=f"Multiplier on qubits: {m1_reg} * {m2_reg}; result on qubits: {res_reg}")

    circ = Circuit()

    m1_len = len(m1_reg) - 1
    for m2_idx, m2_qubit in enumerate(m2_reg):
        for m1_idx, m1_qubit in enumerate(m1_reg):
            circ.g_add(GName.CCX, targets=Qubit(
                m1_idx, is_ancilla=True), controls=[m1_qubit, m2_qubit])

        addToReg = []
        for i in range(m2_idx, m2_idx + len(m2_reg) + 1):
            addToReg.append(res_reg[i])

        circ.c_extend(adder(Qubit.qlist(
            list(range(len(m1_reg) + 1)), is_ancilla=True), addToReg))

        for m1_idx, m1_qubit in enumerate(reversed(m1_reg)):
            circ.g_add(GName.CCX, targets=Qubit(m1_len - m1_idx,
                       is_ancilla=True), controls=[m1_qubit, m2_qubit])

    if qreverse:
        circ.reverse()
            
    return circ


def multiplier_asymmetric(m1_reg, m2_reg, res_reg, qreverse=False):
    """ Parametric Quantum Multiplier. With registers of different length
    Based on classic long multiplication combined with quantum adders
    """

    log.log(level=DEBUG_MODE, msg=f"Multiplier on qubits: {m1_reg} * {m2_reg}; result on qubits: {res_reg}")

    if len(res_reg) < len(m1_reg) + len(m2_reg):
        return print("Error: resulting register too small for multiplication!")

    circ = Circuit()

    m1_len = len(m1_reg) - 1
    for m2_idx, m2_qubit in enumerate(m2_reg):
        for m1_idx, m1_qubit in enumerate(m1_reg):
            circ.g_add(GName.CCX, targets=Qubit(
                m1_idx, is_ancilla=True), controls=[m1_qubit, m2_qubit])

        addToReg = []
        for i in range(m2_idx, len(res_reg) - (len(m2_reg) - m2_idx - 1)):
            addToReg.append(res_reg[i])

        circ.c_extend(adder(Qubit.qlist(
            list(range(len(m1_reg) + 1)), is_ancilla=True), addToReg))

        for m1_idx, m1_qubit in enumerate(reversed(m1_reg)):
            circ.g_add(GName.CCX, targets=Qubit(m1_len - m1_idx,
                       is_ancilla=True), controls=[m1_qubit, m2_qubit])

    if qreverse:
        circ.reverse()

    return circ


""" Utilities """

def print_circ(circuit=Circuit()):
    """ Prints a circuit to terminal """

    print(str("OPENQASM 2.0;\n" + "include \"qelib1.inc\";\n" + "qreg q[" + str(
        circuit.get_max_non_ancilla() + 1) + "];\n" + "creg c[" + str(len(circuit.measurement_list)) + "];\n"))

    gate: Gate
    for gate in circuit.gates_list:
        gate_lst = []

        if type(gate.controls) == list:
            for qubit in gate.controls:
                gate_lst.append(f"q[{qubit.index}]")
        else:
            gate_lst.append(f"q[{gate.controls}]")

        if type(gate.targets) == list:
            for qubit in gate.targets:
                gate_lst.append(f"q[{qubit.index}]")
        else:
            gate_lst.append(f"q[{gate.targets}]")

        separator = ", "
        gate_str = separator.join(gate_lst)
        print(f"{gate.name.value} {gate_str};")

    mes: Measurement
    for mes in circuit.measurement_list:
        print(f"measure q[{mes.qubit}] -> c[{mes.classic_bit}];")


def export_qasm(filename, circuit=Circuit()):
    """ Prints a circuit to circuit.qasm text file and terminal """
    circuit.plot_ancilla()

    header = str("OPENQASM 2.0;\n" + "include \"qelib1.inc\";\n" + "qreg q[" + str(
        circuit.get_max_non_ancilla() + 1) + "];\n" 
        + "creg c[" + str(len(circuit.measurement_list)) + "];\n")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(header + "\n")

    log.log(level=DEBUG_QASM, msg=header)

    gate: Gate
    for gate in circuit.gates_list:
        gate_lst = []

        if type(gate.controls) == list:
            for qubit in gate.controls:
                gate_lst.append(f"q[{qubit.index}]")
        else:
            gate_lst.append(f"q[{gate.controls}]")

        if type(gate.targets) == list:
            for qubit in gate.targets:
                gate_lst.append(f"q[{qubit.index}]")
        else:
            gate_lst.append(f"q[{gate.targets}]")

        separator = ", "
        gate_str = separator.join(gate_lst)
        write_qasm(filename, f"{gate.name.value} {gate_str};")

    mes: Measurement
    for mes in circuit.measurement_list:
        write_qasm(filename, f"measure q[{mes.qubit}] -> c[{mes.classic_bit}];")
    
    Register.last_qubit_index = -1


def write_qasm(filename, line):
    """ Writes a line to circuit.qasm """
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(line + "\n")

        log.log(level=DEBUG_QASM, msg=line)


""" Quantum Neural Network synthesis related section """

def build_param_network(input_to_hidden_binds, hidden_to_output_bindins, input_reg_size, threshold_value):
    circ = Circuit()
    oracle_part = Circuit()

    """ Allocate quantum registers based on inputted network definition """
    
    # Registers that hold the "body" of Grover's algorithm. 
    # They will store our results in the end of the algorithm.
    grover_regs = []
    
    # Create weight registers for splines connecting input and hidden neurons
    for i_bind in input_to_hidden_binds:
        hidden_id = i_bind['Hidden']
        new_weight_register = Register(input_reg_size)
        i_bind['I->H_Weight'] = new_weight_register
        grover_regs.append(new_weight_register)

    # Create weight registers for splines connecting output and hidden neurons
    for o_bind in hidden_to_output_bindins:
        hidden_id = o_bind['Hidden']
        new_register = Register(input_reg_size)
        o_bind['H->O_Weight'] = new_register
        grover_regs.append(new_register)

    # Create input value registers
    for i_bind in input_to_hidden_binds:
        created_input_regs = [bind for bind in input_to_hidden_binds if (bind['Input'] == i_bind['Input']) and ('Input_reg' in bind)]
        
        if not created_input_regs:
            new_input_register = Register(input_reg_size)
            i_bind['Input_reg'] = new_input_register
            # Add input values to the circuit as X gates for 1's
            # Reversed to keep qubit order (top -> bottom) = (lowest -> highest)
            for qubit_idx, qubit in enumerate(reversed(new_input_register)):
                val_list = i_bind['Input_value']
                
                if val_list[qubit_idx] == 1:
                    circ.g_add(GName.X, qubit)
        
        else:
            # If the register is already created for this input's value -> 
            #  bind to it, instead of creating a new one
            new_input_register = created_input_regs[0]['Input_reg']
            i_bind['Input_reg'] = new_input_register

    reg: Register
    grover_qubits = []
    for reg in grover_regs:
        grover_qubits.extend(reg)

    # Create a register for threshold value
    threshold_register = Register(len(threshold_value))
    # Add the threshold value to the circuit as X gates for 1's
    # Reversed to keep qubit order (top -> bottom) = (lowest -> highest)
    for qubit_idx, qubit in enumerate(reversed(threshold_register)):
        if threshold_value[qubit_idx] == 1:
            circ.g_add(GName.X, qubit)

    # Create registers for storing Input*Weight(to input) multiplication results
    current_hidden_id = -1
    current_res_reg = -1

    for i_bind in input_to_hidden_binds:
        hidden_id = i_bind['Hidden']
        new_register = Register(input_reg_size * 2)
        i_bind['IxW'] = new_register
        
        # Pick first multiplication result register (per hidden neuron) to hold the sum of weights
        if hidden_id > current_hidden_id:
            current_res_reg = new_register
            current_hidden_id = hidden_id
        
        i_bind['IxW_Sum'] = current_res_reg

    # Create registers for storing IxW_Sum*Weight(to output) values
    current_output_id = -1
    current_res_reg = -1

    for o_bind in hidden_to_output_bindins:
        output_id = o_bind['Output']

        # This register size is for the asymmetric multiplication variant is:
        #  len(mul1) + len(mul2) == len(result)
        new_register = Register(input_reg_size + input_reg_size * 2)

        o_bind['HxWo'] = new_register

        # Pick first multiplication result register (per output neuron)
        #  to hold the sum of weights
        if output_id > current_output_id:
            current_res_reg = new_register
            current_output_id = hidden_id
        o_bind['HxWo_Sum'] = current_res_reg

    """ Generate circuit based on previous register allocations """
    
    """ Apply hadamard transform (1st part of Grover's algorithm) """
    circ.g_add_reg(GName.H, grover_qubits)

    """ Build the Oracle function along with a NCZ gate (2nd part of Grover's algorithm) """
    
    # Multiply all I*W(input)
    for i_bind in input_to_hidden_binds:
        oracle_part.c_extend(multiplier(
            i_bind['Input_reg'], i_bind['I->H_Weight'], i_bind['IxW']))
    
    # Sum those /\ I*W(input) into the first multiplication result register
    for i_bind in input_to_hidden_binds:
        if (i_bind['IxW'] != i_bind['IxW_Sum']):
            oracle_part.c_extend(adder(
                i_bind['IxW'], i_bind['IxW_Sum']))
    
    # Multiply all H*W(output)
    for o_bind in hidden_to_output_bindins:
        o_h_bind = [bind for bind in input_to_hidden_binds if bind['Hidden'] == o_bind['Hidden']][0]
        oracle_part.c_extend(multiplier_asymmetric(
            o_h_bind['IxW_Sum'], o_bind['H->O_Weight'], o_bind['HxWo']))
        
    # Sum those /\ H*W(output) into the first multiplication result register    
    for o_bind in hidden_to_output_bindins:
        if (o_bind['HxWo'] != o_bind['HxWo_Sum']):
            oracle_part.c_extend(adder(
                o_bind['HxWo'], o_bind['HxWo_Sum']))
    
    # Check if the final /\ HxWo_Sum equals the output threshold value
    cz_oracle_gate_controls = []
    for o_bind in hidden_to_output_bindins:
        target: Register
        target = o_bind['HxWo_Sum']
        if (o_bind['HxWo'] == o_bind['HxWo_Sum']):
            oracle_part.c_extend(
                if_equal(target, threshold_register))
        
        cz_oracle_gate_controls.extend(target)

    circ.c_extend(oracle_part)

    cz_oracle_gate_target = cz_oracle_gate_controls.pop()

    circ.c_extend(multi_control_gate_3cx(
        GName.CZ, cz_oracle_gate_target, cz_oracle_gate_controls))

    circ.c_extend(oracle_part.reverse_non_destr())

    """ Add 3rd Grover's algorithm step - amplitude amplification """
    circ.g_add_reg(GName.H, grover_qubits)
    circ.g_add_reg(GName.X, grover_qubits)

    grover_reg_copy = grover_qubits[:]
    grover_reg_copy_target = grover_reg_copy.pop()

    circ.c_extend(multi_control_gate_3cx(
        GName.CZ, grover_reg_copy_target, grover_reg_copy))

    circ.g_add_reg(GName.X, grover_qubits)
    circ.g_add_reg(GName.H, grover_qubits)
    circ.g_add_reg(GName.MEASUREMENT, grover_qubits)

    return circ

