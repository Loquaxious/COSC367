from search import *
import math

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

def main():
    print('Example 1')
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('C', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})
    
    
    for arc in graph.outgoing_arcs('A'):
        print(arc)
    
    for arc in graph.outgoing_arcs('B'):
        print(arc)
    
    for arc in graph.outgoing_arcs('C'):
        print(arc)

    print()
    print('Example 2')
    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10,6),
                   'c': (10,18)},
        edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
        starting_nodes=['a'],
        goal_nodes={'c'})
    
    for arc in pythagorean_graph.outgoing_arcs('a'):
        print(arc)   
        
    print()
    print('Example 3')
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A'), ('C', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})
    
    
    for arc in graph.outgoing_arcs('A'):
        print(arc)
    
    for arc in graph.outgoing_arcs('B'):
        print(arc)
    
    for arc in graph.outgoing_arcs('C'):
        print(arc)    

if __name__ == '__main__':
    main()
