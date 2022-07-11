def estimate(time, observations, k):
    distance = lambda x, y : abs(x - y)
    dist = sorted((distance(time, y[0]), y) for y in observations)
    neighbours = []
    if k < len(dist):
        for i in range(k):
            neighbours.append(dist[i])
        if neighbours[-1][0] == dist[k][0]:
            prev = neighbours[-1][0]
            neighbours.append(dist[k])
            for j in range(k+1, len(dist)):
                if prev == dist[j][0]:
                    neighbours.append(dist[j])
                else:
                    break
        return sum(x[1][1] for x in neighbours) / len(neighbours)
    else:
        return sum(x[1][1] for x in dist) / len(dist)
    


def main():
    observations = [
        (-1, 1),
        (0, 0),
        (-1, 1),
        (5, 6),
        (2, 0),
        (2, 3),
    ]
    
    for time in [-1, 1, 3, 3.5, 6]:
        print(estimate(time, observations, 2)) 
        
    print()
    observations = [
        (-1, 1),
        (0, 0),
        (-1, 1),
        (5, 6),
        (2, 0),
        (2, 3),
    ]
    
    for time in [-1, 1, 3, 3.5, 6]:
        print("{:1.3}".format(estimate(time, observations, 10)))    
    
if __name__ == '__main__':
    main()