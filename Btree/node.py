from data_key_handler import DataHandler

class Node:
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












