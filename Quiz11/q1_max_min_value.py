"""
Write two functions max_value(tree) and min_value(tree) that given a game tree, return the utility of the root of the tree when the root is a max node or min node correspondingly. Process the children of a node from left (lower index) to right (higher index).
"""
def max_value(tree):
    if type(tree) == int:
        return tree
    return max(min_value(i) for i in tree)


def min_value(tree):
    if type(tree) == int:
        return tree
    return min(max_value(i) for i in tree)


def main():
    print('test 1')
    game_tree = 3
    
    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))
    
    print()
    print('test 2')
    game_tree = [1, 2, 3]
    
    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))
    
    print()
    print('test 3')
    game_tree = [1, 2, [3]]
    
    print(min_value(game_tree))
    print(max_value(game_tree))
    
    print()
    print('test 4')
    game_tree = [[1, 2], [3]]
    
    print(min_value(game_tree))
    print(max_value(game_tree))
    

if __name__ == '__main__':
    main()