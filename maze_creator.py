import sys
import math
import random

# drawing a graph with no connections should produce a grid
def gen_sq_graph(dim):
    mat = [[]]
    for i in range(0, dim):
        for j in range(0, dim):
            mat[i][j]


def print_grid(dim):
    print("\u001b[33m")
    for x in range(0, dim):
        print("+ - " * dim + "+")
        print("|   " * dim + "|")

    print("+ - " * dim + "+")
    print("\u001b[0m")


# Assuming every node is indexed in graph dictionary
def draw_maze(graph):
    """ print a grid representation of the graph"""

    nodes = len(graph)
    dim = int(math.sqrt(nodes))  # handle error where not int

    # Draw the grid upper border
    print("+ - " * dim, end="+\n")
    for i in range(0, dim):
        verts = "|"
        horzs = "+"
        for j in range(0, dim):
            node = i * dim + j
            arcs = list(filter(lambda x: x > node, graph[node]))
            
            # If connected to next node along, don't draw grid line
            verts += "    " if node + 1 in arcs else "   |"
            
            # If connected to node in square below, don't draw grid line
            horzs += "   +" if node + dim in arcs else " - +"
        print(verts)
        print(horzs)


def get_row(n, dim):
    """ Get row of node is square grid """
    return n // dim


def get_col(n, dim):
    """ Get column of node in square grid """
    return n % dim


def create_grid_graph(dim):
    """ Creates adjacency list for fully connected grid """
    nodes = dim**2
    graph = {}
    for n in range(0, nodes):
        arcs = set()
         # Add square above if not first row
        if n // dim != 0: arcs.add(n - dim)
        
        # Add square to left if not first col
        if n % dim != 0: arcs.add(n - 1)
        
        # Add square to right if not last col
        if n % dim != dim - 1: arcs.add(n + 1)

        # Add square below if not last row
        if n // dim != dim - 1: arcs.add(n + dim)
        
        graph[n] = arcs
    return graph


def rand_edge_maze(dim):

    grid = create_grid_graph(dim)
    edges = grid
    maze = {}  # [range(0, dim**2)]
    visited = set()
    
    for n in range(0, dim**2):
        maze[n] = set()
    
    while len(edges) > 0:
        #print(edges)
        n1 = random.choice(list(edges.keys()))
        #print("N1:",n1)
        n2 = random.sample(edges[n1], 1)  # will break if edges[n1] is empty but it shouldn't be!! 
        #print("N2:",n2)
        n2 = n2[0]

        # Add edge to maze if either node is unvisited
        # This bit is wrong
        if not (n1 in visited and n2 in visited):
            maze[n1].add(n2)  # add to maze
       
        #print(maze)
        # Add nodes to visited set
        visited.add(n1)
        visited.add(n2)

        # remove edge from set
        edges[n1].remove(n2)
        if len(edges[n1]) == 0:
            del edges[n1]
        # repeat until edges is empty

    return maze


def generate_bfs_maze(dim):
    """ Uses randomised BFS to create a connected graph representation of maze """

    grid = create_grid_graph(dim)
    maze = []
    start = 0
    maze[start] = {}
    frontier = {start}
    frontier.update(grid[start])

    # Select a frontier node
    # Add it to maze connecion to it
    # label it visited 

# Create and draw maze taking dimension from command line
# Need better checks here obvs
dim = int(sys.argv[1]) if len(sys.argv) > 1 else 3
maze = rand_edge_maze(dim)
draw_maze(maze)


g_1 = {
    0: [1],
    1: [0, 2],
    2: [1, 5],
    3: [4, 6],
    4: [3, 5],
    5: [2, 4],
    6: [3, 7],
    7: [6, 8],
    8: [7]
    }

g_2 = {
    0: [1, 3],
    1: [1, 4],
    2: [5],
    3: [0, 6],
    4: [1, 7],
    5: [2, 8],
    6: [3],
    7: [4, 8],
    8: [5, 7]
    }


