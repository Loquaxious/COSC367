from search import *
import re
import heapq

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
        #agnt_row, agnt_col, fuel = node
        
        #if (agnt_row, agnt_col) in self.customers:
            #return 0
        
        #results = []
        
        #for goal_row, goal_col in self.customers:
            #results.append(abs(agnt_row - goal_row) + abs(agnt_col - goal_col))
        
        #return min(results)
        return 0 # For this Q it asked for it to only return 0


class AStarFrontier(Frontier):
    def __init__(self, map_graph):
        """The constructor takes no argument. It initialises the
        container to an empty prioity queue."""
        self.container = []
        self.entry_count = 0
        self.pruned = set()
        self.map_graph = map_graph

    def add(self, path):
        if path[-1][1] in self.pruned:
            return 
        
        totalcst = 0
        for arc in path:
            totalcst += arc[-1]
        totalcst += self.map_graph.estimated_cost_to_goal(path[-1][1])
        heapq.heappush(self.container, (totalcst , self.entry_count, path))
        self.entry_count += 1

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        while len(self.container) > 0:
            candidate = heapq.heappop(self.container)[-1]
            if candidate[-1] not in self.pruned:
                self.pruned.add(candidate[-1])
                return candidate
        raise StopIteration   # don't change this one

    
def main():
    map_str = """\
    +-------+
    |   G   |
    |       |
    |   S   |
    +-------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    print()
    print('Test 2:')
    print()
    
    map_str = """\
    +-------+
    |  GG   |
    |S    G |
    |  S    |
    +-------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution) 
    
    print()
    print('Test 3:')
    print()    
    
    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    | S     |
    +-------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    print()
    print('Test 4:')
    print()  
    
    map_str = """\
    +-------+
    |  F  X |
    |X XXXXG|
    | 3     |
    +-------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)  
    
    print()
    print('Test 5:')
    print()      
    
    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    print()
    print('Test 6:')
    print()    
    
    map_str = """\
    +---+
    |GF2|
    +---+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    print()
    print('Test 7:')
    print()  
    
    map_str = """\
    +----+
    | S  |
    | SX |
    |GX G|
    +----+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution) 
    
    print()
    print('Test 8:')
    print()      
    
    map_str = """\
    +---------+
    |         |
    |    G    |
    |         |
    +---------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)  
    
    print()
    print('Test 9:')
    print()
    
    map_str = """\
    +---+
    |2 F|
    |XX |
    |X3 |
    |X X|
    |1 X|
    |2  |
    |XX |
    | XF|
    |X  |
    |   |
    |2  |
    |   |
    | G |
    +---+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)    
    
    print()
    print('Test 10:')
    print()       
    
    map_str = """\
    +----------------+
    |2              F|
    |XX     G 123    |
    |3XXXXXXXXXXXXXX |
    |  F             |
    |          F     |
    +----------------+
    """    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    print()
    print('Test 11:')
    print()       
    
    map_str = """\
    +-----+
    |S    |
    |     |
    |     |
    |     |
    |     |
    |2  G |
    | F   |
    +-----+
    """    
    map_graph = RoutingGraph(map_str)
    print(map_graph)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    

if __name__ == '__main__':
    main()