network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
    },
    
    'B': {
    'Parents': [],
    'CPT': {
        (): 0.2 # You can change this value
        }
    },
    
    'C': {
    'Parents': [],
    'CPT': {
        (): 0.2 # You can change this value
        }
    
    },
    
    'D': {
    'Parents': ['B'],
    'CPT': {
        (True,): 0.2, # You can change this value
        (False,):0.3
        }
    
    },
    
    'E': {
    'Parents': ['B'],
    'CPT': {
        (True,): 0.2,
        (False,):0.4
        }
    
    },    
}
            
            
