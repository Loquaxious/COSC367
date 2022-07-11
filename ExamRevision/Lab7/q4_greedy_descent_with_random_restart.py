import random

def n_queens_neighbours(state):
    neighbours = []
    memo = {state}
    for i in range(len(state)):
        for j in range(len(state)):
            if i == j:
                continue
            
            lst_state = list(state)
            lst_state[i], lst_state[j] = lst_state[j], lst_state[i]
            new_state = tuple(lst_state)
            
            if new_state in memo:
                continue
            else:
                memo.add(new_state)
                neighbours.append(new_state)
    return sorted(neighbours)


def n_queens_cost(state):
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range((i + 1), n):
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost 

def greedy_descent(initial_state, neighbours, cost):
    states = [initial_state]
    state = initial_state
    while True:
        try:
            cst, nbr = min(((cost(x), x) for x in neighbours(state)), key=lambda i : i[0])
        except ValueError:
            break
        if cst < cost(state):
            state = nbr
            states.append(nbr)
        else:
            break
    return states


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    state = random_state()
    global_min = cost(state)
    
    while True:
        descent_states = greedy_descent(state, neighbours, cost)
        for state in descent_states:
            print(state)
        global_min = cost(descent_states[-1])
        if global_min <= 0:
            break
        print('RESTART')
        state = random_state()
    


def main():
    N = 6
    random.seed(0)
    
    def random_state():
        return tuple(random.sample(range(1,N+1), N))   
    
    greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)
    
    print()
    
    N = 8
    random.seed(0)
    
    def random_state():
        return tuple(random.sample(range(1,N+1), N))   
    
    greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost) 
    
    print()
    N = 1
    random.seed(0)
    
    def random_state():
        return tuple(random.sample(range(1,N+1), N))
    
    greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)    

if __name__ == '__main__':
    main()