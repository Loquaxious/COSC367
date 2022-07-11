"""
Write a function depth(expression) that takes an expression (that follows our definition of expression) and returns the depth of the expression tree. The depth of a tree is the depth of its deepest leaf.

Notes
This is a recursive function and can be written in 5 lines of code.
The depth of an expression that is just a single leaf (e.g. the expression 2 or y) is zero.
Converting the expression into a string and analysing the string to compute the depth is not a good idea.
"""
def is_valid_expression(object, function_symbols, leaf_symbols):
    if type(object) == int:
        return True
    elif type(object) == str and object in leaf_symbols:
        return True
    elif type(object) == list and len(object) == 3:
        if object[0] in function_symbols and is_valid_expression(object[1], function_symbols, leaf_symbols) and is_valid_expression(object[2], function_symbols, leaf_symbols):
            return True
        else:
            return False
    else:
        return False
        

def depth(expression):
    if type(expression) != list:
        return 0
    else:
        d1 = depth(expression[1])
        d2 = depth(expression[2])
        if d1 > d2:
            return depth(expression[1]) + 1
        else:
            return depth(expression[2]) + 1

def main():
    print('test 1')
    expression = 12
    print(depth(expression))
    
    print()
    print('test 2')
    expression = 'weight'
    print(depth(expression))
    
    print()
    print('test 3')
    expression = ['add', 12, 'x']
    print(depth(expression))
    
    print()
    print('test 4')
    expression = ['add', ['add', 22, 'y'], 'x']
    print(depth(expression))   
    
    print()
    print('test 5')
    expression = ['+', ['*', 2, 'i'], ['*', -3, 'x']]
    print(depth(expression))    
    
if __name__ == '__main__':
    main()