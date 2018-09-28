class Vertex(object):
  """
  Vertex data structure for the adjacency list implementation of the Graph ADT. Adjacency list implementation of the graph adt requires vertec data structure/class because the
  edges/neighbors of each vertex are maintained on the vertex object while the master list of verticies are maintained on the Graph data structure/class.
  """

  def __init__(self,key):
    self.id = key
    self.connectedTo = {}

  def addNeighbor(self,nbr,weight=0):
    self.connectedTo[nbr] = weight

  def __str__(self):
    return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

  def getConnections(self):
    return self.connectedTo.keys()

  def getId(self):
    return self.id

  def getWeight(self,nbr):
    return self.connectedTo[nbr]


class Graph(object):
  """
  Graph Data Structure with an adjacency list implementation - Recall that when we give an abstract data type a physical implementation we refer to the implementation as a data structure.
  """
  
  def __init__(self):
    self.vertList = {}
    self.numVertices = 0

  def addVertex(self,key):
    self.numVertices = self.numVertices + 1
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    return newVertex

  def getVertex(self,n):
    if n in self.vertList:
      return self.vertList[n]
    else:
      return None

  def __contains__(self,n):
    return n in self.vertList

  def addEdge(self,f,t,cost=0):
    if f not in self.vertList:
      nv = self.addVertex(f)
    if t not in self.vertList:
      nv = self.addVertex(t)
    self.vertList[f].addNeighbor(self.vertList[t], cost)

  def getVertices(self):
    return self.vertList.keys()

  def __iter__(self):
    return iter(self.vertList.values())


def main():
  g = Graph()
  for i in range(6):
    g.addVertex(i)

  print(g.vertList)

  g.addEdge(0,1,5)
  g.addEdge(0,5,2)
  g.addEdge(1,2,4)
  g.addEdge(2,3,9)
  g.addEdge(3,4,7)
  g.addEdge(3,5,3)
  g.addEdge(4,0,1)
  g.addEdge(5,4,8)
  g.addEdge(5,2,1)
  for v in g:
    for w in v.getConnections():
      print("( %s , %s , %s )" % (v.getId(), w.getId(), v.getWeight(w)))


"""
When the interpreter reads a python file, it executes all the code found in it.
Before executing the code, the interpreter defines some special variables(environment, etc.)
If the python interpreter is running the python file as the main program(eg. when being called from the command line),
It sets the __name__ variable to "__main__". If the python file is being imported from another module, __name__ will
be set to the module's name.
By doing the __main__ check, you can control when parts of code execute.
"""
if __name__ == "__main__":
  main()
