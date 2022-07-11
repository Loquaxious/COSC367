from itertools import product

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


def query(network, query_var, evidence):
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    raw_dist = {True : 0, False : 0}
    assignment = dict(evidence)
    for query_value in {True, False}:
        assignment[query_var] = query_value
        for values in product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            for key, value in hidden_assignments.items():
                assignment[key] = value
            p = joint_prob(network, assignment)
            raw_dist[query_value] += p
            print(assignment)
            print(p)
    norm = sum(raw_dist[p] for p in raw_dist)
    for key, p in raw_dist.items():
        raw_dist[key] = p/norm
    print(raw_dist)
    return raw_dist

network = {
    'Disease' : {
        'Parents' : [],
        'CPT' : {
            () : 1/100000
            }
        },
    
    'Test' : {
        'Parents' : ['Disease'],
        'CPT' : {
            (True,) : 0.99,
            (False,) : 0.01
            }
        }
    }


def main():
    answer = query(network, 'Disease', {'Test': True})
    print("The probability of having the disease\n"
          "if the test comes back positive: {:.8f}"
          .format(answer[True]))
    
    answer = query(network, 'Disease', {'Test': False})
    print("The probability of having the disease\n"
          "if the test comes back negative: {:.8f}"
          .format(answer[True]))
    
if __name__ == '__main__':
    main()