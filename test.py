from dataStructures import *

state = Node([0,2,3,1,4,5,6,7,8,9,10,11,12,13,14,15])
print(state)
print()
expanded = expand_state(state)
for node in expanded:
    print(node)
    print()