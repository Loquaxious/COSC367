from csp import Relation

relations = [
      Relation(header = ['a','b','c'],
          tuples = {(1,2,3),
                  (1,2,4),
                  (1,3,4),
                  (2,3,4)
                  }
          ),
      
      Relation(header = ['b'],
          tuples = {(2,),
                  (4,)
                  }
          )
      
      ] 

relations_after_elimination = [
    
    Relation(header=['a','c'],
        tuples={(1,3),
                (1,4)
                }
        )
    
    ] 


print(type(relations) is list)
print(all(type(r) is Relation for r in relations))
print()
print(type(relations_after_elimination) is list)
print(all(type(r) is Relation for r in relations_after_elimination))
