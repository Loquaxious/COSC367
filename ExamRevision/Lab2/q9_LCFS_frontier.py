from search import *
import math
import heapq

class LocationGraph(ExplicitGraph):
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes):
        self.nodes = nodes
        self.locations = locations
        self.edges = edges
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def outgoing_arcs(self, node):
        arcs = []
        for edge in self.edges:
            if node in edge:
                x1, y1 = self.locations[edge[0]]
                x2, y2 = self.locations[edge[1]]
                dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
                if edge[0] != node:
                    if Arc(node, edge[0], str(node) + '->' + str(edge[0]), dist) not in arcs:
                        arcs.append(Arc(node, edge[0], str(node) + '->' + str(edge[0]), dist))
                else:
                    if Arc(node, edge[1], str(node) + '->' + str(edge[1]), dist) not in arcs:
                        arcs.append(Arc(node, edge[1], str(node) + '->' + str(edge[1]), dist))
        return sorted(arcs, key=lambda x : (x[0], x[1]))


class LCFSFrontier(Frontier):
    def __init__(self):
        self.heap = []
        self.count = 0
    
    def add(self, path):
        totalcst = 0
        for arc in path:
            totalcst += arc[-1]
        heapq.heappush(self.heap, (totalcst, self.count, path))
        self.count += 1
    
    def __next__(self):
        return heapq.heappop(self.heap)[-1]
            


def main():
    print('Example 1')
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A'), ('C', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

    print()
    print('Example 2')
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution) 
        
    print()
    print('Example 3')
    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10,6),
                   'c': (10,18)},
        edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
        starting_nodes=['a'],
        goal_nodes={'c'})
    
    solution = next(generic_search(pythagorean_graph, LCFSFrontier()))
    print_actions(solution)    

if __name__ == '__main__':
    main()
