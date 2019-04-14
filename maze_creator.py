import sys
from prims import prims_maze
from maze_helpers import draw_maze
# Create and draw maze taking dimension from command line
# Need better checks here obvs

dim = int(sys.argv[1]) if len(sys.argv) > 1 else 3

maze = prims_maze(dim)
draw_maze(maze)



#  def print_grid(dim):
#   print("\u001b[33m")
#    for x in range(0, dim):
#        print("+ - " * dim + "+")
#        print("|   " * dim + "|")

#    print("+ - " * dim + "+")
#    print("\u001b[0m")
