# Graph Abstract Data Type - Adjacency Matrix Implementation
  * One of the easiest ways to implement a graph is to use a two-dimensional matrix. In this matrix implementation, each of the rows and columns represent a vertex in the graph. The value that is stored in the cell at the intersection of row v and column w indicates if there is an edge from vertex v to vertex w. When two vertices are connected by an edge, we say that they are adjacent. The figure below illustrates the adjacency matrix for the graph in the [parent README](../README.md). A value in a cell represents the weight of the edge from vertex v to vertex w.
    ![sample adjacency matrix](img/sample_adjacency_matrix.png)
  * The advantage of the adjacency matrix is that it is simple, and for small graphs it is easy to see which nodes are connected to other nodes. However, notice that most of the cells in the matrix are empty. Because most of the cells are empty we say that this matrix is “sparse.” A matrix is not a very efficient way to store sparse data. In fact, in Python you must go out of your way to even create a matrix structure like the one in the figure above.
  * The adjacency matrix is a good implementation for a graph when the number of edges is large. But what do we mean by large? How many edges would be needed to fill the matrix? Since there is one row and one column for every vertex in the graph, the number of edges required to fill the matrix is |V|^2. A matrix is full when every vertex is connected to every other vertex. There are few real problems that approach this sort of connectivity, though this structre has its advantages in situations like this.
  * In case of undirected graph, the matrix is symmetric about the diagonal because of every edge (i,j), there is also an edge (j,i).

  * If you know how to create two dimensional arrays, you also know how to create adjacency matrix. The implementation is here: [Graph](main.py)
    * Pros of adjacency matrix
      * The basic operations like adding an edge, removing an edge and checking whether there is an edge from vertex i to vertex j are extremely time efficient, constant time operations.
      * If the graph is dense and the number of edges is large, adjacency matrix should be the first choice. Even if the graph and the adjacency matrix is sparse, we can represent it using data structures for sparse matrix.
      * The biggest advantage however, comes from the use of matrices. The recent advances in hardware enable us to perform even expensive matrix operations on the GPU.
      * By performing operations on the adjacent matrix, we can get important insights into the nature of the graph and the relationship between its vertices.
    * Cons of adjacency matrix
      * The VxV space requirement of adjacency matrix makes it a memory hog. Graphs out in the wild usually don't have too many connections and this is the major reason why adjacency lists are the better choice for most tasks.
      * While basic operations are easy, operations like inEdges and outEdges(for given vertex) are expensive when using the adjacency matrix representation.
