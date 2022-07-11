def num_parameters(unit_counts):
    total = 0
    if len(unit_counts) > 1:
        total += unit_counts[0] * unit_counts[1]
        for i in range(1, len(unit_counts)-1):
            total += unit_counts[i] * unit_counts[i+1]
        
        for i in range(1, len(unit_counts)):
            total += unit_counts[i]
        return total        
        
    else:
        return 0
    
print(num_parameters([2,4,2]))   
print(num_parameters([2, 4, 3, 4]))

