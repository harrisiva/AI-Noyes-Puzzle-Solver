# Driver for 3x3
from dataStructures import *
from itertools import permutations

# Set the goal state
GOAL_STATE = [0,1,2,3,4,5,6,7,8]

# Generate all permutations, given the goal state. Filter by disorder parameter.
initial_states = [list(permutation) for permutation in permutations(GOAL_STATE) if (get_disorder_parameter(list(permutation))%2==0)]
# Select the first hundered (or sort, possibly using the same insort right algo, by smallest to largest disorder parameter and then select the first 100) and convert them to nodes
initial_state_nodes=[Node(state) for state in initial_states[:100]] # The first one is the goal state

initial_state = initial_state_nodes[1]
# Add the node to the tree

print(initial_state)
if initial_state.state.state==GOAL_STATE:
    print("GOAL STATE")
    # Go to the next node in the intiail_state_nodes
else:
    # Expand the node
    # Add the current node to the explored nodes list
    # Add the expanded nodes to the frontier if its not already in the frontier and if its not in the frontier or explored list already
    # Pop a node from the frontier and repeat the following
    pass