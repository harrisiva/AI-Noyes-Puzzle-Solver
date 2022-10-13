import math
from copy import deepcopy

GOAL_STATE = [0,1,2,3,4,5,6,7,8]
def heuristic1(state_data:list)->int:
    count=0
    for i in range(0,len(state_data),1):  # Ignore the Blank in the sample state
        if state_data[i]!=0:
            if state_data[i]!=GOAL_STATE[i]:
                count+=1
    return count

heuristicFunc = heuristic1 # Change this when you run the code to swtich from h1 to h2 or h3

# NOTE: The state class is only accessed by the Node class (not accessed directly in the driver)
class State:
    def __init__(self,state:list): # Given a state as a list of integers, this method initializes the object by calculating the n (rows/cols) and i (index of the blank-0)
        self.state:list = state
        self.n = int(math.sqrt(len(self.state)))
        self.i = self.state.index(0)
        return

    def derive(self,action)->list: # Given an action, this method returns a new state based on the current objects state as a list
        action_shifts={0:-self.n,1:+self.n,2:-1,3:+1} # shifts of the index based on the applied action
        # perform given action using the index shifts as calcualted in the action_shifts
        state:list = deepcopy(self.state) # create a copy of the current objects state (to avoid changing the values it holds)
        temp = state[self.i+action_shifts[action]] # create a temp variable with the value in the shift location
        state[self.i+action_shifts[action]]=state[self.i] # move the blank to the index obtained from action_shift
        state[self.i]=temp # replace the original blanks index with the value stored in temp (original value at state[action_shift[action]])
        return state

    def expand(self)->list: # returns a list of valid states as lists with data (using the derive method)
        state:list = deepcopy(self.state) # create a copy of the current objects state (to avoid changing the values it holds)
        expanded:list = []
        if not 0<=self.i<=(self.n-1): expanded.append(self.derive(0)) # action=Up
        if not (len(state)-self.n)<=self.i<=(len(state)-1): expanded.append(self.derive(1)) # action=Down
        if not self.i%self.n==0: expanded.append(self.derive(2)) # action=Left
        if not self.i%self.n==2: expanded.append(self.derive(3)) #action=Right
        return expanded

    # This function can later be used to produce the GUI
    # NOTE: Bug right now but this function is used to view the list as a 2d matrix
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

class Node: # This is the object that will be placed in the tree. It contains a State attribute followed by the parent state, pcost, and the heuristic evaluation
    def __init__(self,state:list):
        self.state:State = State(state)

        # Tree data
        self.parent: Node = None
        self.children:list = [] # Contains a list of nodes

        # Heuristic data (NOTE: Change default from none to -1 or something that takes less memory)
        self.heuristic: int = heuristicFunc(self.state.state)
        self.pcost: int = 0 # Path cost for the root node
        self.evaluef: int = self.heuristic + self.pcost        
        return
    
    def __str__(self):
        return self.state.view()


class Frontier: # A Frontier (has a list that is ordered from lowest to highest eval)
    def __init__(self):
        self.nodes = []
        return

    def is_empty(self): return len(self.nodes)==0 #NOTE: This function is mainly here to guide is when we translte it to C++
    
    def pop(self): # gives the front node (node with the lowest eval)
        node = self.nodes[0]
        self.nodes = self.nodes[1:]
        return node

    def insert(self, node:Node): 
        """Insert item x in list a, and keep it sorted assuming a is sorted.
        If x is already in a, insert it to the right of the rightmost x.
        Optional args lo (default 0) and hi (default len(a)) bound the
        slice of a to be searched.
        """
        if self.is_empty():
            self.nodes.append(node)
        else:
            lo, hi = 0, len(self.nodes) # Rather than taking these as inputs, we can just define them here (no real difference, but we can turn this into one sort function)
            while lo < hi: # Looped to keep narrowing the indexes untill you find the spot
                mid = (lo+hi)//2 # Floor division
                if node.evaluef < self.nodes[mid].evaluef:
                    hi = mid
                else:
                    lo = mid+1
            self.nodes.insert(lo, node) # We need to rewrite this in C++
        return

    def view(self): # Prints each nodes state from the frontier
        for node in self.nodes:
            print(node)
            print('--'*10)
        return

    def contains(self,node:Node)->bool: # checks if the given node is already a part of the frontier, if true, return true, else false
        does_contain=False
        for nodes in self.nodes:
            if nodes.state.state==node.state.state:
                does_contain = True
        return does_contain

    def __str__(self): # [evaluef of 1,.....,evaluef of n-1,]
        to_return = ""
        for node in self.nodes: to_return+=f'{str(node.evaluef)},'
        return f'[{to_return}]'

class Tree:
    def __init__(self, root:Node):
        self.root = root # The children for the root node are stored within the root nodes .nodes list
        self.nodes = [] # A list of all the nodes in the tree (Appended in order of three restrictions (max 4 children))
        return
    def __str__(self): # NOTE: Refine this method later, we will rarely need to print the tree itself, just there for logic purposes
        for node in self.nodes:
            print(node)
        return

# Given a Node, this function expands it (generating valid states) and returns them as a list of nodes (where the child.parent is mapped to node and the child node gets appended to parent.children
def expand_state(parent_node:Node)->list:
    # Expand the nodes, set their parent fields, and update the parents children field
    # Also add the nodes to the frontier which will use their Node.eval to sort the list
    expanded_nodes = []
    expanded_states:list = parent_node.state.expand() 
    for state in expanded_states:
        state: State = state # redeclared variable with type for ease of development
        child_node: Node = Node(state)
        child_node.parent = parent_node
        child_node.pcost = parent_node.pcost+1
        child_node.evaluef = child_node.pcost+child_node.heuristic
        parent_node.children.append(child_node)
        expanded_nodes.append(child_node)
    return expanded_nodes

# Function to calculate the disorder parameter
def get_disorder_parameter(state:list)->int: # Calculate the disorder parameter of the given state
    dp = 0
    for i in range(0,len(state)-1,1): # Dont need to bother with the last element as there are no elements in front of it (so you subtract one from the length)
        for j in range(i+1,len(state),1): # Dont need to check the current number with itself (so you add 1 to i)
            dp = dp+1 if (state[i]-state[j])>0 else dp # if the difference is positive, that means state[i]>state[j], in that case increment it by 1
    return dp

def is_in(EXPLORED_SET: list,  given_node:Node):
    given_node:list = given_node.state.state
    is_inside = False
    for node in EXPLORED_SET:
        node = node.state.state
        if node==given_node:
            is_inside=True
    return is_inside