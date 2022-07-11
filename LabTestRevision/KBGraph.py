"""
Write a class KBGraph that poses a knowledge base and a query as a graph. The intention is to use the graph with a graph search algorithm to have a top-down proof procedure. The query will be a set of atoms (strings). If you wish you can use the template provided in the answer box. You must also provide an implementation of DFSFrontier. You can simply copy this across from the graph search quiz if you have answered that question.

The graph class will not be tested on the order of edges; you can generate edges in whatever order you wish. The input knowledge base is guaranteed to not have cyclic clauses. For example the following is NOT an example input:

a :- b.
b :- c.
c :- a.
d.
Notes
See the top-down proof procedure, answer clauses, and the example search tree for an SLD resolution in the lecture notes.
The top-down proof procedure presented in the lecture notes has a non-deterministic statement ("choose"). For implementation, this has to be translated to some form of backtracking. This is why you are being asked to provide a graph class and a DFS frontier class. These two together implicitly achieve backtracking.
You need to think about the right representation for nodes. Since all answer clauses are of the form yes :- a_body, you can factor out the 'yes' part and only represent the body.
After answering this question, as an additional exercise for yourself, improve your program such that knowledge bases with cycles can be handled.
If the graph search determines that the given query is true, the proof of it can be produced by printing the path. Therefore it is useful to have meaningful labels for the edges of the graph (where each label is a string representation of a rule from the KB). You are not required to implement this in your answer.
The length of the proof will depend on the search strategy (the type of frontier used for the graph search).
"""

import re
from search import *


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 31 Jul 2019

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        return [self.query]
        
    def is_goal(self, node):
        return len(node) == 0

    def outgoing_arcs(self, tail_node):
        arcs = []
        for clause in self.clauses:
            if clause[0] in tail_node:
                arcs.append(Arc(tail_node, clause[1], str(tail_node) + '->' + str(clause[1]), None))
        return arcs
            

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration   # don't change this one
        
def main():
    print('test 1')
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
    
    query = {'a'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")
        
    print()
    print('test 2')
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
    
    query = {'a', 'b', 'd'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

if __name__ == '__main__':
    main()