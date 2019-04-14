import random
from maze_helpers import create_grid_graph


def prims_maze(dim):
    """
    Create maze using prims algorithm. Set of seen nodes.
    """

    # Edges starts as adjancency list of full gird
    edges = create_grid_graph(dim)
    # Algorithm can start at arbitrary node in the tree
    n1 = random.choice(list(edges.keys()))

    visited = {n1}
    explored = set()  # Nodes for which every edge has been considered

    maze = {}
    for n in range(0, dim**2):
        maze[n] = set()

    while len(edges) > 0:

        # Choose random visited node with unexplored edges
        # Choose edge at random end get adjacent node
        n1 = (random.sample(visited.difference(explored), 1))[0]
        n2 = (random.sample(edges[n1], 1))[0]

        # Add edge to maze if the unexplored edge led to unvisited node
        if n2 not in visited.union(explored):
            maze[n1].add(n2)
            maze[n2].add(n1)
            visited.add(n2)

        # Remove edge from set of unexplored edges
        edges[n1].remove(n2)

        # Mark start node if now fully explored
        if len(edges[n1]) == 0:
            del edges[n1]  # redundant
            explored.add(n1)

    return maze
