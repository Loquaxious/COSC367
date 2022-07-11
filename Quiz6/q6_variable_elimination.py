"""
Convert the following instance of CSP to an equivalent list of relations called relations. In each relation, the variables must appear in alphabetic order. The order of relations in the outer list is not important. Then use the variable elimination algorithm to eliminate variable a and produce a new list of relations called relations_after_elimination.

csp = CSP(
   var_domains = {var:{-1,0,1} for var in 'abcd'},
   constraints = {
      lambda a, b: a == abs(b),
      lambda c, d: c > d,
      lambda a, b, c: a * b > c + 1
      }
   )
"""

from csp import Relation

relations = [
      Relation(header=['a', 'b'],
               tuples={(1, -1),
                       (0, 0),
                       (1, 1)}),
      
      Relation(header=['c', 'd'],
               tuples={(0, -1),
                       (1, -1),
                       (1, 0)}),
      
      Relation(header=['a', 'b', 'c'],
               tuples={(1, 1, -1),
                       (-1, -1, -1)})
      ] 

relations_after_elimination = [
          Relation(header=['c', 'd'],
               tuples={(0, -1),
                       (1, -1),
                       (1, 0)}),
          
          Relation(header=['b', 'c'],
                   tuples={(1, -1)})
    
    ] 

if __name__ == '__main__':
    print(len(relations))
    print(all(type(r) is Relation for r in relations))