

from node import Node
from data_key_handler import DataHandler
import inspect

'''
Decorator _track_operation is used to wrap methods in the Tree class
to log their actions
'''
def _track_operation(func):
    def wrapper(self, *args, **kwargs):
        if self.debug_mode:
            caller = inspect.stack()[1].function
            print(f"{func.__name__} called by {caller}")

        result = func(self, *args, **kwargs)
        return result
    return wrapper
class Tree:
    '''
    Class Tree representing Btree
    Attributes:
        root - root of the tree (Frst node tpo be created)
        t - degree of the tree
        max_num_of_keys - maximum allowed keys in the Btree
        debug_mode - if true decorated method log function calls
    Methods:
        __init__ - creating a Btree object  with given attributes
        insert_ - inserts a key into the tree, splitting nodes if necessary
        insert_non_full - inserts a key into a node that is not full
        search_key - searches for a key in the tree and returns the key/data ora node and index if called by delete
        search_key_in_node - helper function to search within a node recursively
        split - splits a full child node
        in_order_traversal - returns all keys in the tree in sorted order
        merge - merges a node with its sibling
        borrow - rebalances a node/tree,also calls merge
        borrow_from_right / borrow_from_left - helper functions for borrowing
        get_predcessor / get_scccesor - find predecessor or successor keys during deletion
        delete_key - deletes a key from the tree while maintaining B-tree properties
        print_tree - prints the tree structure in acceptable format

    '''

    def __init__(self,t: int):
        self.root = None
        self.t = t
        self.max_num_of_keys = 2*t -1
        self.debug_mode = True


    '''
    def log_acitivity(self,messege):
        if self.debug_mode:
            caller = inspect.stack()[1].function
            print(f"[{caller}] --- {messege}")
    '''
    @_track_operation
    def insert_(self,data_key):
        if self.root is None:
            self.root = Node(self.t)
            self.root.keys = [data_key]
            return

        if self.root.num_of_keys_in_node == self.max_num_of_keys:
            new_root = Node(self.t)
            old_root = self.root
            new_root.children.append(old_root)
            old_root.parent = new_root
            self.root = new_root
            self.split(new_root, 0)

        self.insert_non_full(self.root,data_key)
    @_track_operation
    def insert_non_full(self, node: Node, data_and_key: DataHandler):
        i = len(node.keys) - 1

        if node.is_leaf_:
            node.keys.append(None)
            while i >= 0 and data_and_key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = data_and_key

        else:
            while i >= 0 and data_and_key < node.keys[i]:
                i -= 1
            i += 1

            if node.children[i].num_of_keys_in_node == self.max_num_of_keys:
                self.split(node, i)
                if data_and_key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], data_and_key)

    def search_key(self, key_to_search: int):
        if self.root is None:
            print("The Root does not exist, nothing to be searched")
            return None, None
        return self.search_key_in_node(self.root, key_to_search, return_node=False)

    def search_key_in_node(self, node: Node, key: int, return_node=False):

        i = 0
        while i < len(node.keys) and key > node.keys[i].ID:
            i += 1

        if i < len(node.keys) and key == node.keys[i].ID:
            if return_node:
                return node, i
            else:
                return node.keys[i], i

        if node.is_leaf_:
            print("Key could not be found")
            return None, None

        return self.search_key_in_node(node.children[i], key, return_node)
    @_track_operation
    def split(self, parent: Node, index: int):

        t = self.t
        node_to_split = parent.children[index]


        left = Node(t,parent = parent)
        right = Node(t,parent = parent)
        middle = node_to_split.keys[t - 1]

        left.keys = node_to_split.keys[:t - 1]
        right.keys = node_to_split.keys[t:]
       # Case1: node is not a leaf
        if not node_to_split.is_leaf_:
            left.children = node_to_split.children[:t]
            right.children = node_to_split.children[t:]
           #left.update_leaf()
           # right.update_leaf()
            for child in left.children:
                child.parent = left
            for child in right.children:
                child.parent = right


        parent.keys.insert(index, middle)
        parent.children[index:index + 1] = [left, right]
        #parent.update_leaf()

        return
   # @_track_operation
    def in_order_traversal(self,node)-> []:
        if node is None:
            return []

        result = []


        for i in range(len(node.keys)):

            if i < len(node.children):
                result.extend(self.in_order_traversal(node.children[i]))

            result.append(node.keys[i])


        if node.children:
            result.extend(self.in_order_traversal(node.children[-1]))

        return result

    @_track_operation
    def merge(self, parent, node_index, sibling_index):


        left_idx = min(node_index, sibling_index)
        right_idx = max(node_index, sibling_index)


        separator = parent.keys[left_idx]
        node_to_be_merged = parent.children[left_idx]
        right_sibling = parent.children[right_idx]


        node_to_be_merged.keys.append(separator)
        node_to_be_merged.keys.extend(right_sibling.keys)

        if not node_to_be_merged.is_leaf_:
            node_to_be_merged.children.extend(right_sibling.children)
            for c in right_sibling.children:
                c.parent = node_to_be_merged


        parent.keys.pop(left_idx)
        parent.children.pop(right_idx)
        if parent is self.root and len(parent.keys) == 0:
            self.root = node_to_be_merged
            node_to_be_merged.parent = None

        elif parent != self.root and len(parent.keys) < self.t - 1:
            parent_idx = parent.parent.children.index(parent)
            self.borrow(parent.parent, parent_idx)


    @_track_operation
    def borrow(self,parent: Node,index: int):
        if index +1 <len(parent.children):
            right = parent.children[index +1]
            if len(right.keys) > self.t -1:
                self.borrow_from_right(parent,index)
                return
        if index - 1 >= 0:
            left = parent.children[index -1]
            if len(left.keys) > self.t -1:
                self.borrow_from_left(parent,index)
                return

        if index +1 < len(parent.children):
            self.merge(parent,index,index +1)
            return
        else:
            self.merge(parent,index,index -1)

    @_track_operation
    def borrow_from_right(self,parent_node,child_index):
        right_sibling = parent_node.children[child_index +1]
        child = parent_node.children[child_index]

        key_to_parent = right_sibling.keys.pop(0)
        key_to_node = parent_node.keys[child_index]

        parent_node.keys[child_index] = key_to_parent
        child.keys.append(key_to_node)

        if not right_sibling.is_leaf_:
            moved_child = right_sibling.children.pop(0)
            child.children.append(moved_child)
            moved_child.parent = child

    @_track_operation
    def borrow_from_left(self,parent_node,child_index):

        #messege = "Borrowing from right"

        left_sibling = parent_node.children[child_index -1]
        child = parent_node.children[child_index]

        key_to_parent = left_sibling.keys.pop(len(left_sibling.keys)-1)
        key_to_node = parent_node.keys[child_index - 1 ]

        parent_node.keys[child_index -1] = key_to_parent
        child.keys.insert(0,key_to_node)

        if not left_sibling.is_leaf_:
            moved_child = left_sibling.children.pop(len(left_sibling.children)-1)
            child.children.insert(0,moved_child)
            moved_child.parent = child

    @_track_operation
    def get_predcessor(self, parent, index):

        child = parent.children[index]

        while not child.is_leaf_:
            child = child.children[-1]


        predecessor = child.keys[-1]


        parent.keys[index] = predecessor



       # temp_key = DataHandler(predecessor.ID, predecessor.data)

        child.keys.pop()


        if len(child.keys) < self.t - 1 and child.parent is not None:
            parent_idx = child.parent.children.index(child)
            self.borrow(child.parent, parent_idx)

        return predecessor

    @_track_operation
    def get_scccesor(self, parent, index):

        if index + 1 >= len(parent.children):
            return None

        child = parent.children[index + 1]


        while not child.is_leaf_:
            child = child.children[0]

        if len(child.keys) == 0:
            return None


        successor = child.keys[0]


        parent.keys[index] = successor


        child.keys.pop(0)

        if len(child.keys) < self.t - 1 and child.parent is not None:
            parent_idx = child.parent.children.index(child)
            self.borrow(child.parent, parent_idx)

        return successor

    @_track_operation
    def delete_key(self, key: DataHandler):
        if self.root is None:
            print("Tree is empty")
            return

        node, index = self.search_key_in_node(self.root, key.ID, return_node=True)

        if node is None:
            print(f"Key {key.ID} not found")
            return


        if node.is_leaf_:
            node.keys.pop(index)

            if node != self.root and len(node.keys) < self.t - 1:
                parent_idx = node.parent.children.index(node)
                self.borrow(node.parent, parent_idx)
            return


        else:

            if len(node.children[index].keys) >= self.t:
                self.get_predcessor(node, index)

            elif index + 1 < len(node.children) and len(node.children[index + 1].keys) >= self.t:
                self.get_scccesor(node, index)

            else:

                self.merge(node, index, index + 1)
                self.delete_key(key)
                return


        if len(self.root.keys) == 0 and len(self.root.children) > 0:
            self.root = self.root.children[0]
            self.root.parent = None

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root

        indent = "   " * level
        print(f"{indent}Level {level} | Keys: {[k.ID for k in node.keys]} | "
              f"Children: {len(node.children)}")

        for child in node.children:
            self.print_tree(child, level + 1)




















