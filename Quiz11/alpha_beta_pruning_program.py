"""
Sorta the alpha beta search algorithm but not quite working and more just made to see how to trace through the algorithm
"""
def max_value(tree, alpha=None, beta=None):
    if alpha and beta:
        if type(tree) == int:
            return tree
        v = float('-inf')
        for i in range(len(tree)):
            print('tree value', tree[i])
            print('v before', v)
            print('alpha before', alpha)
            v = max(v, min_value(tree[i], alpha, beta))
            alpha = max(alpha, v)
            print('v after', v)
            print('alpha after', alpha) 
            print('-'*25)
            if alpha >= beta:
                print('!! pruned at', (alpha, beta), v)
                return v
        return v
    else:
        if type(tree) == int:
            return tree
        return max(min_value(i) for i in tree)


def min_value(tree, alpha=None, beta=None):
    if alpha and beta:
        if type(tree) == int:
            return tree
        v = float('inf')
        for i in range(len(tree)):
            print('tree value', tree[i])
            print('v before', v)
            print('beta before', beta)
            v = min(v, max_value(tree[i], alpha, beta))
            beta = min(beta, v)
            print('v after', v)
            print('beta after', beta)
            print('-'*25)
            if alpha >= beta:
                print('!! pruned at', (alpha, beta), v)
                return v
        return v
    else:    
        if type(tree) == int:
            return tree
        return min(max_value(i) for i in tree)


def alpha_beta_search(tree, minimax='max'):
    if minimax == 'max':
        v = max_value(tree, float('-inf'), float('inf'))
        return v
    else:
        v = min_value(tree, float('-inf'), float('inf'))
        return v

def main():
    print(alpha_beta_search([[1, [3 , -11], 8], [6, -4, 6]]))

    
    
    
if __name__ == '__main__':
    main()
