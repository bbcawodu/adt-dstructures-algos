# Breadth First Search
* Bredth First Search is an algorithm using the Graph ADT and data structure that has many applications.
* First we will outline and implement the breadth first search algorithm on an instance of the Graph data structre.
  * Breadth first search (BFS) is one of the easiest algorithms for searching a graph. It also serves as a prototype for several other important graph algorithms.
  * Given a graph G and a starting vertex s, a breadth first search proceeds by exploring edges in the graph to find all the vertices in G for which there is a path from s. The remarkable thing about a breadth first search is that it finds all the vertices that are a distance k from s before it finds any vertices that are a distance k+1. One good way to visualize what the breadth first search algorithm does is to imagine that it is building a tree, one level of the tree at a time. A breadth first search adds all children of the starting vertex before it begins to discover any of the grandchildren.
  * To keep track of its progress, BFS colors each of the vertices white, gray, or black. All the vertices are initialized to white when they are constructed. A white vertex is an undiscovered vertex. When a vertex is initially discovered it is colored gray, and when BFS has completely explored a vertex it is colored black. This means that once a vertex is colored black, it has no white vertices adjacent to it. A gray node, on the other hand, may have some white vertices adjacent to it, indicating that there are still additional vertices to explore.
  * The breadth first search algorithm shown in [bfs()](main.py) uses the adjacency list graph representation gone through in the parent directory: [Adjacency List](../../adjacency-list/README.md). In addition it uses a Queue, a crucial point as we will see, to decide which vertex to explore next.
  * In addition the BFS algorithm uses an extended version of the Vertex class. This new vertex class adds three new instance variables: distance, predecessor, and color. Each of these instance variables also has the appropriate getter and setter methods.
  * BFS begins at the starting vertex s and colors start gray to show that it is currently being explored. Two other values, the distance and the predecessor, are initialized to 0 and None respectively for the starting vertex. Finally, start is placed on a Queue. The next step is to begin to systematically explore vertices at the front of the queue. We explore each new node at the front of the queue by iterating over its adjacency list. As each node on the adjacency list is examined its color is checked. If it is white, the vertex is unexplored, and four things happen:
    1. The new, unexplored vertex nbr, is colored gray.
    2. The predecessor of nbr is set to the current node currentVert
    3. The distance to nbr is set to the distance to currentVert + 1
    4. nbr is added to the end of a queue. Adding nbr to the end of the queue effectively schedules this node for further exploration, but not until all the other vertices on the adjacency list of currentVert have been explored.
  * Let’s look at how the bfs function would construct the breadth first tree corresponding to the [word_ladder_example_1](img/word_ladder_example_1.png) graph. Starting from fool we take all nodes that are adjacent to fool and add them to the tree. The adjacent nodes include pool, foil, foul, and cool. Each of these nodes are added to the queue of new nodes to expand. The figure below shows the state of the in-progress tree along with the queue after this step.
    ![In Progress BFS](img/bfs_example_1.png)
  * In the next step bfs removes the next node (pool) from the front of the queue and repeats the process for all of its adjacent nodes. However, when bfs examines the node cool(while explring the neighbors of pool), it finds that the color of cool has already been changed to gray. This indicates that there is a shorter path to cool and that cool is already on the queue for further expansion. The only new node added to the queue while examining neighbors of pool is poll. The new state of the tree and queue is shown below.
    * ![In Progress BFS Step 2](img/bfs_example_2.png)
  * The next vertex on the queue is foil. The only new node that foil can add to the tree is fail. As bfs continues to process the queue, neither of the next two nodes add anything new to the queue or the tree. The figure below shows the tree and the queue after expanding all the vertices on the second level of the tree.
    ![In Progress BFS Step 3](img/bfs_example_3.png)
  * Work through the algorithm on your own so that you are comfortable with how it works. The figure below shows the final breadth first search tree after all the vertices in the [word_ladder_example_1](img/word_ladder_example_1.png) graph have been expanded. The amazing thing about the breadth first search solution is that we have not only solved the FOOL–SAGE problem we started out with, but we have solved many other problems along the way. We can start at any vertex in the breadth first search tree and follow the predecessor arrows back to the root to find the shortest word ladder from any word back to fool. The function [traverse()](main.py) shows how to follow the predecessor links to print out the word ladder.
    ![In Progress BFS Step 4](img/bfs_example_4.png)



