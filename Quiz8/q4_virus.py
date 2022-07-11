"""
Consider two medical tests, A and B, for a virus. Test A is 95% effective at recognising the virus when the virus is present, but has a 10% false positive rate (indicating that the virus is present, when it is not). Test B is 90% effective at recognizing the virus, but has a 5% false positive rate. The two tests use independent methods of identifying the virus. The virus is carried by 1% of all people.

Express these facts in the form of a (causal) belief network. Use variable names 'A',  'B', and 'Virus'. Assign the network to the variable network.

Important: Supply the query function and all the functions and modules it depends on (e.g. joint_prob) from the previous questions. 
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
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    raw_dist = {True: 0, False: 0} 
    assignment = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        assignment[query_var] = query_value
        for values in product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            for key, item in hidden_assignments.items():
                assignment[key] = item
            p = joint_prob(network, assignment)
            raw_dist[query_value] += p
    norm = sum(raw_dist[p] for p in raw_dist)
    for key, p in raw_dist.items():
        raw_dist[key] = p/norm
    return raw_dist

network = {
    'Virus': {
        'Parents': [],
        'CPT': {
            (): 0.01
            }},
    'A': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.95,
            (False,): 0.1
            }},
    'B': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05
            }}        
    }


def main():
    print('test 1')
    answer = query(network, 'Virus', {'A': True})
    print("The probability of carrying the virus\n"
          "if test A is positive: {:.5f}"
          .format(answer[True]))
    
    print()
    print('test 2')
    answer = query(network, 'Virus', {'B': True})
    print("The probability of carrying the virus\n"
          "if test B is positive: {:.5f}"
          .format(answer[True]))

if __name__ == '__main__':
    main()