from dataStructures import *

node = [6,1,3,5,8,7,4,0,2]

def debug(node:Node):
    print(node)
    print(f'Path Cost: {node.pcost} Heuristic: {node.heuristic} Evaluative Function: {node.evaluef}')
    return

frontier = Frontier()

expanded = expand_state(Node(node))

parent = Node(node)
frontier.insert(parent)
debug(parent)
print(frontier)

node1 = expanded[0]
debug(node1)
frontier.insert(node1)
print(frontier)

node2 = expanded[1]
debug(node2)
frontier.insert(node2)
print(frontier)

node3 = expanded[2]
debug(node3)
frontier.insert(node3)
print(frontier)


expanded2 = expand_state(node3)

node4 = expanded2[0]
debug(node4)
frontier.insert(node4)
print(frontier)

node5 = expanded2[1]
debug(node5)
frontier.insert(node5)
print(frontier)


# Testing the frontier pop function
print("Testing the pop function")
pop1 = frontier.pop()
debug(pop1)
print(frontier)

pop1 = frontier.pop()
debug(pop1)
print(frontier)

pop1 = frontier.pop()
debug(pop1)
print(frontier)

pop1 = frontier.pop()
debug(pop1)
print(frontier)

pop1 = frontier.pop()
debug(pop1)
print(frontier)

pop1 = frontier.pop()
debug(pop1)
print(frontier)