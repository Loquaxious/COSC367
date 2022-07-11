from search import *
from statistics import pvariance
import heapq


class PriorityFrontier(Frontier):
    

    def __init__(self):
        # The constructor does not take any arguments.
        self.container = []
        self.count = 0
        self.pruned = set()
        

    def add(self, path):
        totalcst = 0
        population = []
        for arc in path:
            population.append(arc[-1])
            totalcst += arc[-1]
        pvar = pvariance(population)
        if path[-1][1] not in self.pruned:
            heapq.heappush(self.container, (totalcst, pvar, self.count, path))
            self.count+=1
        else:
            return

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional information for iteration."""
        return self
        
    def __next__(self):
        while len(self.container) > 0:
            result = heapq.heappop(self.container)[-1]
            if result[-1][1] not in self.pruned:
                self.pruned = self.pruned.union(result[-1][1])
                return result
        raise StopIteration   # raise this when the container is exhuasted
    
def main():
    print('Example 1')
    graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A',3), ('S','B',1), ('B','A',1), ('A','B',1), ('A','G',5)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

    solution = next(generic_search(graph, PriorityFrontier()))
    print_actions(solution)
    
    print()
    print('Example 2')
    graph = ExplicitGraph(
        nodes = {'S', 'A', 'B', 'G'},
        edge_list=[('S','A', 1), ('S','B',2),
                   ('A', 'G', 3), ('B', 'G', 2)],
        starting_nodes = ['S'],
        goal_nodes = {'G'})
    
    solution = next(generic_search(graph, PriorityFrontier()))
    print_actions(solution)
    
    print()
    print('Example 3')
    graph = ExplicitGraph(
        nodes = {'S', 'A', 'B', 'C', 'G'},
        edge_list=[('S','A', 1), ('S','C',2), ('S', 'B', 2),
                   ('A', 'G', 3), ('C', 'G', 2), ('B', 'G', 2)],
        starting_nodes = ['S'],
        goal_nodes = {'G'})
    
    solution = next(generic_search(graph, PriorityFrontier()))
    print_actions(solution) 
    
    print()
    print('Example 4')
    graph = ExplicitGraph(
        nodes = {'S', 'A', 'B', 'G'},
        edge_list=[('S','A', 1), ('A', 'B', 1), ('B','S',1)],
        starting_nodes = ['S'],
        goal_nodes = {'G'})
    
    solution = next(generic_search(graph, PriorityFrontier()), None)
    print_actions(solution)    

if __name__ == '__main__':
    main()