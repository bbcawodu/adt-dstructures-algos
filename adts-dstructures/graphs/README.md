# Graph Abstract Data Type
  * Graphs are an abstract data type that can be used to represent many interesting things about our world, including systems of roads, airline flights from city to city, how the Internet is connected, or even the sequence of classes you must take to complete a major in computer science. Once there is a good representation for a problem, we can use some standard graph algorithms to solve what otherwise might seem to be a very difficult problem.
  * A Graph is an abstract data type that can be represented as a collection of verticies and edges that connect 2 given verticies. To more formally define a graph, it is helpful to start with a description of its components.
    * Vertex
      * A vertex (also called a “node”) is a fundamental part of a graph. It can have a name, which we will call the “key.” A vertex may also have additional information. We will call this additional information the “payload.”
    * Edge
      * An edge (also called an “arc”) is another fundamental part of a graph. An edge connects two vertices to show that there is a relationship between them. Edges may be one-way or two-way. If the edges in a graph are all one-way, we say that the graph is a directed graph, or a digraph. The class prerequisites graph shown above is clearly a digraph since you must take some classes before others.
    * Weight
      * Edges may be weighted to show that there is a cost to go from one vertex to another. For example in a graph of roads that connect one city to another, the weight on the edge might represent the distance between the two cities.


  * The figure below shows an example of a simple weighted digraph. Formally we can represent this graph as the set of six vertices:
    ```V={V0,V1,V2,V3,V4,V5}```
    and the set of nine edges:
    ```E={(v0,v1,5),(v1,v2,4),(v2,v3,9),(v3,v4,7),(v4,v0,1),(v0,v5,2),(v5,v4,8),(v3,v5,3),(v5,v2,1)}```

    [!example digraph](/img/digraph.png)