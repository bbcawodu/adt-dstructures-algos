class Vertex(object):
  """
  Vertex data structure for the adjacency list implementation of the Graph ADT. Adjacency list implementation of the graph adt requires vertec data structure/class because the
  edges/neighbors of each vertex are maintained on the vertex object while the master list of verticies are maintained on the Graph data structure/class.
  """

  def __init__(self, key):
    self.id = key
    self.connectedTo = {}
    self.color = 'white'

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


def knightGraph(bdSize):
  ktGraph = Graph()
  for row in range(bdSize):
   for col in range(bdSize):
     nodeId = posToNodeId(row,col,bdSize)
     newPositions = genLegalMoves(row,col,bdSize)
     for e in newPositions:
       nid = posToNodeId(e[0],e[1],bdSize)
       ktGraph.addEdge(nodeId,nid)
  return ktGraph


def posToNodeId(row, column, board_size):
  return (row * board_size) + column


def genLegalMoves(x,y,bdSize):
  newMoves = []
  moveOffsets = [
    (-1,-2),
    (-1,2),
    (-2,-1),
    (-2,1),
    ( 1,-2),
    ( 1,2),
    ( 2,-1),
    ( 2,1)
  ]
  for i in moveOffsets:
    newX = x + i[0]
    newY = y + i[1]
    if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
      newMoves.append((newX,newY))
  return newMoves


def legalCoord(x,bdSize):
  if x >= 0 and x < bdSize:
    return True
  else:
    return False


def knightTour(n,path,u,limit):
  u.setColor('gray')
  path.append(u)
  if n < limit:
    nbrList = orderByMovesAvail(u)
    i = 0
    done = False
    while i < len(nbrList) and not done:
      if nbrList[i].getColor() == 'white':
        done = knightTour(n+1, path, nbrList[i], limit)
      i = i + 1
    if not done:  # prepare to backtrack
      path.pop()
      u.setColor('white')
  else:
    done = True
  return done


def orderByMovesAvail(n):
  resList = []
  for v in n.getConnections():
    if v.getColor() == 'white':
      c = 0
      for w in v.getConnections():
        if w.getColor() == 'white':
          c = c + 1
      resList.append((c,v))
  resList.sort(key=lambda x: x[0])

  return [y[1] for y in resList]


def main():
  g = knightGraph(8)
  path = []
  start = g.getVertex(0)
  found = knightTour(1,path,start,64)
  print(found)
  print(len(path))


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
