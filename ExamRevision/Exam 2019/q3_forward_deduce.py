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
        
def forward_deduce(kb):
    kb_clauses = list(clauses(kb))
    true_atoms = set()
    prev_atoms = None
    while true_atoms != prev_atoms:
        prev_atoms = true_atoms.copy()
        for clause in kb_clauses:
            if len(clause[1]) == 0:
                true_atoms.add(clause[0])
            else:
                if set(clause[1]).issubset(true_atoms):
                    true_atoms = true_atoms.union({clause[0]})
                    
    return true_atoms


def main():
    kb = """
    a :- b.
    b.
    """
    
    print(", ".join(sorted(forward_deduce(kb))))
    
    print()
    kb = """
    good_programmer :- correct_code.
    correct_code :- good_programmer.
    """
    
    print(", ".join(sorted(forward_deduce(kb))))
    
    print()
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
    
if __name__ == '__main__':
    main()