import math
from copy import deepcopy

# NOTE: The state class is only accessed by the Node class (not accessed directly in the driver)
class State:
    def __init__(self,state:list):
        self.state = state
        self.n = int(math.sqrt(len(self.state)))
        self.i = self.state.index(0)
        return

    def derive(self,action)->list:
        action_shifts={0:-self.n,1:+self.n,2:-1,3:+1} # shifts of the index based on the applied action
        # perform given action using the index shifts as calcualted in the action_shifts
        state:list = deepcopy(self.state) # create a copy of the current objects state (to avoid changing the values it holds)
        temp = state[self.i+action_shifts[action]] # create a temp variable with the value in the shift location
        state[self.i+action_shifts[action]]=state[self.i] # move the blank to the index obtained from action_shift
        state[self.i]=temp # replace the original blanks index with the value stored in temp (original value at state[action_shift[action]])
        return state

    def expand(self)->list: # returns a list of valid states as lists with data
        state:list = deepcopy(self.state) # create a copy of the current objects state (to avoid changing the values it holds)
        expanded:list = []
        if not 0<=self.i<=(self.n-1): expanded.append(self.derive(0)) # action=Up
        if not (len(state)-self.n)<=self.i<=(len(state)-1): expanded.append(self.derive(1)) # action=Down
        if not self.i%self.n==0: expanded.append(self.derive(2)) # action=Left
        if not self.i%self.n==2: expanded.append(self.derive(3)) #action=Right
        return expanded

    # This function can later be used to produce the GUI
    # NOTE: Bug right now (but I have working code elsewhere, need to integrate it)
    def view(self)->str: 
        state = deepcopy(self.state) # done to avoid any changes to the actual state
        srepresentation: str = "" # String representation of the state
        row = []
        for i in range(0,len(state),1):
            row.append(state[i])
            srepresentation+=f'{state[i]} '
            if i%self.n==self.n-1:
                #print(row)
                srepresentation+='\n' if i!=len(state)-1 else ''
                row=[]
        return srepresentation

class Node:
    def __init__(self,state:list):
        self.state:State = State(state)
        self.parent:State= None
        self.pcost: int = None # Path cost
        return
    
    def expand(self): # Returns a list of the nodes states expansions (derived by applying all legal action)
        expanded_states = self.state.expand()
        return expanded_states
    
    def __str__(self):
        return self.state.view()

class Frontier: # A Frontier (has a list that is ordered based on the evaluative function)
    def __init__(self):
        self.nodes = []
        return
    def is_empty(self):
        return
    def pop(self): # gives the front node
        return
    def insert(self, node:Node):
        # get the sum of the heuristic and the g(n) and insert it with that
        # run the node through the evaluative function g(n) + h(n)
        return

frontier = Frontier() # Initialize a fronter list
istate = Node([1,2,3,4,0,5,6,7,8])  # Initial State
print(istate,'\n------\n')
expanded_states = istate.expand()
for state in expanded_states:
    expanded_node = Node(state)
    print(expanded_node)
    print()