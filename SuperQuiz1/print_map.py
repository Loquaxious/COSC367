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
        agnt_row, agnt_col, fuel = node
        
        if (agnt_row, agnt_col) in self.customers:
            return 0
        
        results = []
        
        for goal_row, goal_col in self.customers:
            results.append(abs(agnt_row - goal_row) + abs(agnt_col - goal_col))
        
        return min(results) * 5


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
            if candidate[-1][1] not in self.pruned:
                self.pruned.add(candidate[-1][1])
                return candidate
        raise StopIteration   # don't change this one
    
def print_map(map_graph, frontier, solution):
    """Prints a string representation of a given graph."""
    map_lst = []
    for row in map_graph.map_lst:
        map_lst.append(list(row))
    for x, y, _ in frontier.pruned:
        map_lst[x][y] = '.'    
    if solution is not None:
        for direction in solution:
            x, y, _ = direction[1]
            map_lst[x][y] = '*'
    for node in map_graph.agents:
        x, y, _ = node
        map_lst[x][y] = 'S'
    for node in map_graph.customers:
        x, y = node
        map_lst[x][y] = 'G'        
    for row in map_lst:
        print(''.join(row))

def main():
    
    print()
    print('Test 1:')
    
    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)  
    
    print()
    print('Test 2:') 
    
    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """
    
    
    map_graph = RoutingGraph(map_str)
    # changing the heuristic so the search behaves like LCFS
    map_graph.estimated_cost_to_goal = lambda node: 0
    
    frontier = AStarFrontier(map_graph)
    
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)  
    
    print()
    print('Test 3:')     
    
    map_str = """\
    +-------------+
    | G         G |
    |      S      |
    | G         G |
    +-------------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)  
    
    print()
    print('Test 4:')
    
    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    |  S    |
    +-------+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)    
    
    print()
    print('Test 5:')    
    
    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)    
    
    print()
    print('Test 6:')    
    
    map_str = """\
    +----+
    |    |
    | SX |
    | X G|
    +----+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)  
    
    print()
    print('Test 7:')   
    
    map_str = """\
    +---------------+
    |    G          |
    |XXXXXXXXXXXX   |
    |           X   |
    |  XXXXXX   X   |
    |  X S  X   X   |
    |  X        X   |
    |  XXXXXXXXXX   |
    |               |
    +---------------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)    
    
    print()
    print('Test 8:')       
    
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
    print_map(map_graph, frontier, solution)    
    
if __name__ == "__main__":
    main()