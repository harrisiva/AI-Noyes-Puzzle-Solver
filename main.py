from dataStructures import Frontier, Node, expand_state

EXPLORED = []

frontier = Frontier()

# Create a node for the initial state and display it on the screen (NOTE: For testing purposes)
istate = Node([1,2,3,4,0,5,6,7,8])
frontier.view()
expanded = expand_state(istate)
EXPLORED.append(istate.state)

for node in expand_state(istate):
    node:Node = node
    frontier.insert(node)
    print(node)
    print(f'h1: {node.heuristic} | pcost: {node.pcost} | evalf: {node.evaluef}')
    print()

print()
for node in frontier.nodes:
    node: Node = node
    print(node.evaluef)

# Expand the initial state and add them as the children to the current node (and set the childrens parent as the current node)
#NOTE: Might also need to set their path cost (child.pcost=parent.pcost+1)

# TODO: Explored (can be kept in main?) 
# TODO: Tree