# Tree List of Lists Data Structure
  * In a tree represented by a list of lists, we will begin with Python’s list data structure and write the functions
  defined for the tree ADT. Although writing the interface as a set of operations on a list is a bit different from the
  other abstract data types we have implemented, it is interesting to do so because it provides us with a simple
  recursive data structure that we can look at and examine directly.
  * In a list of lists tree, we will store the value of the root node as the first element of the list. The second
  element of the list will itself be a list that represents the left subtree. The third element of the list will be
  another list that represents the right subtree.
  * One very nice property of this list of lists approach is that the structure of a list representing a subtree
  adheres to the structure defined for a tree; the structure itself is recursive! A subtree that has a root value and
  two empty lists is a leaf node.
  * Another nice feature of the list of lists approach is that it generalizes to a tree that has many subtrees.
  In the case where the tree is more than a binary tree, another subtree is just another list.
  * A formal definition of a binary tree data structure is given by providing some functions that make it easy for us to
  use lists as trees. Note that we do not define a binary tree class. The functions we write just help us manipulate a
  standard list as though we are working with a tree.