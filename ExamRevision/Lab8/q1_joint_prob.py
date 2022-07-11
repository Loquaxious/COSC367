def joint_prob(network, assignment):
    p = 1 # p will enentually hold the value we are interested in
    for var in network:
        if var in assignment:
            parents = network[var]['Parents']
            cpt = network[var]['CPT']
            p_var = tuple(assignment[i] for i in parents)
            
            if assignment[var]:
                p *= cpt[p_var]
            else:
                p *= 1- cpt[p_var]
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
    p = joint_prob(network, {'A': False, 'B':True})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': True, 'B':False})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': True, 'B':True})
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