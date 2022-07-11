"""
Write two functions max_action_value(game_tree) and min_action_value(game_tree) that given a game tree, return a pair where first element is the best action and the second element is the utility of the root of the tree when the root is a max node or min node correspondingly. For a leaf node the action is None; for an internal node, the action is the index of the subtree corresponding to the best action. Process the children of a node from left (lower index) to right (higher index). If there is a tie, return the left-most optimal action.
"""
def max_value(tree):
    if type(tree) == int:
        return tree
    return max(min_value(i) for i in tree)


def min_value(tree):
    if type(tree) == int:
        return tree
    return min(max_value(i) for i in tree)


def max_action_value(game_tree):
    utility = max_value(game_tree)
    if type(game_tree) == int:
        return (None, utility)
    action, index = max((min_value(game_tree[i]), i) for i in range(len(game_tree)))
    return (index, utility)


def min_action_value(game_tree):
    utility = min_value(game_tree)
    if type(game_tree) == int:
        return (None, utility)
    action, index = min((max_value(game_tree[i]),i) for i in range(len(game_tree)))
    return (index, utility)


def main():
    print('test 1')
    game_tree = [2, [-3, 1], 4, 1]
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    
    print()
    print('test 2')
    game_tree = 3
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    
    print()
    print('test 3')
    game_tree = [1, 2, [3]]
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    
    print()
    print('test 4')
    game_tree = [[2, 3, 4], [1, 100, -100]]
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)    
    
    print()
    game_tree = [[3, -2], [2, 1, 4]] 
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
if __name__ == '__main__':
    main()