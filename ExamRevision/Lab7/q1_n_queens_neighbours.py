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


def main():
    print('test 1')
    print(n_queens_neighbours((1, 2)))
    
    print()
    print('test 2')
    print(n_queens_neighbours((1, 3, 2)))
    
    print()
    print('test 3')
    print(n_queens_neighbours((1, 2, 3)))
    
    print()
    print('test 4')
    print(n_queens_neighbours((1,)))
    
    print()
    print('test 5')
    for neighbour in n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
        print(neighbour)
    
    print()
    print('test 6')
    for neighbour in n_queens_neighbours((2, 3, 1, 4)):
        print(neighbour)    
        
if __name__ == '__main__':
    main()