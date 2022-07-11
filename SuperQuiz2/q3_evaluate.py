"""
Write a function evaluate(expression, bindings) that takes an expression and a dictionary of bindings and returns an integer that is the value of the expression. The parameters of the function are:

expression: an expression according to our definition of expressions;
bindings: a dictionary where all the keys are strings and are either a function symbol or a variable leaf. A function symbol is mapped to a function that takes two arguments. A leaf symbol is mapped to an integer.
Note: this function is recursive and can be written in less than 10 lines of code.
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

def evaluate(expression, bindings):
    if type(expression) == int:
        return expression
    elif type(expression) == str and expression in bindings:
        return bindings[expression]
    else:
        function = bindings[expression[0]]
        return function(evaluate(expression[1], bindings), evaluate(expression[2], bindings)) 


def main():
    print('test 1')
    bindings = {}
    expression = 12
    print(evaluate(expression, bindings))
    
    print()
    print('test 2')
    bindings = {'x':5, 'y':10, 'time':15}
    expression = 'y'
    print(evaluate(expression, bindings))
    
    print()
    print('test 3')
    bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
    expression = ['add', 12, 'x']
    print(evaluate(expression, bindings))
    
    print()
    print('test 4')
    import operator

    bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
    expression = ['add', ['add', 22, 'y'], 'x']
    print(evaluate(expression, bindings)) 
    
    #print()
    #print('test 5')
    #expression = ['+', ['*', 2, 'i'], ['*', -3, 'x']]
    #print(depth(expression))    
    
if __name__ == '__main__':
    main()