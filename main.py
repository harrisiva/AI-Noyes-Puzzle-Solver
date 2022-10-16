from dataStructures import *
import time

# I believe the loop might be wrong, we need to start of by rewriting it and then trying to reduce the number of iterations for the ss i sent to the GC

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


initial_state = [7,2,4,5,0,6,8,3,1]
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