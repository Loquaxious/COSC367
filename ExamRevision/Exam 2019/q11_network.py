network = {
    'A': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.001,
            (False,) : 0.9
         }
    },
        
    'B': {
        'Parents': [],
        'CPT': {
            (): 0.002,
        }
    },

    'C': {
        'Parents': ['A', 'D'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
        }
    },

    'D': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
        }
    },
}