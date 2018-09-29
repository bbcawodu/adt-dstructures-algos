class Vertex(object):
  """
  Vertex data structure for the adjacency list implementation of the Graph ADT. Adjacency list implementation of the graph adt requires vertec data structure/class because the
  edges/neighbors of each vertex are maintained on the vertex object while the master list of verticies are maintained on the Graph data structure/class.
  """

  def __init__(self, key):
    self.id = key
    self.connectedTo = {}
    self.color = 'white'
    self.distance = 0
    self.predecessor = None

  def addNeighbor(self, neighbor, weight=0):
    self.connectedTo[neighbor] = weight

  def __str__(self):
    return str(self.id) + ' connectedTo: ' + str([neighbor.id for neighbor in self.connectedTo])

  def getConnections(self):
    return self.connectedTo.keys()

  def getId(self):
    return self.id

  def getWeight(self, neighbor):
    return self.connectedTo[neighbor]

  def setColor(self, col):
    self.color = col

  def getColor(self):
    return self.color

  def setDistance(self, dist):
    self.distance = dist

  def getDistance(self):
    return self.distance

  def setPred(self, pred):
    self.predecessor = pred

  def getPred(self):
    return self.predecessor


class Graph(object):
  """
  Graph Data Structure with an adjacency list implementation - Recall that when we give an abstract data type a physical implementation we refer to the implementation as a data structure.
  """
  
  def __init__(self):
    self.vertList = {}
    self.numVertices = 0

  def addVertex(self, key):
    self.numVertices = self.numVertices + 1
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    return newVertex

  def getVertex(self, key):
    if key in self.vertList:
      return self.vertList[key]
    else:
      return None

  def __contains__(self, key):
    return key in self.vertList

  def addEdge(self, from_vertex_key, to_vertex_key, cost=0):
    if from_vertex_key not in self.vertList:
      nv = self.addVertex(from_vertex_key)
    if to_vertex_key not in self.vertList:
      nv = self.addVertex(to_vertex_key)
    self.vertList[from_vertex_key].addNeighbor(self.vertList[to_vertex_key], cost)

  def getVertices(self):
    return self.vertList.keys()

  def __iter__(self):
    return iter(self.vertList.values())


class Queue(object):
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0,item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)


def bfs(g, start):
  start.setDistance(0)
  start.setPred(None)
  # need to chanage dfs to use priority queue by the distance value so that the dfs can take edge weight into account, also need to change the neighbor.setdistance to be currentVert.getDistance() + weight
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for neighbor in currentVert.getConnections():
      if (neighbor.getColor() == 'white'):
        neighbor.setColor('gray')
        neighbor.setDistance(currentVert.getDistance() + 1)
        neighbor.setPred(currentVert)
        vertQueue.enqueue(neighbor)
    currentVert.setColor('black')


def traverse_using_predecessor_refs(start):
  current = start
  while (current.getPred()):
    print(current.getId())
    current = current.getPred()
  print(current.getId())


def main():
  g = Graph()
  for i in range(6):
    g.addVertex(i)

  g.addEdge(0,1,5)
  g.addEdge(0,5,2)
  g.addEdge(1,2,4)
  g.addEdge(2,3,9)
  g.addEdge(3,4,7)
  g.addEdge(3,5,3)
  g.addEdge(4,0,1)
  g.addEdge(5,4,8)
  g.addEdge(5,2,1)

  bfs(g, g.getVertex(0))
  traverse_using_predecessor_refs(g.getVertex(4))


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
