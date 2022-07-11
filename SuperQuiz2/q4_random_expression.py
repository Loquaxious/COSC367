"""
Write a function random_expression(function_symbols, leaves, max_depth) that randomly generates an expression. The function takes the following arguments:

function_symbols: a list of function symbols (strings)
leaves: a list of constant and variable leaves (integers and strings)
max_depth: a non-negative integer that specifies the maximum depth allowed for the generated expression.
The function will be called 10,000 times to generate these many expressions. Then the following tests are performed on the generated expressions:

All the generated expressions must be valid expressions constructed from the given function symbols and leaves.
Out of the 10,000 generated expressions, at least 1000 must be syntactically distinct. The semantic of expressions is disregarded when testing for distinctness. For example ['+', 1, 2] and ['+', 2, 1] will be regarded as different expressions.
Out of the 10,000 generated expressions, at least 100 must be of depth 0, at least 100 of depth 1, ..., and at least 100 must be of depth max_depth (which is set to 4 in the test cases).
Notes
This function is recursive.
I suggest an implementation along these lines: Toss a coin. If it's a head (or if some other condition that you have to determine is satisfied) return a leaf node, otherwise return a random expression tree (a 3-element list). If the latter, you also need to randomly generate its two arguments.
Consider using functions provided in the random module.
You can implement this function in about 15 lines of code
In order to be able to replicate your results (for example for debugging purposes), consider using random.seed(some_integer) which will cause the generators to always produce the same sequence of random numbers and as a result your program will always produce the same output.
It is recommended that you test your code locally. You should consider developing your own test code that checks the stated requirements.
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


def main():
    random.seed(1)
    print('test 1: valid expressions')
    # All the generated expressions must be valid
    
    function_symbols = ['f', 'g', 'h']
    constant_leaves =  list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    max_depth = 4
    
    for _ in range(10000):
        expression = random_expression(function_symbols, leaves, max_depth)
        if not is_valid_expression(expression, function_symbols, leaves):
            print("The following expression is not valid:\n", expression)
            break
    else:
        print("OK")
    
    print()
    print('test 2: expression depth')
    function_symbols = ['f', 'g', 'h']
    constant_leaves =  list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    max_depth = 4
    
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0    
    
    for _ in range(10000):
        expression = random_expression(function_symbols, leaves, max_depth)
        d = depth(expression)
        if d > max_depth: 
            print('The following expression is deeper than shoud be\n', expression)
            break
        if d == 0:
            count0 += 1
        elif d == 1:
            count1 += 1
        elif d == 2:
            count2+=1
        elif d == 4:
            count3+=1
        else:
            count4+=1
    else:
        print('OK')
        print(count0, count1, count2, count3, count4)
    
    #print()
    #print('test 3: distinctness')
    #function_symbols = ['f', 'g', 'h']
    #constant_leaves =  list(range(-2, 3))
    #variable_leaves = ['x', 'y', 'i']
    #leaves = constant_leaves + variable_leaves
    #max_depth = 4
    
    #expressions = [random_expression(function_symbols, leaves, max_depth) for _ in range(10000)] 
    #d_count = 0
    #memo = set()
    #for exp in expressions:
        #if type(exp) == int or type(exp) == str:
            #if (exp,) not in memo:
                #memo = memo.union((exp,))
                #d_count += 1
        #else:
            #if tuple(exp) not in memo:
                #memo = memo.union(tuple(exp))
                #d_count += 1

    #print('distinct expressions: ',d_count)  
    
     
if __name__ == '__main__':
    main()