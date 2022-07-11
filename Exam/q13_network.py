network = {
    'A' : {
        'Parents' : ['D'],
        'CPT' : {
            (True,) : 0.2,
            (False,) : 0.3
            }
        },
    
    'B' : {
        'Parents' : ['A', 'C'],
        'CPT' : {
            (True,True) : 0.3,
            (True, False) : 0.45,
            (False,True) : 0.82,
            (False, False) : 0.74
            }
        },
    'C' : {
        'Parents' : ['D'],
        'CPT' : {
            (True,) : 0.69,
            (False,) : 0.96
            }
        },
    
    'D' : {
        'Parents' : [],
        'CPT' : {
            (True,) : 0.46,
            (False,) : 0.42,
            }
        },
    
    'E' : {
        'Parents' : [],
        'CPT' : {
            () : 0.5
            }
        }
    }
    