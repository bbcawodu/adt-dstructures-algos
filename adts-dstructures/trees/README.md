# Tree Abstract Data Type
  * Below is a formal definition of a tree and its components:
    * Node
      * A node is a fundamental part of a tree. It can have a name, which we call the “key.” A node may also have additional
      information. We call this additional information the “payload.” While the payload information is not central to many tree
      algorithms, it is often critical in applications that make use of trees.
    * Edge
      * An edge is another fundamental part of a tree. An edge connects two nodes to show that there is a relationship between
      them. Every node (except the root) is connected by exactly one incoming edge from another node. Each node may have several
      outgoing edges.
    * Root
      * The root of the tree is the only node in the tree that has no incoming edges.
    * Path
      * A path is an ordered list of nodes that are connected by edges. 
    * Children
      * The set of nodes 𝑐 that have incoming edges from the same node to are said to be the children of that node.
    * Parent
      * A node is the parent of all the nodes it connects to with outgoing edges.
    * Sibling
      * Nodes in the tree that are children of the same parent are said to be siblings.
    * Subtree
      * A subtree is a set of nodes and edges comprised of a parent and all the descendants of that parent.
    * Leaf Node
      * A leaf node is a node that has no children.
    * Level
      *The level of a node 𝑛 is the number of edges on the path from the root node to 𝑛.
    * Height
      * The height of a tree is equal to the maximum level of any node in the tree.
    * With the basic vocabulary now defined, we can move on to a formal definition of a tree. In fact, we will provide
    two definitions of a tree. One definition involves nodes and edges. The second definition, which will prove to be
    very useful, is a recursive definition.
      * Definition One: A tree consists of a set of nodes and a set of edges that connect pairs of nodes. A tree has the
      following properties:
        * One node of the tree is designated as the root node.
        * Every node 𝑛, except the root node, is connected by an edge from exactly one other node 𝑝, where 𝑝 is the parent of 𝑛.
        * A unique path traverses from the root to each node.
        * If each node in the tree has a maximum of two children, we say that the tree is a binary tree.
      * Definition Two: A tree is either empty or consists of a root and zero or more subtrees, each of which is also a
      tree. The root of each subtree is connected to the root of the parent tree by an edge.
    * The following are 2 data structure representations of the tree adt
      * [Tree List of Lists Data Structure](list_of_lists/tree_list_of_lists.md)
      * [Tree Nodes and References Data Structure](nodes_and_references/tree_nodes_and_refs.md)