from search import *
import heapq
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


class LCFSFrontier(Frontier):

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty prioity queue."""
        self.container = []
        self.entry_count = 0
        #heapq.heapify(self.container)

    def add(self, path):
        totalcst = 0
        for arc in path:
            totalcst += arc[-1]
        heapq.heappush(self.container, (totalcst, self.entry_count, path))
        self.entry_count += 1
        #self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return heapq.heappop(self.container)[-1]
            #return self.container.pop(0)
        else:
            raise StopIteration   # don't change this one
        
        
def main():
    # test 0
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
    
    #test 1
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
    
    #test 2
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
    
    #test 3
    graph = LocationGraph(nodes=set('ABCDG'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (0, 3),
                                     'D': (3, 3),
                                     'G': (4, 4)},
                          edges={('A', 'B'), ('C', 'A'), ('B','D'), ('C','D'),
                                 ('D', 'G')},
                          starting_nodes=['A'],
                          goal_nodes={'G'})
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)    
        
    
if __name__ == "__main__":
    main()