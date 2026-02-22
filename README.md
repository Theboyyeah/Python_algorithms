"""===========Btree algorithm==========="""


B-tree is a self-balancing tree structure used in database systems 
(nowadays B+trees are more common). It is characterized by:
- Each node can hold a maximum of 2*t - 1(or 2*t +1 depends of how we define degree of a betree) keys and a minimum of t-1(or t) keys.
- Each internal node can have a maximum of 2*t (or 2*t +1) children and a minimum of t children.
- Exception: the root can have as few as 1 key and 2 children (or 0 keys if the tree is empty).
- All leaves are at the same level (this is what keeps it balanced).


Inserting keys into Btree:
- Firstly we check if the root exists, if not we create a new root and insert the key directly.
- If the root is full (has max_num_of_keys) we create a new root, make the old root
  its child and split it before inserting
- Then we call insert_non_full starting from the root

insert_non_full:
- If the current node is a leaf we find the correct position by shifting keys
  to the right until we find the right spot, then insert the key there.
- If the current node is an internal node we find the correct child by counting
  how many keys are smaller than the inserted key (index i), then we go to children[i].
- Before entering children[i] we check if it is full — if so we split it first,
  then choose the correct child after the split

-- Insert helper function:
-- split- splits the full child of parent at given index:
   -- The middle key (at index t-1) is moved up to the parent
   -- All keys smaller than the middle key stay in the left node (left node might be original node(node which is curently splited)
   but in my implementation i just created two new nodes (Idk if it's correct but it's working the same)
   -- All keys greater than the middle key go to the new right node
   -- If the node is not a leaf, children from index 0 to t go to the left node
      and the remaining children go to the right node
   -- Both left and right nodes have their parent set to the original parent


Searching key:
- Firstly we check if the root exists, if not we return None
- Then search_key calls search_key_in_node starting from the root
- In search_key_in_node we iterate through the keys of the current node
  counting how many keys are smaller than the searched key (this gives us
  index i)
- If we find the key at index i we return it (or the node itself if return_node=True (if return_node == True that means search was called by delete_key function))
- If we reach a leaf node without finding the key, the key does not exist in the tree
- If the current node is not a leaf, we recurse into children[i] — the correct
  child is always at the same index i, since i tells us how many keys were
  smaller than ours, meaning our key must be in the subtree after those keys
Deleting key:
- Firstly we check if the root exists and search for the key using search_key_in_node
- If the key is not found we return None

Case 1 - node is a leaf:
- Simply we remove key from the node
- If the node has too few keys (less than t-1) we call borrow to fix it

Case 2 - node is an internal node:
- If the left child (children[index]) has enough keys (>= t) we replace
  the key with its predecessor using get_predecessor() which finds the
  largest key in the left subtree
- If the right child (children[index+1]) has enough keys (>= t) we replace
  the key with its successor using get_successor which finds the smallest
  key in the right subtree
- If both children have too few keys we merge them using merge and call
  delete_key again recursively

-- delete helper functions:
-- borrow (!!!Function that encompasses other functions used in delete,
name might be misleading since it also deals with merge and successors!!!)- tries to borrow a key from right sibling first,
   then left sibling. If neither sibling has enough keys, it merges instead
-- borrow_from_right - takes the leftmost key from the right
   sibling, pushes the separator from parent down to the node
-- borrow_from_left - takes the rightmost key from the left
   sibling, pushes the separator from parent down to the node
-- get_predecessor - goes as far right as possible in the left
   subtree to find the largest key, replaces the deleted key with it
-- get_successor - goes as far left as possible in the right
   subtree to find the smallest key, replaces the deleted key with it
-- merge - merges two siblings and the
   separator(key in parent node between childe nodes (Node we are merging and node thet is going to be absorbed)) key from parent into one node. If parent becomes empty and is
   root, the merged node becomes the new root

Additional funtions used in btree.py:
 - Those function were used to simplify the depuging process:
--_track_operation - decorator used for debugging. If debug_mode is enabled,
   it prints the name of the called function and who called it (the caller function name).
   Wraps every major operation in the tree. Uses inspect
--print_tree(node, level) - prints the tree structure to the console level by level(in acceptable way.
   For each node it shows the current level, the keys stored in it and the number
   of children. Recursively prints all children below
--in_order_traversal(node) - traverses the tree in order.Result should be always sorted


Note:
 - Evry delete heleper function (method) like merge also needs to
   tends to balans the tree after deleting the key
 - this is only my implementation of Btree propably there are more
   itnresting ways to do Btrees or more correctly
 - It should be working in evry case (t > 1) but who knows :)
 



Files in Directory 'Btree'

- data_key_handler.py
  Optional helper file. It connects data with a key (ID) so that we can access the associated data by searching for its key.
  Data can be anything: files, strings, or any object. Not strictly required for the B-tree to function.

- node.py
  Contains the Node class, which represents a single node of the B-tree.
  Handles keys, children, parent references, and dynamic properties like checking if the node is a leaf or counting its keys.
  
- Btree.py
  Main implementation of the B-tree. Contains the Tree class with insertion, deletion, search, traversal, and balancing operations.
  Uses the Node and DataHandler classes.
- visualization.py
  - Not finished  yet (work in progres(might finish,might not(not required for B-tree to work)))



How to run program:


1 Clone repository using:
git clone https://github.com/theboyyeah/Python_algorithms.git


2 Enter correct directory:
   cd Python_algorithms/Btree

3 run:
python3 main.py


