"""
Provide an instance of CSP class named cryptic_puzzle that represents the following cryptarithmetic problem:

  two
+ two
------
 four
 
The objective is to find what digit each letter can represent. Each letter is associated to exactly one digit and each digit is associated to up to one letter. The letters on the left (t and f) cannot be zero (if they were they wouldn't be there). This problem is depicted in the lecture notes (as an additional example)

Important: Your solution must also contain the solution to two earlier questions: the functions generate_and_test and arc_consistent.

Notes:

1. If you wish, you can use the code template provided in the answer box.
2. Use lower case letters for variable names.
3. The domains of t, w, o, f, u, and r must be the set of integers from 0 to 9 (inclusive).
4. You need to define some auxiliary variables to take care of the carry overs. In the template provided, these are called c1 and c2.
5. The CSP object must contain a number of constraints describing the given problem. One of the constraints, should require that the variable t, w, o, f, u, r must have different values. One way of implementing this is to use a set. For example, consider what the expression len({a, b}) evaluates to if a and b have the same value.
6. All the constraints in this problem can be added as a number of lambda expression (one line each). A lambda expression evaluates to a function object without a name (an anonymous function). If you think for some of the constraints you need to write more code, you can define a named function outside and then include the name of the function in the set of constraints.
7. The answer must include all the required import statements.
8. Notice that we first make an arc-consistent version of the network (using the function you provide) and then solve the instance using generate-and-test. Without making the network arc-consistent, the generate-and-test algorithm takes a long time (about 30 seconds on a mid-range desktop computer) to find all the solutions. which is not allowed on the server. However, once the network is made arc-consistent, all the solutions can be found in a few seconds.
"""
import itertools, copy 
from csp import scope, satisfies, CSP

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in scope(c)} 
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: 
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c): 
                    new_domain.add(xval) 
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime): 
                        if x != z: 
                            to_do.add((z, cprime))
            csp.var_domains[x] = new_domain
    return csp
    
def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x : v for x, v in zip(names, values)}
        if all(satisfies(assignment, c) for c in csp.constraints):
            yield assignment

domains = {x: set(range(10)) for x in "twofur"}
domains.update({'c1':{0, 1}, 'c2': {0, 1}}) # domains of the carry overs

cryptic_puzzle = CSP(
    var_domains=domains,
    constraints={
        lambda o, r, c1 : o + o == r + 10 * c1, 
        lambda w, u, c1, c2 : w + w + c1 == u + 10 * c2,
        lambda t, o, c2 : t + t + c2 == o + 10,
        lambda f : f == 1,
        lambda t, w, o, f, u, r : len({t, w, o, f, u, r}) > 5,
        })

def main():
    
    print("test 1")
    print()
    
    print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
    print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twour")) 
    
    print()
    print('test 2')
    print()
    
    new_csp = arc_consistent(cryptic_puzzle)
    print(sorted(new_csp.var_domains['r']))    

    print()
    print('test 3')
    print()
    
    new_csp = arc_consistent(cryptic_puzzle)
    print(sorted(new_csp.var_domains['w']))
    
    print()
    print('test 4')
    print()    
    
    new_csp = arc_consistent(cryptic_puzzle)
    solutions = []
    for solution in generate_and_test(new_csp):
        solutions.append(sorted((x, v) for x, v in solution.items()
                                if x in "twofur"))
    print(len(solutions))
    solutions.sort()
    print(solutions[0])
    print(solutions[5])    

if __name__ == "__main__":
    main()