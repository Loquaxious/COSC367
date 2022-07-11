def max_value(tree):
    if type(tree) == int:
        return tree
    else:
        return max(min_value(x) for x in tree)

def min_value(tree):
    if type(tree) == int:
        return tree
    else:
        return min(max_value(x) for x in tree)  
    
def max_action_value(game_tree):
    if type(game_tree) == int:
        return (None, game_tree)
    else:
        result = max((min_value(game_tree[i]),i) for i in range(len(game_tree)))
    return (result[1], result[0])

def min_action_value(game_tree):
    if type(game_tree) == int:
        return (None, game_tree)
    else:
        result = min((max_value(game_tree[i]),i) for i in range(len(game_tree)))
    return (result[1], result[0])


def main():
    game_tree = [2, [-3, 1], 4, 1]
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    print()
    
    game_tree = 3
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    print()
    
    game_tree = [1, 2, [3]]
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    
if __name__ == '__main__':
    main()