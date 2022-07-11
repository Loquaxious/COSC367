def num_crossovers(parent_expression1, parent_expression2):
    if type(parent_expression1) == list: 
        expr1 = recursive_len(parent_expression1)
    else:
        expr1 = 1
    if type(parent_expression2) == list:
        expr2 = recursive_len(parent_expression2)
    else: 
        expr2 = 1
        
    return expr1 * expr2
    
    
def recursive_len(expression):
    length = 0 
    for node in expression:
        if type(node) == int or type(node) == str:
            length += 1
        else:
            length += recursive_len(node)
    return length

def main():
    
    expression1 = ['+', 12, 'x']
    expression2 = ['-', 3, 6]
    print(num_crossovers(expression1, expression2))
    
    expression1 = 'weight'
    expression2 = ['-', 8, 4]
    print(num_crossovers(expression1, expression2))
    
    expression1 = 2
    expression2 = "five"
    print(num_crossovers(expression1, expression2))
    
    
    
    
if __name__ == '__main__':
    main()