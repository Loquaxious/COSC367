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


def knn_predict(input, examples, distance, combine, k):
    dist = []
    for iput, oput in examples:
        dist.append((distance(input, iput), oput))
    dist.sort()
    neighbours = [dist[i] for i in range(k)]
    if k < len(dist) and neighbours[-1][0] == dist[k][0]:
        prev = neighbours[-1][0]
        neighbours.append(dist[k])
        for i in range(k+1, len(dist)):
            if prev == dist[i][0]:
                neighbours.append(dist[i])
            else:
                break
    return combine([x[1] for x in neighbours])


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