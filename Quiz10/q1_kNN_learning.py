"""
The kNN learning algorithm depends on two functions that must be passed to the algorithm:

distance: this is a function that takes two objects and returns a non-negative number that is the distance between the objects according to some metric. This function is used to identify the neighbours of an object.
combine: this is a function that takes a set of outputs and combines them in order to derive a new prediction.
In this question you have to write two concrete examples of these functions. Write the following functions:

euclidean_distance(v1, v2) where v1 and v2 are two numeric vectors (sequences) with the same number of elements. The function must return the euclidean distance between the points represented by v1 and v2.
majority_element(labels) where labels is a collection of class labels. The function must return a label that has the highest frequency (most common). [if there is a tie it doesn't matter which majority is returned.] This is an example of a combine function.
"""
import math
from collections import defaultdict

def euclidean_distance(v1, v2):
    e_dist = 0
    for i in range(len(v1)):
        e_dist += (v1[i] - v2[i])**2
    return math.sqrt(e_dist)


def majority_element(labels):
    memo = defaultdict(int)
    for item in labels:
        memo[item] += 1
    result = None 
    r_val = 0
    for key, value in memo.items():
        if r_val < value:
            r_val = value
            result = key
    return result
            

def main():
    print('test 1')
    print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))
    
    print()
    print('test 2')
    print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
    print(majority_element("ababc") in "ab")    

if __name__ == '__main__':
    main()