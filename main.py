from dataStructures import *
from itertools import permutations
import time
import numpy
import datetime as dt

def debug(node:Node):
    print(node)
    print(f'Path Cost: {node.pcost} Heuristic: {node.heuristic} Evaluative Function: {node.evaluef} Dp: {get_disorder_parameter(node.state.state)}')
    return

GOAL_STATE = [0,1,2,3,4,5,6,7,8]
def graph_search(initial_state:Node, EXPLORED_SET:list):
    frontier: Frontier = Frontier() # Initialize the frontier
    frontier.insert(initial_state) 
    start = dt.datetime.now()
    while True:
        update_time = time.time()
        if frontier.is_empty(): return False
        leaf_node: Node = frontier.pop() # Choose a leaf node and remove it from the frontier
        if leaf_node.state.state==GOAL_STATE: return leaf_node
        EXPLORED_SET.append(leaf_node)
        children: list = expand_state(leaf_node)
        for child in children:
            if frontier.contains(child)!=True and is_in(EXPLORED_SET,child)!=True: 
                frontier.insert(child)
        update = dt.datetime.now()
        if (update-start>dt.timedelta(seconds=60)):
            return False


# Generate all permutations, given the goal state. Filter by disorder parameter.
#initial_states = [list(permutation) for permutation in permutations(GOAL_STATE) if (get_disorder_parameter(list(permutation))%2==0)]
# Select the first hundered (or sort, possibly using the same insort right algo, by smallest to largest disorder parameter and then select the first 100) and convert them to nodes
#set_1 = [Node(state) for state in initial_states[1:100000]]

#print(len(set_1))

#initial_state_nodes=[Node(state) for state in initial_states[1:101]] # The first one is the goal state

# Required Data:
# Number of steps to find the solution
# Number of nodes expanded by A* in each case

def load():
    initial_states = []
    with open('states3.txt','r') as file: lines = file.readlines()
    for line in lines: initial_states.append(Node(list(map(int, (line.replace('\n','')).split(',')))))
    return initial_states

initial_states = load()
set_ = initial_states #set_1
with open('logh3.txt','w') as file:
    for i in range(0,len(set_),1):
        EXPLORED_SET = []
        solution = graph_search(set_[0],EXPLORED_SET)
        if isinstance(solution,bool)!=True:
            file.write(f'{i}){solution.pcost},{len(EXPLORED_SET)},{set_[i].state.state}\n')
            print(f'{i}) Solved {set_[i].state.state}')
        else: print(f'{i}) Timed out')