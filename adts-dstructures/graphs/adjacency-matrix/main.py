class Graph(object):
  """
  Graph Data Structure with an adjacency matrix implementation - Recall that when we give an abstract data type a physical implementation we refer to the implementation as a data structure.
  """
  
  def __init__(self, size):
    self.adjMatrix = []
    for i in range(size):
      self.adjMatrix.append([-1 for i in range(size)])
    self.size = size

  def addEdge(self, v1, v2, weight=0):
    if v1 == v2:
      print("Same vertex %d and %d" % (v1, v2))
      return
    self.adjMatrix[v1][v2] = weight
    self.adjMatrix[v2][v1] = weight

  def removeEdge(self, v1, v2):
    if self.adjMatrix[v1][v2] == -1:
      print("No edge between %d and %d" % (v1, v2))
      return
    self.adjMatrix[v1][v2] = -1
    self.adjMatrix[v2][v1] = -1

  def containsEdge(self, v1, v2):
    return True if self.adjMatrix[v1][v2] >= 0 else False

  def __len__(self):
    return self.size
      
  def toString(self):
    return_string = "\n"
    for row in self.adjMatrix:
      for val in row:
        return_string += '{:4}'.format(val)
      return_string += "\n"

    return return_string


def main():
  g = Graph(5)
  g.addEdge(0, 1)
  g.addEdge(0, 2)
  g.addEdge(1, 2)
  g.addEdge(2, 0)
  g.addEdge(2, 3)

  print(g.toString())


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

    