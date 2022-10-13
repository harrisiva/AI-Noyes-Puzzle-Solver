# Driver for 3x3
from dataStructures import *
from itertools import permutations

# Set the goal state
GOAL_STATE = [0,1,2,3,4,5,6,7,8]
# Create a list to keep track of the explored nodes (check using is_in)
EXPLORED_SET = []


# Generate all permutations, given the goal state. Filter by disorder parameter.
initial_states = [list(permutation) for permutation in permutations(GOAL_STATE) if (get_disorder_parameter(list(permutation))%2==0)]
# Select the first hundered (or sort, possibly using the same insort right algo, by smallest to largest disorder parameter and then select the first 100) and convert them to nodes
initial_state_nodes=[Node(state) for state in initial_states[:100]] # The first one is the goal state

"""
root_node = initial_state_nodes[1]
# Initialize the tree using the root node
tree = Tree(root_node)
# Intiailzie the frontier
frontier = Frontier()

current_node = root_node # Set the root node as the current node

print(current_node)
if current_node.state.state==GOAL_STATE: # If the current node is the goal state, end script
    print("GOAL STATE")
    # Go to the next node in the intiail_state_nodes
else:
    # Expand the node
    nodes_children = expand_state(current_node)
    # Add the current node to the explored nodes list
    EXPLORED_SET.append(current_node)
    # Add the expanded nodes to the frontier if its not already in the frontier and if its not in the frontier or explored list already
    for node in nodes_children:
        if frontier.contains(node)!=True and is_in(EXPLORED_SET,node)!=True:
            frontier.insert(node)

    # Pop a node from the frontier and repeat the following
    print(frontier)
    print(EXPLORED_SET)
    print(frontier.pop())
    print(frontier)
    print(frontier.pop())
    print(frontier)

"""


# Logic following slide 27 from m3-search
# ---------------------------------------
# Pick the first node from the initial state nodes to set as this iterations initial state
initial_node = initial_state_nodes[1] # [0] is the goal state
# Initialize the frontier using the intiailize state
frontier = Frontier()
frontier.insert(initial_node)
EXPLORED_SET = []

solution = False
while solution==False:
    if frontier.is_empty(): # if the frontier is empty, then return failure
        solution=False
        break # Return failure
    # Choose a leaf node (unexplored) and remove it from the frontier
    node:Node = frontier.pop()
    if node.state.state==GOAL_STATE:
        solution=True
        # reutrn solution (backtrack the parent sequence onto a list and flip the list)
    else:
        expanded:list = expand_state(node)
        EXPLORED_SET.append(node)
        for derived_node in expanded:
            derived_node: Node = derived_node
            if frontier.contains(derived_node)!=True and is_in(EXPLORED_SET,derived_node)!=True:
                frontier.insert(derived_node)

print(solution)
print(node)
# If solution==True
# Create a list of the parent nodes, flip it, and print the steps
