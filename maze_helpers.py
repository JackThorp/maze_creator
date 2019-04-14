import math

def bg_str(str):
    return "\u001b[30m" + str + "\u001b[0m"

def fg_str(str):
    return "\u001b[45m" + str + "\u001b[0m"

# Assuming every node is indexed in graph dictionary
def draw_maze(graph):
    """ print a grid representation of the graph"""

    nodes = len(graph)
    dim = int(math.sqrt(nodes))  # handle error where not int

    # Draw the grid upper border
    print(bg_str("+ - ") * dim, end=bg_str("+\n"))
    for i in range(0, dim):
        verts = bg_str("|")
        horzs = bg_str("+")
        for j in range(0, dim):
            node = i * dim + j
            arcs = list(filter(lambda x: x > node, graph[node]))
            
            # If connected to next node along, don't draw grid line
            verts += fg_str("    ") if node + 1 in arcs else fg_str("   ") + bg_str("|")
            
            # If connected to node in square below, don't draw grid line
            horzs += fg_str("   ") + bg_str("+") if node + dim in arcs else bg_str(" - +")
        print(verts)
        print(horzs)


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
