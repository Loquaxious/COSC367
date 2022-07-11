import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")

"""
Write a function forward_deduce that takes the string of a knowledge base containing propositional definite clauses and returns a (complete) set of atoms (strings) that can be derived (to be true) from the knowledge base.
"""
def forward_deduce(kb):
    C = set()
    prevC = None
    while prevC != C:
        prevC = C
        for clause in list(clauses(kb)):
            if len(clause[1]) == 0:
                C = C.union([clause[0]])
            else:
                if set(clause[1]).issubset(C) and clause[0] not in C:
                    C = C.union([clause[0]])
                else:
                    continue
            
    return C
        

if __name__ == '__main__':
    kb = """
    a :- b.
    b.
    """
    
    print(", ".join(sorted(forward_deduce(kb))))
    
    print()
    print('test 2')
    kb = """
    good_programmer :- correct_code.
    correct_code :- good_programmer.
    """
    
    print(", ".join(sorted(forward_deduce(kb))))
    
    print()
    print('test 3')
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """
    
    print(", ".join(sorted(forward_deduce(kb))))    