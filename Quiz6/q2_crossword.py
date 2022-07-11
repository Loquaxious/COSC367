"""
Make the following CSP arc consistent by modifying the code (if necessary) and 
pasting the result in the answer box.


from csp import CSP

crossword_puzzle = CSP(
    var_domains={
        # read across:
        'a1': set("ant big bus car has".split()),
        'a3': set("book buys hold lane year".split()),
        'a4': set("ant big bus car has".split()),
        # read down:
        'd1': set("book buys hold lane year".split()),
        'd2': set("ginger search symbol syntax".split()),
        },
    constraints={
        lambda a1, d1: a1[0] == d1[0],
        lambda d1, a3: d1[2] == a3[0],
        lambda a1, d2: a1[2] == d2[0],
        lambda d2, a3: d2[2] == a3[2],
        lambda d2, a4: d2[4] == a4[0],
        })


Notes:

    1. This CSP instance is for a crossword puzzle (visualised here). Look at 
    the puzzle and check whether this instance indeed represents the puzzle. 
    Note that the domains contain only words that have the same length as the 
    corresponding variable (field) in the puzzle. Another approach would be to 
    have all the words in all the domains and provide additional length constraints 
    for variables.
    2. Start by copying the above program into your editor. Modify the domains 
    and then paste in the result. Remember to include the import statement in your answer.
    3. The expression set("ant big bus car has".split()) is equivalent to 
    {"ant", "big", "bus", "car", "has"}. However, it emphasises the fact that we
    can use any expression that evaluates to a set of values and that these 
    values need not be hard-coded. For example we could use an expression to 
    fetch the words from a database. For answer this question, you are free to 
    use any expression you wish as long as it evaluates to the correct set of values.
"""


from csp import CSP

crossword_puzzle = CSP(
    var_domains={
        # read across:
        'a1': set("bus has".split()),
        'a3': set("lane year".split()),
        'a4': set("ant car".split()),
        # read down:
        'd1': set("buys hold".split()),
        'd2': set("search syntax".split()),
        },
    constraints={
        lambda a1, d1: a1[0] == d1[0],
        lambda d1, a3: d1[2] == a3[0],
        lambda a1, d2: a1[2] == d2[0],
        lambda d2, a3: d2[2] == a3[2],
        lambda d2, a4: d2[4] == a4[0],
        })


def main():
    print('across')
    print(sorted(crossword_puzzle.var_domains['a1']))
    print(sorted(crossword_puzzle.var_domains['a3']))
    print(sorted(crossword_puzzle.var_domains['a4']))  
    print()
    print('down')
    print(sorted(crossword_puzzle.var_domains['d1']))  
    print(sorted(crossword_puzzle.var_domains['d2']))  
    

if __name__ == "__main__":
    main()