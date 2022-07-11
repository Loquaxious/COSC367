from search import *
import re
import math

class RoutingGraph(Graph):
    def __init__(self, map_str):
        AGENT = r'[0-9]'
        self.agents = []
        self.obstacles = []
        self.customers = []
        self.fuel = []
        map_lst =  map_str.strip().split('\n')
        for i in range(len(map_lst)):
            map_lst[i] = map_lst[i].strip()
        self.map_lst = map_lst
        
        h = len(map_lst)
        w = len(map_lst[0])
        
        for i in range(h):
            for j in range(w):
                if i == 0 or i == h-1 or j == 0 or j == w-1:
                    continue
                if map_lst[i][j] == 'S': 
                    self.agents.append((i, j, float('inf')))
                elif re.match(AGENT, map_lst[i][j]):
                    self.agents.append((i, j, int(map_lst[i][j])))
                elif map_lst[i][j] == 'X':
                    self.obstacles.append((i, j))
                elif map_lst[i][j] == 'G':
                    self.customers.append((i, j))
                elif map_lst[i][j] == 'F':
                    self.fuel.append((i, j))
                
    
    def starting_nodes(self):
        return self.agents
        
    def is_goal(self, node):
        row, col, fuel = node
        return (row, col) in self.customers

    def outgoing_arcs(self, node):
        directions = [('N' , -1, 0),
                      ('E' ,  0, 1),
                      ('S' ,  1, 0),
                      ('W' ,  0, -1),]
        row, col, fuel = node
        arcs = []
        for i in range(4):           
            direction, dir_row, dir_col = directions[i]
            if fuel == float('inf'):
                n_move = (int(row) + int(dir_row), \
                          int(col) + int(dir_col), fuel)
            else:
                n_move = (int(row) + int(dir_row), \
                          int(col) + int(dir_col), int(fuel) - 1)
            if (n_move[0] < len(self.map_lst)-1 and n_move[0] > 0) and \
               (n_move[1] < len(self.map_lst[0])-1 and n_move[1] > 0):
                if (n_move[0], n_move[1]) not in self.obstacles and fuel > 0:
                    arcs.append(Arc(node, n_move, direction, 5))
        
        if (row, col) in self.fuel and fuel < 9: 
            arcs.append(Arc(node, (row, col, 9), 'Fuel up', 15)) 
            
        return arcs
    
    def estimated_cost_to_goal(self, node):
        agnt_row, agnt_col, fuel = node
        results = []
        
        for goal_row, goal_col in self.customers:
            results.append(abs(agnt_row - goal_row) + abs(agnt_col - goal_col))
        
        return min(results)
        
        


def main():
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
    print('Test 2')
    print()
    
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
    print('Test 3')
    print()
    
    map_str = """\
    +------+
    |S    S|
    |  GXXX|
    |S     |
    +------+
    """
    
    graph = RoutingGraph(map_str)
    print("Starting nodes:", sorted(graph.starting_nodes()))        

if __name__ == "__main__":
    main()