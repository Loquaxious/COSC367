def n_queens_cost(state):
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range((i + 1), n):
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost 


def main():
    print('test 1')
    print(n_queens_cost((1, 2)))
    
    print()
    print('test 2')
    print(n_queens_cost((1, 3, 2)))
    
    print()
    print('test 3')
    print(n_queens_cost((1, 2, 3)))
    
    print()
    print('test 4')
    print(n_queens_cost((1,)))
    
    print()
    print('test 5')
    print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))
    
    print()
    print('test 6')
    print(n_queens_cost((2, 3, 1, 4)))  
        
if __name__ == '__main__':
    main()