from data_key_handler import DataHandler

class Node:
    '''
    Class Node  represents a single Node of Btree

    Attributes:
        max_num_of_keys  -  maximum keys/objects which can be stored in node of Btree
        debug_mode  - enables debug logging for testing tree operations
        keys - list of keys/objects
        parent  - reference to the parent Node
        children - list of children in the node
        NUM_OF_NODES_IN_TREE - counter of the nodes in Btree (not used in my implementation for now)
        name - representation of a node. Cane be used to identify the node

    Methods:
        __init__ - creating a Object Node with given attributes
        is_leaf_- checks if   node is leaf DYNAMICALLY
        num_of_keys_in_node  checks number of keys in node DYNAMICALLY
    '''
    NUM_OF_NODES_IN_TREE = 0
    def __init__(self, t: int, parent = None):
        self.max_num_of_keys = 2*t -1
        self.debug_mode = True
        self.keys = []
        self.parent = parent
        self.children = []
        Node.NUM_OF_NODES_IN_TREE += 1
        self.name = (f"Node_{Node.NUM_OF_NODES_IN_TREE}, \n  and my parent is {self.parent},\n "
                     f"My keys: {self.keys}")

    #def check_data(self):pas
    '''
    def update_leaf(self):
        if len(self.children) >0:
            self.is_leaf = False
    '''
    @property
    def num_of_keys_in_node(self) -> int:
        return len(self.keys)

    @property
    def is_leaf_(self) -> bool:
        return len(self.children) == 0












