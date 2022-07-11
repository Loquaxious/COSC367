import math
from search import *
import heapq


class RoutingGraph(Graph):
    def __init__(self, map):
        """Routing graph object constructor"""
        self.map_rep, self.starting_nodes_, self.goal_nodes = self.generate_graph(map)

    def generate_graph(self, graph_str):
        """Function that takes a string representation of a graph and generates it's list representation"""
        temp = [b.strip() for b in graph_str.splitlines()]
        map_rep = [[row for row in col] for col in temp]
        agents, call_points = [], []
        location = namedtuple('location', 'x,y,cost')
        for col in range(len(map_rep)):
            for row in range(len(map_rep[col])):
                if map_rep[col][row] == 'S':
                    agents.append(location(col, row, math.inf))
                elif map_rep[col][row] == 'G':
                    call_points.append(location(col, row, 0))
                elif map_rep[col][row].isdigit():
                    agents.append(location(col, row, int(map_rep[col][row])))
        return map_rep, agents, call_points

    def is_goal(self, node):
        """Returns true if the candidate node happens to be a goal node"""
        result = False
        for candidate in self.goal_nodes:
            if node[0] == candidate.x and node[1] == candidate.y:
                result = True
        return result

    def convert_to_tuple(self, _tuple):
        """Returns a tuple representation of the given node"""
        return (_tuple.x, _tuple.y, _tuple.cost)

    def starting_nodes(self):
        """Returns all the starting nodes of the given graph"""
        return [self.convert_to_tuple(i) for i in self.starting_nodes_]

    def outgoing_arcs(self, tail_node):
        """Returns all the outgoing arcs of the given node"""
        arcs = []
        valid_actions = ['S', 'G', ' ', 'F']
        directions = [('N', -1, 0),
                      ('E', 0, 1),
                      ('S', 1, 0),
                      ('W', 0, -1)]
        y, x = tail_node[0], tail_node[1]
        for action, dy, dx in directions:
            candidate = self.map_rep[y + dy][x + dx]
            if (candidate in valid_actions or candidate.isdigit()) and tail_node[2] - 1 >= 0:
                arcs.append(Arc(tail_node, (y + dy, x + dx, tail_node[2] - 1), action, 5))
        if self.map_rep[y][x] == 'F' and tail_node[2] < 9:
            arcs.append(Arc(tail_node, (y, x, 9), 'Fuel up', 15))

        return arcs

    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given state"""
        if node in self.goal_nodes:
            return 0

        if node is None:
            return 0

        method = lambda x1, x2, y1, y2: abs(x1 - x2) + abs(y1 - y2)
        pool = []
        n_row = node[0]
        n_col = node[1]
        for grow, gcol, _ in self.goal_nodes:
            pool.append(method(n_col, gcol, n_row, grow))
        result = min(pool) * 5

        return result


class AStarFrontier(Frontier):
    def __init__(self, map_graph):
        """AStarFrontier class constructor"""
        self.container = []
        self.map_graph = map_graph
        self.candidate_count = 0
        self.priority = {}
        self.clippers = set()
        heapq.heapify(self.container)

    def make_heap_key(self, cost):
        """Creates a heap key from the given cost"""
        if cost in self.priority:
            self.priority[cost] += 1
            return cost, self.priority[cost]
        self.priority[cost] = 0
        return cost, self.priority[cost]

    def make_prune_key(self, arc_):
        """Creates a prune key from the given arc"""
        return arc_.head[0], arc_.head[1], arc_.head[2]

    def add(self, path):
        """Calculates the estimated cost to the goal"""
        cost = sum(arc.cost for arc in path) + self.map_graph.estimated_cost_to_goal(path[-1].head)
        key = (self.make_heap_key(cost))
        heapq.heappush(self.container, (key, path))

    def add_to_clippings(self, arc_):
        """Adds the given pruned key to the clippers list"""
        self.clippers.add(self.make_prune_key(arc_))

    def clip_check(self, arc_):
        """Returns true if a pruned key is in the clippers, false otherwise"""
        if arc_.tail is not None:
            return (self.make_prune_key(arc_)) in self.clippers
        return False

    def __next__(self):
        """Iterates through all the candidates"""
        while len(self.container) > 0:
            self.candidate_count += 1
            candidate = heapq.heappop(self.container)[1]
            if not (self.clip_check(candidate[-1])):
                self.add_to_clippings(candidate[-1])
                return candidate
        raise StopIteration

def main():
    
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
    
    print(frontier.clippers)
    
    #print()
    #print('Test 11:')
    #print()       
    
    #map_str = """\
    #+-----+
    #|S    |
    #|     |
    #|     |
    #|     |
    #|     |
    #|2  G |
    #| F   |
    #+-----+
    #"""    
    #map_graph = RoutingGraph(map_str)
    #frontier = AStarFrontier(map_graph)
    #solution = next(generic_search(map_graph, frontier), None)
    #print_actions(solution)      
    

if __name__ == '__main__':
    main()