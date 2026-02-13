"""===========Btree algorithm==========="""

Files in Dictionary 'Btree'

- data_key_handler.py
  Optional helper file. It connects data with a key (ID) so that we can access the associated data by searching for its key.
  Data can be anything: files, strings, or any object. Not strictly required for the B-tree to function.

- node.py
  Contains the Node class, which represents a single node of the B-tree.
  Handles keys, children, parent references, and dynamic properties like checking if the node is a leaf or counting its keys.
- Btree.py
  Main implementation of the B-tree. Contains the Tree class with insertion, deletion, search, traversal, and balancing operations.
  Uses the Node and DataHandler classes.
- visualization.oy
  - Not finished  yet (work in progres

