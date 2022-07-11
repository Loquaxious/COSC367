"""
Suppose we want to predict the value of variable Y based on the values of variables X1, X2, and X3. Assuming that we want to use a Naive Bayes model for this purpose, create a belief net for the model called network. The probabilities must be learnt by using the dataset given below. Use Laplacian smoothing with a pseudocount of 2.

X1	X2	X3	Y 
T	T	F	F
T	F	F	F
T	T	F	F
T	F	F	T
F	F	F	T
F	T	F	T
F	F	F	T
Notes
Node names are case sensitive.
Since we are using Python syntax, you can use fraction expressions if you wish. For example you can use 3/4 or even (2+1)/(2+1+0+1) which will be evaluated at runtime.
"""
network = {
    'X1': {
        'Parents': ['Y'],
        'CPT': {
            (True,): 3/8,
            (False,): 5/7,
            }
        },
    'X2': {
        'Parents': ['Y'],
        'CPT': {
            (True,): 3/8,
            (False,): 4/7,
            }
        },
    'X3': {
        'Parents': ['Y'],
        'CPT': {
            (True,): 2/8,
            (False,): 2/7,
            }
        },
    'Y': {
        'Parents': [],
        'CPT': {
            (): 6/11,
            }
        }}  

def main():
    from numbers import Number
    # Checking the overall type-correctness of the network
    # without checking anything question-specific
    
    assert type(network) is dict
    for node_name, node_info in network.items():
        assert type(node_name) is str
        assert type(node_info) is dict
        assert set(node_info.keys()) == {'Parents', 'CPT'}
        assert type(node_info['Parents']) is list
        assert all(type(s) is str for s in node_info['Parents'])
        for assignment, prob in node_info['CPT'].items():
            assert type(assignment) is tuple
            assert isinstance(prob, Number)
    
    print("OK")

if __name__ == "__main__":
    main()