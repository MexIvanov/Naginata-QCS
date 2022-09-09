from naginata import *

""" QNN Generation tests """

def run_test_1():
    """ Test 1: 2 input neurons -> 1 hidden neuron -> 1 Output neuron """
    
    input_to_hidden_bindins = [
        # Connections between Input and Hidden neurons
        {'Hidden': 0, 'Input': 0, 'Input_value': [1, 1]},
        {'Hidden': 0, 'Input': 1, 'Input_value': [1, 0]},
    ]

    hidden_to_output_bindins = [
        # Connections between Hidden and Output neurons
        {'Hidden': 0, 'Output': 0},
    ]

    export_qasm("qnn_test1.qasm", build_param_network(input_to_hidden_bindins,
                hidden_to_output_bindins, 2, [0, 0, 0, 1, 1, 0]))


def run_test_2():
    """ Test 2: 1 input neuron -> 2 hidden neurons -> 1 Output neuron; Threshold value 000110 """
    
    input_to_hidden_bindins = [
        # Connections between Input and Hidden neurons
        {'Hidden': 0, 'Input': 0, 'Input_value': [1, 1]},
        {'Hidden': 1, 'Input': 0, 'Input_value': [1, 1]},
    ]

    hidden_to_output_bindins = [
        # Connections between Hidden and Output neurons
        {'Hidden': 0, 'Output': 0},
        {'Hidden': 1, 'Output': 0},
    ]
    
    export_qasm("qnn_test2.qasm", build_param_network(input_to_hidden_bindins,
                hidden_to_output_bindins, 2, [0, 0, 0, 1, 1, 0]))


def run_test_3():
    """ Test 3: 2 input neurons -> 2 hidden neurons (1 per input) -> 1 Output neuron """
    
    input_to_hidden_bindins = [
        # Connections between Input and Hidden neurons
        {'Hidden': 0, 'Input': 0, 'Input_value': [1, 1]},
        {'Hidden': 1, 'Input': 1, 'Input_value': [1, 0]},
    ]

    hidden_to_output_bindins = [
        # Connections between Hidden and Output neurons
        {'Hidden': 0, 'Output': 0},
        {'Hidden': 1, 'Output': 0},
    ]

    export_qasm("qnn_test3.qasm", build_param_network(input_to_hidden_bindins,
                hidden_to_output_bindins, 2, [0, 1, 0, 1, 1, 0]))


#run a test
run_test_1()
run_test_2()
run_test_3()
