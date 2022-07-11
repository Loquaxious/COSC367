"""
Consider a medical test for a certain disease that is very rare, striking only 1 in 100,000 people. Suppose the probability of testing positive if the person has the disease is 99%, as is the probability of testing negative when the person does not have the disease.

Express these facts in the form of a (causal) belief network. Use variable names 'Disease' and 'Test'. Assign the network to the variable network.

Important: Supply the query function and all the functions and modules it depends on (e.g. joint_prob) from the previous questions.

Comment: After solving the problem, you may find the value of P(having disease| positive test), which is essentially the precision of the test, counter-intuitive; one may expect this value to be much higher. Observe that the probability of returning positive regardless of the disease is about 1%, which is quite high compared to how rare the disease is. A good test for this rare disease must have a much higher specificity, which is the probability of returning negative when the person does not have the disease. You can explore this by changing the values in the CPTs (more specifically, making the value corresponding to Disease being False in the CPT of Test smaller). 
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
    'Disease': {
        'Parents': [],
        'CPT': {
            (): 1/100000,
            }},
    'Test': {
        'Parents': ['Disease'],
        'CPT': {
            (True,) : 0.99,
            (False,): 0.01
            }}
    }


def main():
    print('test 1')
    answer = query(network, 'Disease', {'Test': True})
    print("The probability of having the disease\n"
          "if the test comes back positive: {:.8f}"
          .format(answer[True]))
    
    print()
    print('test 2')
    answer = query(network, 'Disease', {'Test': False})
    print("The probability of having the disease\n"
          "if the test comes back negative: {:.8f}"
          .format(answer[True]))

if __name__ == '__main__':
    main()