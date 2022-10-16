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

# Logic following slide 27 from m3-search
# ---------------------------------------
# Pick the first node from the initial state nodes to set as this iterations initial state
initial_node = initial_state_nodes[1] # [0] is the goal state
print(initial_node.state.state)
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
            derived_node:Node = derived_node
            if frontier.contains(derived_node)!=True and is_in(EXPLORED_SET,derived_node)!=True:
                frontier.insert(derived_node)

# If solution==True
# Create a list of the parent nodes, flip it, and print the steps
if solution:
    print("SOLUTION FOUND!!!")
    solution_steps = []
    parent_node = node.parent
    while node!=None:
        solution_steps.append(node)
        node = node.parent
    solution_steps = solution_steps[::-1] # Flip the nodes (alternative is to pre-pend)
    
    # Print the solution
    print("initial state:")
    print(initial_node)
    print('--------')
    print("Root:")
    for nodes in solution_steps:
        nodes:Node = nodes
        print(nodes) # Represent this as a GUI and we're doneeee with 3x3!!!
        print('--------')
    print(len(solution_steps))