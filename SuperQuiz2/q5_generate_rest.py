"""
Write a function generate_rest(initial_sequence, expression, length) that takes an initial sequence of numbers, an expression, and a specified length, and returns a list of integers with the specified length that is the continuation of the initial list according to the given expression. The parameters are:

    initial_sequence: an initial sequence (list) of integer numbers that has at least two numbers;
    expression: an expression constructed from function symbols '+', '-', and '*' which correspond to the three binary arithmetic functions, and the leaf nodes are integers and 'x', 'y', and 'i' where the intended meaning of these three symbols is described above; 
    length: a non-negative integer that specifies the length of the returned list.

Hint: The values must be generated in order, from left to right. For the first value, the expression must be evaluated with 'i' set to the length of the initial sequence (because this would be the index of the first number in the generated sequence) and 'x' and 'y' set to the last two elements of the initial sequence. As new values are generated, the values of i, x, and y are updated. Recall that values of variable leaves are set via a dictionary of bindings.

Note: It is recommended that you use your implementation of the evaluate function. This would allow you to implement this function in about 11 lines of code.
"""
import random
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


def random_expression(function_symbols, leaves, max_depth, depth=0):
    if random.random() >= 0.5 or depth == max_depth:
        return leaves[random.randint(0, len(leaves)-1)]
    else:
        return [function_symbols[random.randint(0, len(function_symbols)-1)], 
                random_expression(function_symbols, leaves, max_depth, depth+1), 
                random_expression(function_symbols, leaves, max_depth, depth+1)]
    
    
def generate_rest(initial_sequence, expression, length):
    bindings = {'i' : len(initial_sequence), 
                'y' : initial_sequence[-1], 
                'x' : initial_sequence[-2],
                '*' : lambda x, y : x * y,
                '+' : lambda x, y : x + y,
                '-' : lambda x, y : x - y}
    result = []
    
    for i in range(length):
        e = evaluate(expression, bindings)
        result.append(e)        
        bindings['x'] = bindings['y']
        bindings['y'] = e
        bindings['i'] = i + len(initial_sequence) + 1
    return result
        

def main():
    random.seed(1)
    print('test 1')
    initial_sequence = [0, 1, 2]
    expression = 'i' 
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression,
                        length_to_generate))
    
    print()
    print('test 2')
    # no particular pattern, just an example expression
    initial_sequence = [-1, 1, 367]
    expression = 'i' 
    length_to_generate = 4
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))
    
    print()
    print('test 3')
    initial_sequence = [4, 6, 8, 10]
    expression = ['*', ['+', 'i', 2], 2]
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    print()
    print('test 4')
    initial_sequence = [4, 6, 8, 10]
    expression = ['+', 2, 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    print()
    print('test 5')
    initial_sequence = [0, 1]
    expression = 'x'
    length_to_generate = 6
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    print()
    print('test 6')
    # Fibonacci sequence
    initial_sequence = [0, 1]
    expression = ['+', 'x', 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    print()
    print('test 7')
    initial_sequence = [367, 367, 367]
    expression = 'y'
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    print()
    print('test 8')
    # no pattern, just a demo
    initial_sequence = [0, 1, 2]
    expression = -1 
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    print()
    print('test 9')
    initial_sequence = [0, 1, 2]
    expression = 'i'
    length_to_generate = 0
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))    
    
     
if __name__ == '__main__':
    main()