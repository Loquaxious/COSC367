"""
Write a function of the form is_valid_expression(object, function_symbols, leaf_symbols) that takes an object as its first argument and tests whether it is a valid expression according to our definition of expressions in this assignment. The function must return True if the given object is valid expression, False otherwise.

The parameters of the function are:

object: any Python object
function_symbols: a collection (list, set, ...) of strings that are allowed to be used in function positions (internal nodes of the tree).
leaf_symbols: a collection of strings that are allowed to be used as variable leaves.
Notes
This function needs to be recursive. The base cases are for leaf nodes.
This function can be written in less than 10 lines of code.
The built-in function type can be useful here.
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
        

def main():
    print('test 1:1')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 1
    
    print(is_valid_expression(expression, function_symbols, leaf_symbols)) 
    
    print()
    print('test 1:2')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'y'
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    print()
    print('test 1:3')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 2.0
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    print()
    print('test 1:4')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 123, 'x']
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    print()
    print('test 1:5')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', ['+', 0, -1], ['f', 1, 'x']]
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    print()
    print('test 1:6')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['+', ['f', 1, 'x'], -1]
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    print()
    print('test 1:7')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y', -1, 0, 1]
    expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    print()
    print('test 1:8')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'f'
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    print()
    print('test 1:9')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 1, 0, -1]
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    print()
    print('test 1:10')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['x', 0, 1]
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    print()
    print('test 1: 11')
    function_symbolsfunction_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['g', 0, 'y']
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
if __name__ == '__main__':
    main()