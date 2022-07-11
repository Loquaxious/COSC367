network = {
    'A' : {
        'Parents' : ['C'],
        'CPT' : {
            (True,) : 0.95,
            (False,) : 0.32
            }
        },
    'B' : {
        'Parents' : ['A', 'D'],
        'CPT' : { 
            (True, True) : 0.5,
            (True, False) : 0.23,
            (False, True) : 0.32,
            (False, False) : 0.45
            }
        },
    'C' : {
        'Parents' : [],
        'CPT' : { 
            () : 0.3
            }
        },
    'D' : {
            'Parents' : [],
            'CPT' : { 
                () : 0.3
                }
            },
    }
        
            