"""
Write a function greedy_descent(initial_state, neighbours, cost) that takes an initial state and two functions to compute the neighbours and cost of a state, and then iteratively improves the state until a local minimum (which may be global) is reached. The function must return the list of states it goes through (including the first and last one) in the order they are encountered. The algorithm should move to a new state only if the cost improves. If there is a tie between multiple states, the first one (in the order they appear in the sequence returned by neighbours) must be used.

Arguments

    - initial_state: the state from which the search starts
    - neighbours: a function that takes a state and returns a list of neighbours
    - cost a function that takes a state returns its cost (e.g. number of conflicts).

Notes

    - consider using the min function in Python.
    - you do not need to provide any other function or code.
"""
def greedy_descent(initial_state, neighbours, cost):
    states = [initial_state]
    current = (cost(initial_state), initial_state)
    previous = None
    while current != previous:      
        previous = current
        current_neighbours = [(cost(i), i) for i in neighbours(current[1])]
        if len(current_neighbours) == 0:
            break
        else:
            min_neighbour = min(current_neighbours, key=lambda x: x[0])
            if current[0] > min_neighbour[0]:
                states.append(min_neighbour[1])
                current = min_neighbour         
        
    return states

def main():
    print()
    print('test 1')    
    def cost(x):
        return x**2
    
    def neighbours(x):
        return [x - 1, x + 1]
    
    for state in greedy_descent(4, neighbours, cost):
        print(state)
    
    print()
    print('test 2')
    def cost(x):
        return x**2
    
    def neighbours(x):
        return [x - 1, x + 1]
    
    for state in greedy_descent(-6.75, neighbours, cost):
        print(state)
        
    print()
    print('test 3')
    def cost(x):
        return -x**2
    
    def neighbours(x):
        return [x - 1, x + 1] if abs(x) < 5 else []
    
    for state in greedy_descent(0, neighbours, cost):
        print(state)    

if __name__ == '__main__':
    main()