* Now we will present different problems that can be solved using breadth first search.
  * Word Ladder Problem.
    * Let’s consider the following puzzle called a word ladder. Transform the word “FOOL” into the word “SAGE”. In a word ladder puzzle you must make the change occur gradually by changing one letter at a time. At each step you must transform one word into another word, you are not allowed to transform a word into a non-word. The word ladder puzzle was invented in 1878 by Lewis Carroll, the author of Alice in Wonderland. The following sequence of words shows one possible solution to the problem posed above.
      ```
      FOOL
      POOL
      POLL
      POLE
      PALE
      SALE
      SAGE
      ```
    * There are many variations of the word ladder puzzle. For example you might be given a particular number of steps in which to accomplish the transformation, or you might need to use a particular word. We are interested in figuring out the smallest number of transformations needed to turn the starting word into the ending word.
    * Not surprisingly, since this module is about graphs, we can solve this problem using a graph algorithm. Here is an outline of where we are going:
      * Represent the relationships between the words as a graph.
      * Use the graph algorithm known as breadth first search to find an efficient path from the starting word to the ending word.
    * Our first problem is to figure out how to turn a large collection of words into a graph. What we would like is to have an edge from one word to another if the two words are only different by a single letter. If we can create such a graph, then any path from one word to another is a solution to the word ladder puzzle. The figure below shows a small graph of some words that solve the FOOL to SAGE word ladder problem. Notice that the graph is an undirected graph and that the edges are unweighted.
      ![word_ladder_example_1](img/word_ladder_example_1.png)
    * We could use several different approaches to create the graph we need to solve this problem. Let’s start with the assumption that we have a list of words that are all the same length. As a starting point, we can create a vertex in the graph for every word in the list. To figure out how to connect the words, we could compare each word in the list with every other. When we compare we are looking to see how many letters are different. If the two words in question are different by only one letter, we can create an edge between them in the graph. For a small set of words that approach would work fine; however let’s suppose we have a list of 5,110 words. Roughly speaking, comparing one word to every other word on the list is an O(n^2) algorithm. For 5,110 words, n^2 is more than 26 million comparisons.
    * We can do much better by using the following approach. Suppose that we have a huge number of buckets, each of them with a four-letter word on the outside, except that one of the letters in the label has been replaced by an underscore. For example, consider the figure below, we might have a bucket labeled “pop\_.” As we process each word in our list we compare the word with each bucket, using the ‘\_’ as a wildcard, so both “pope” and “pops” would match “pop\_.” Every time we find a matching bucket, we put our word in that bucket. Once we have all the words in the appropriate buckets we know that all the words in the bucket must be connected.
      ![word_ladder_example_2](img/word_ladder_example_2.png)
    * In Python, we can implement the scheme we have just described by using a dictionary. The labels on the buckets we have just described are the keys in our dictionary. The value stored for that key is a list of words. Once we have the dictionary built we can create the graph. We start our graph by creating a vertex for each word in the graph. Then we create edges between all the vertices we find for words found under the same key in the dictionary. The code below shows the Python code required to build the graph.
      ```
      from pythonds.graphs import Graph

      def buildGraph(wordFile):
          word_buckets = {}
          g = Graph()
          wfile = open(wordFile,'r')
          # create buckets of words that differ by one letter
          for line in wfile:
              word = line[:-1]
              for i in range(len(word)):
                  bucket = word[:i] + '_' + word[i+1:]
                  if bucket in word_buckets:
                      word_buckets[bucket].append(word)
                  else:
                      word_buckets[bucket] = [word]
          # add vertices and edges for words in the same bucket
          for bucket in word_buckets.keys():
              for word1 in word_buckets[bucket]:
                  for word2 in d[bucket]:
                      if word1 != word2:
                          g.addEdge(word1,word2)
          return g
      ```
    * You might be wondering how sparse is the graph? The list of four-letter words we have for this problem is 5,110 words long. If we were to use an adjacency matrix, the matrix would have 5,110 * 5,110 = 26,112,100 cells. The graph constructed by the buildGraph function has exactly 53,286 edges, so the matrix would have only 0.20% of the cells filled! That is a very sparse matrix indeed.
