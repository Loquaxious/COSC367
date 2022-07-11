"""
Write a function query(network, query_var, evidence) that given a belief network, the name of a variable in the network, and some evidence, returns the posterior distribution of query_var. The parameter network is a belief network whose data structure was described earlier. The parameter query_var is the name of the variable we are interested in and is of type string. The parameter evidence is a dictionary whose elements are assignments to some variables in the network; the keys are the name of the variables and the values are Boolean.

The function must return a pair of real numbers where the first element is the probability of query_var being false given the evidence and the second element is the probability of query_var being true given the evidence.

Note: Please remember to include the joint probability function (from the previous question) and relevant import statements in your answer.

Hints

This is inference by enumeration. You need to use the joint probability function developed in the previous question. You have to perform the operation once for query_var being true and once for false. You have to sum over all possible values of "hidden" variables. The following gives you the set of hidden variables:

hidden_vars = network.keys() - evidence.keys() - {query_var}

All possible assignments to hidden variables can be obtained by:

for values in itertools.product((True, False), repeat=len(hidden_vars)):
    hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}

Remarks

    When the argument evidence is an empty dictionary we are (semantically) asking for the prior probability of query_var. The algorithm, however, remains the same.
    This algorithm is very close to the mathematical definition of inference over the network and therefore it's easy to understand and implement. However, this is not an efficient algorithm (constant memory, O(n2^n) time). Using factors would be a much more efficient approach (see the textbook). Note that none of the test cases are very large, so for this question it doesn't make a difference what approach is taken.
"""
from itertools import product
def joint_prob(network, assignment):
    p = 1
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
    return p

def query(network, query_var, evidence):
    # Find the hidden variables
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    # Initialise a raw distribution to [0, 0]
    raw_dist = {True: 0, False: 0} 
    assignment = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        # Update the assignment to include the query variable
        assignment[query_var] = query_value
        for values in product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            # Update the assignment (we now have a complete assignment)
            for key, item in hidden_assignments.items():
                assignment[key] = item
            # Update the raw distribution by the probability of the assignment.
            p = joint_prob(network, assignment)
            raw_dist[query_value] += p
    # Normalise the raw distribution and return it
    norm = sum(raw_dist[p] for p in raw_dist)
    for key, p in raw_dist.items():
        raw_dist[key] = p/norm
    return raw_dist


def main():
    print('test 1')
    network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
    }

    answer = query(network, 'A', {})
    print("P(A=true) = {:.5f}".format(answer[True]))
    print("P(A=false) = {:.5f}".format(answer[False]))
    
    print()
    print('test 2')
    
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
 
    answer = query(network, 'B', {'A': False})
    print("P(B=true|A=false) = {:.5f}".format(answer[True]))   
    print("P(B=false|A=false) = {:.5f}".format(answer[False]))
    
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
     
    answer = query(network, 'B', {})
    print("P(B=true) = {:.5f}".format(answer[True]))
    print("P(B=false) = {:.5f}".format(answer[False]))
    
    print()
    print('test 4')
    
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
    
    answer = query(network, 'Burglary', {'John': True, 'Mary': True})
    print("Probability of a burglary when both\n"
          "John and Mary have called: {:.3f}".format(answer[True]))   
    
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
    
    answer = query(network, 'John', {'Mary': True})
    print("Probability of John calling if\n"
          "Mary has called: {:.5f}".format(answer[True]))      

if __name__ == '__main__':
    main()