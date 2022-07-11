"""
Write a function knn_predict(input, examples, distance, combine, k) that takes an input and predicts the output by combining the output of the k nearest neighbours. If after selecting k nearest neighbours, the distance to the farthest selected neighbour and the distance to the nearest unselected neighbour are the same, more neighbours must be selected until these two distances become different or all the examples are selected. The description of the parameters of the function are as the following:

input: an input object whose output must be predicted. Do not make any assumption about the type of input other than that it can be consumed by the distance function.
examples: a collection of pairs. In each pair the first element is of type input and the second element is of type output.
distance: a function that takes two objects and returns a non-negative number that is the distance between the two objects according to some metric.
combine: a function that takes a set of outputs and combines them in order to derive a new prediction (output).
k: a positive integer which is the number of nearest neighbours to be selected. If there is a tie more neighbours will be selected (see the description above).
Note: the majority_element function used in some test cases returns the smallest element when there is a tie. For example majority_element('--++') returns '+' because it is the most common label (like -) and in the character encoding system '+' comes before '-'.
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


def knn_predict(input, examples, distance, combine, k):
    label = []
    dist = []
    for example in examples:
        dist.append((example[1], distance(input, example[0])))
    dist.sort(key=lambda x : (x[1], x[0]))
    print(dist)
    prev = None
    for i in range(k):
        label.append(dist[i][0])
        prev = dist[i]
    print('label before', label)
    if k >= len(dist):
        return combine(label)
    else:
        j = k
        while prev[1] == dist[j][1]:
            label.append(dist[j][0])
            j+=1
            if j == len(dist):
                print('break')
                break
        print('label after', label)                  
        return combine(label)


def main():
    print('test 1')
    examples = [
        ([2], '-'),
        ([3], '-'),
        ([5], '+'),
        ([8], '+'),
        ([9], '+'),
    ]
    
    distance = euclidean_distance
    combine = majority_element
    
    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0,10):
            print(x, knn_predict([x], examples, distance, combine, k))
        print()
    
    print()
    print('test 2')
    # using knn for predicting numeric values
    
    examples = [
        ([1], 5),
        ([2], -1),
        ([5], 1),
        ([7], 4),
        ([9], 8),
    ]
    
    def average(values):
        return sum(values) / len(values)
    
    distance = euclidean_distance
    combine = average
    
    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0,10):
            print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
        print()   

if __name__ == '__main__':
    main()