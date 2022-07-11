network = {
    'Y': {
        'Parents': [],
        'CPT': {
            (): 5/8 
         }
    },
        
    'X1': {
        'Parents': ['Y'],
        'CPT': {
            (True,): 5/6,
            (False,): 2/4,
        }
    },

    'X2': {
        'Parents': ['Y'],
        'CPT': {
            (True,): 2/6,
            (False,): 1/4,
        }
    },
}

print("{:0.2f}".format(network['Y']['CPT'][()]))