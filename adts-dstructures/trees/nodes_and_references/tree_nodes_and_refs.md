# Binary Tree Nodes and References data structure
* This method to represent a binary tree uses nodes and references. In this case we will define a class that has attributes for
the root value, as well as the left and right subtrees. Since this representation more closely follows the object-oriented
programming paradigm, this representation is used more frequently with OOP languages.
* A Key thing to remember about the particular representation used in this module is that the nodes only have a key and
not a payload. An implication of this is that this representation is more limited and can not be used as is for data
structures like binary search tree. It needs to be modified to use a new class for the nodes of trees so that it can
handle the payload.
* We will start out with a simple class definition for the nodes and references approach. The important thing to remember
about this representation is that the attributes left and right will become references to other instances of the BinaryTree
class. For example, when we insert a new left child into the tree we create another instance of BinaryTree and modify
self.leftChild in the root to reference the new tree.
* The constructor function expects to get some kind of object to store in the root. Just like you can store any object
you like in a list, the root object of a tree can be a reference to any object. For our early examples, we will store
the name of the node as the root value.
* Next let’s look at the functions we need to build the tree beyond the root node. To add a left child to the tree, we
will create a new binary tree object and set the left attribute of the root to refer to this new object.
  * We must consider two cases for insertion. The first case is characterized by a node with no existing left child.
  When there is no left child, simply add a node to the tree. The second case is characterized by a node with an existing
  left child. In the second case, we insert a node and push the existing child down one level in the tree. The second
  case is handled by the else statement in the insertleft method.
* The code for insertRight must consider a symmetric set of cases. There will either be no right child, or we must insert
the node between the root and an existing right child.
* To round out the definition for a simple binary tree data structure, we will write accessor methods for the left and
right children, as well as the root values.

