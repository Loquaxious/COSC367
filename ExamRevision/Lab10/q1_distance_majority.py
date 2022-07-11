import math 
from collections import defaultdict

def euclidean_distance(v1, v2):
    dist = 0
    for i in range(len(v1)):
        dist += (v1[i] - v2[i])**2
    
    return math.sqrt(dist)


def majority_element(labels):
    ddict = defaultdict(int)
    for label in labels:
        ddict[label] +=1
    max_element = max((item, key) for key, item in ddict.items())
    return max_element[1]

def main():
    print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))
    
    print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
    print(majority_element("ababc") in "ab")    

if __name__ == '__main__':
    main()