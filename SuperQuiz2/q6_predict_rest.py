"""
Finally you are ready to put all the components together and solve the actual problem.  You have to write a function predict_rest(sequence) that takes a sequence of integers of length at least 5, finds the pattern in the sequence, and "predicts" the rest by returning a list of the next five integers in the sequence.

This question is somewhat open-ended; it is up to you what algorithm you implement. The patterns in the test cases are easy enough that even a random search (i.e. generating random expressions until a match is found) is very likely to solve all the test cases. If you are interested, you can implement a proper evolutionary algorithm with operators for mutation and crossover.

Further assumptions
All the sequences in the test cases have patterns that can be expressed as a function of x, y, and i as described before.
All the patterns (functions) can be constructed by combining three binary functions: addition, subtraction, and multiplication.
Using integers between -2 and 2 (inclusive) as constant leafs should be enough to represent the patterns in the test cases.
All the patterns (functions) can  be constructed by expression trees not deeper than 3.
Your algorithm must be able to solve all the problems given in the example test cases in less than 2 seconds (collectively). Following the guidelines given in the assignment should naturally achieve this.
Notes
To make sure your function does not overfit (e.g. memorise) the given example sequences, there are some hidden test cases (which are not more difficult than the example test cases).
Consider using random.seed so that your offline results match what will be generated on the server and you can replicate your results if needed.
Make sure the function does not modify its input.
In its simplest form, this function can be implemented in less than 10 lines of code.
It would be interesting to go through the test cases yourself and see if you can find the patterns.
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


def predict_rest(sequence):
    is_expression = False
    function_symbols = ['*', '+', '-']
    leaves = ['x', 'y', 'i'] + list(range(-2, 3))
    max_depth = 3
    while not is_expression:
        expression = random_expression(function_symbols, leaves, max_depth)
        gen = generate_rest(sequence[:3], expression, len(sequence) - 3)
        if gen == sequence[3:]:
            break
    return generate_rest(sequence, expression, 5)
        

def main():
    import time
    timenow = time.time()
    random.seed(1)
    print('test 1')
    sequence = [0, 1, 2, 3, 4, 5, 6, 7]
    the_rest = predict_rest(sequence)
    print(sequence)
    print(the_rest)
    
    print()
    print('test 2')
    sequence = [0, 2, 4, 6, 8, 10, 12, 14]
    print(predict_rest(sequence))
    
    print()
    print('test 3')
    sequence = [31, 29, 27, 25, 23, 21]
    print(predict_rest(sequence))
    
    print()
    print('test 4')
    sequence = [0, 1, 4, 9, 16, 25, 36, 49]
    print(predict_rest(sequence))
    
    print()
    print('test 5')
    sequence = [3, 2, 3, 6, 11, 18, 27, 38]
    print(predict_rest(sequence))
    
    print()
    print('test 6')
    sequence =  [0, 1, 1, 2, 3, 5, 8, 13]
    print(predict_rest(sequence))
    
    print()
    print('test 7')
    sequence = [0, -1, 1, 0, 1, -1, 2, -1]
    print(predict_rest(sequence))
    
    print()
    print('test 8')
    sequence = [1, 3, -5, 13, -31, 75, -181, 437]
    print(predict_rest(sequence))
    
    print()
    print('total time in seconds')
    print(time.time() - timenow)
     
if __name__ == '__main__':
    main()