from search import *

class RoutingGraph(Graph):
    def __init__(self, map_str):
        self.

def main():
    print('Example 1')
    map_str = """\
    +-------+
    |  9  XG|
    |X XXX  |
    | S  0FG|
    +-------+
    """
    
    graph = RoutingGraph(map_str)
    
    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at starting states:")
    for s in sorted(graph.starting_nodes()):
        print(s)
        for arc in graph.outgoing_arcs(s):
            print ("  " + str(arc))
    
    node = (1,1,5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
    
    node = (1,7,2)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
    
    node = (3, 7, 0)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    
    node = (3, 7, math.inf)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    
    node = (3,6,5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
    
    node = (3,6,9)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
    
    print()
    print('Example 2')
    map_str = """\
    +--+
    |GS|
    +--+
    """
    
    graph = RoutingGraph(map_str)
    
    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at the start:")
    for start in graph.starting_nodes():
        for arc in graph.outgoing_arcs(start):
            print ("  " + str(arc))
    
    
    
    node = (1,1,1)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
    
    print()
    print('Example 3')
    map_str = """\
    +------+
    |S    S|
    |  GXXX|
    |S     |
    +------+
    """
    
    graph = RoutingGraph(map_str)
    print("Starting nodes:", sorted(graph.starting_nodes()))    

if __name__ == '__main__':
    main()