#csp = CSP(
   #var_domains = {var:{-1,0,1} for var in 'abc'},
   #constraints = {
      #lambda a, b: a * b == -1,
      #lambda b, c: b + c == 1,
      #}
   #)

from csp import Relation

relations = [
      Relation(
          header = ['a', 'b'],
          tuples = {(1, -1),
                 (-1, 1)}
      ),
      Relation(
          header = ['b', 'c'],
          tuples = {(0, 1),
                  (1, 0)}
          )
      ] 

relations_after_elimination = [
    Relation(
        header = ['a', 'c'],
        tuples = {(-1, 0)}
        )
    ] 

print(type(relations) is list)
print(all(type(r) is Relation for r in relations))
print()
print(type(relations_after_elimination) is list)
print(all(type(r) is Relation for r in relations_after_elimination))