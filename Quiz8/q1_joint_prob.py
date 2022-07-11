"""
Write a function joint_prob(network, assignment) that given a belief network and a complete assignment of all the variables in the network, returns the probability of the assignment. The data structure of the network is as described above. The assignment is a dictionary where keys are the variable names and the values are either True or False
"""
def joint_prob(network, assignment):
    
    # If you wish you can use the following template
    
    p = 1 # p will enentually hold the value we are interested in
    for var in network:
        if var in assignment:
            a_val = assignment[var]
            belief = network[var]
            p_var = tuple(assignment[i] for i in belief['Parents'])
            if a_val:
                p *= belief['CPT'][p_var]
            else:
                p *= (1- belief['CPT'][p_var])
        else:
            continue
        # Extract the probability of var=true from the network
        # by finding the right assignment for Parents and getting the
        # corresponding CPT. 
        
        # Update p by multiplying it by probablity var=true or var=false
        # depending on how var appears in the given assignment.
    
    return p

def main():
    print('test 1')
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
                }},
    }
    
    p = joint_prob(network, {'A': True})
    print("{:.5f}".format(p))
    
    print()
    print('test 2')
    
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
                }},
    }
    
    p = joint_prob(network, {'A': False})
    print("{:.5f}".format(p))
    
    print()
    print('test 3')
    
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
                }},
                
        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
                }},
        }
     
    p = joint_prob(network, {'A': False, 'B':True})
    print("{:.5f}".format(p)) 
    
    print()
    print('test 4')
    
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
                }},
                
        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
                }},
        }
     
    p = joint_prob(network, {'A': False, 'B':False})
    print("{:.5f}".format(p)) 
    
    print()
    print('test 5')
    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
                }},
                
        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
                }},
        'Alarm': {
            'Parents': ['Burglary','Earthquake'],
            'CPT': {
                (True,True): 0.95,
                (True,False): 0.94,
                (False,True): 0.29,
                (False,False): 0.001,
                }},
    
        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
                }},
    
        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
                }},
        }
    
    p = joint_prob(network, {'John': True, 'Mary': True,
                             'Alarm': True, 'Burglary': False,
                             'Earthquake': False})
    print("{:.8f}".format(p))     

if __name__ == '__main__':
    main()