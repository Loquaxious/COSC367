from search import *
import math

class LocationGraph(ExplicitGraph):
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes, estimates=None):
        """Initialises an location graph.
        Keyword arguments:
        nodes -- a set of nodes
        locations -- a dictionary that holds the coordinates of each node
        edges -- a sequence of tuples in the form (tail, head) or 
                     (tail, head, cost)
        starting_nodes -- the list of starting nodes. We use a list
                          to remind you that the order can influence
                          the search behaviour.
        goal_node -- the set of goal nodes. It's better if you use a set
                     here to remind yourself that the order does not matter
                     here. This is used only by the is_goal method. 
        """

        # A few assertions to detect possible errors in
        # instantiation. These assertions are not essential to the
        # class functionality.
        assert all(tail in nodes and head in nodes for tail, head, *_ in edges)\
           , "An edge must link two existing nodes!"
        assert all(node in nodes for node in starting_nodes),\
            "The starting_states must be in nodes."
        assert all(node in nodes for node in goal_nodes),\
            "The goal states must be in nodes."

        self.nodes = nodes
        self.locations = locations
        self.edges = edges
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
        self.estimates = estimates
        
    def outgoing_arcs(self, node):
        arcs = []
        for edge in self.edges:
            tail, head = edge
            x1 = self.locations[tail][0]
            y1 = self.locations[tail][1]
            x2 = self.locations[head][0]
            y2 = self.locations[head][1]
            cost = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            
            if tail == node and Arc(tail, head, str(tail) + '->' + str(head), cost) not in arcs:
                arcs.append(Arc(tail, head, str(tail) + '->' + str(head), cost))
            if head == node and Arc(head, tail, str(head) + '->' + str(tail), cost) not in arcs:
                arcs.append(Arc(head, tail, str(head) + '->' + str(tail), cost))
        return sorted(arcs, key=lambda x: (x[0],x[1]))
        
def main():
    # Test 0
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
        
    print('8'*25)
        
    # Test 1
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
        
    print('8'*25)
        
    # Test 2
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
    
if __name__ == "__main__":
    main()