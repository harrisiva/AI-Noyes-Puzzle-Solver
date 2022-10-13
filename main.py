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