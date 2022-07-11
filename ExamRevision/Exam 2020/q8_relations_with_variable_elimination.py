"""
csp = CSP(
   var_domains = {var:{-1,0,1} for var in 'abc'},
   constraints = {
      lambda a, b: a * b > 0,
      lambda b, c: b + c > 0,
      }
    )
"""

from csp import Relation

relations = [
      Relation(
          header=['a','b'],
          tuples={(1,1),
                  (-1,-1)}
          ),
      Relation(
          header=['b','c'],
          tuples={(0,1),
                  (1,0),
                  (1,1)}
          )
      ] 

relations_after_elimination = [
    Relation(
        header=['a','c'],
        tuples={(1,1),
                (1,0)}
        )
    ] 
