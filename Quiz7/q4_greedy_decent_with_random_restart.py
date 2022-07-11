"""
Write a procedure greedy_descent_with_random_restart(random_state, neighbours, cost) that takes three functions, one to get a new random state and two to compute the neighbours or cost of a state and then uses greedy_descent (you wrote earlier) to find a solution. The first state in the search must be obtained by calling the function random_state. The procedure must print each state it goes through (including the first and last one) in the order they are encountered. When the search reaches a local minimum that is not global, the procedure must print RESTART and restart the search by calling random_state. Your procedure will be tested only with optimisation versions of CSP problems that have a solution.

Arguments

    random_state: a function that takes no argument and return a random state;
    neighbours: a function that takes a state and returns a list of neighbours;
    cost a function that takes a state returns its cost (e.g. number of conflicts).

Important: You must also provide your implementation of n_queens_neighbours, n_queens_cost, and greedy_descent from previous questions. You do not need to implement random_state; it is implemented in test cases.
"""
def n_queens_neighbours(state):
    states = []
    for i in range(len(state)+1):
        for j in range(i+1, len(state)):
            temp = list(state)
            temp[i], temp[j] = temp[j], temp[i]
            states.append(tuple(temp))
    return sorted(states)


def n_queens_cost(state):
    conflicts = 0
    for i in range(len(state)+1):
        for j in range(i+1, len(state)):
            if abs(state[i] - state[j]) == abs(i - j): 
                conflicts += 1
    return conflicts


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


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    global_min = False
    while not global_min:
        initial_state = random_state()
        states = greedy_descent(initial_state, neighbours, cost)
        for state in states:
            print(state)
            if cost(state) == 0:
                global_min = True
        if not global_min:
            print('RESTART')
        

def main():
    import random
    
    print('test 1')
    N = 6
    random.seed(0)
    
    def random_state():
        return tuple(random.sample(range(1,N+1), N))   
    
    greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)
    
    print()
    print('test 2')
    N = 8
    random.seed(0)
    
    def random_state():
        return tuple(random.sample(range(1,N+1), N))   
    
    greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)    

if __name__ == '__main__':
    main()