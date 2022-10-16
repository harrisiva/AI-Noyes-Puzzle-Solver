from dataStructures import *

node = [6,1,3,5,8,7,4,0,2]

def debug(node:Node):
    print(node)
    print(f'Path Cost: {node.pcost} Heuristic: {node.heuristic} Evaluative Function: {node.evaluef}')
    return

expanded = expand_state(Node(node))
debug(expanded[0])
debug(expanded[1])
debug(expanded[2])