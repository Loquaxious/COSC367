network = {
    'Y' : {
        'Parents' : [],
        'CPT' : {
            () : 4/9
            }
        },
    'X1' : {
        'Parents' : ['Y'],
        'CPT' : {
            (True,) : 2/5,
            (False,) : 3/6
            }
        },
    'X2' : {
        'Parents' : ['Y'],
        'CPT' : {
            (True,) : 2/5,
            (False,) : 1/6
            }
        },
    'X3' : {
        'Parents' : ['Y'],
        'CPT' : {
            (True,) : 1/5,
            (False,) : 1/6
            }
        }
    }