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

def main():
    
    def cost(x):
        return x**2
    
    def neighbours(x):
        return [x - 1, x + 1]
    
    for state in greedy_descent(4, neighbours, cost):
        print(state)    
        
    print()
    def cost(x):
        return x**2
    
    def neighbours(x):
        return [x - 1, x + 1]
    
    for state in greedy_descent(-6.75, neighbours, cost):
        print(state)
        
    print()
    def cost(x):
        return -x**2
    
    def neighbours(x):
        return [x - 1, x + 1] if abs(x) < 5 else []
    
    for state in greedy_descent(0, neighbours, cost):
        print(state)  
        
    print()
    def cost(x):
        return -x**2
    
    def neighbours(x):
        return [x + 1, x - 1] if abs(x) < 5 else []
    
    for state in greedy_descent(0, neighbours, cost):
        print(state)    

if __name__ == '__main__':
    main()