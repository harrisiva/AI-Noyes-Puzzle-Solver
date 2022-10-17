from dataStructures import *
from itertools import permutations
import time

def debug(node:Node):
    print(node)
    print(f'Path Cost: {node.pcost} Heuristic: {node.heuristic} Evaluative Function: {node.evaluef} Dp: {get_disorder_parameter(node.state.state)}')
    return

GOAL_STATE = [0,1,2,3,4,5,6,7,8]
def graph_search(initial_state:Node):
    frontier: Frontier = Frontier() # Initialize the frontier
    frontier.insert(initial_state) 
    EXPLORED_SET = [] # Initialize the explored set to be empty
    while True:
        if frontier.is_empty(): return False
        leaf_node: Node = frontier.pop() # Choose a leaf node and remove it from the frontier
        if leaf_node.state.state==GOAL_STATE: return leaf_node
        EXPLORED_SET.append(leaf_node)
        children: list = expand_state(leaf_node)
        for child in children:
            if frontier.contains(child)!=True and is_in(EXPLORED_SET,child)!=True: frontier.insert(child)


# Generate all permutations, given the goal state. Filter by disorder parameter.
initial_states = [list(permutation) for permutation in permutations(GOAL_STATE) if (get_disorder_parameter(list(permutation))%2==0)]
# Select the first hundered (or sort, possibly using the same insort right algo, by smallest to largest disorder parameter and then select the first 100) and convert them to nodes
initial_state_nodes=[Node(state) for state in initial_states[1:101]] # The first one is the goal state



def count_of(solution:Node):
    count = 0
    while solution!=None:
        count += 1
        solution=solution.parent
    return count


for initial_node in initial_state_nodes:
    debug(initial_node)
    solution = graph_search(initial_node)
    if solution!=False: print(f'Solution Cost: {count_of(solution)}\n')


"""
start_time = time.time()
solution = graph_search(Node(initial_state))
end_time = time.time()
if solution!=False:
    count = 0
    while solution!=None:
        solution=solution.parent
        count += 1
    print(count)
    print(end_time-start_time)
"""