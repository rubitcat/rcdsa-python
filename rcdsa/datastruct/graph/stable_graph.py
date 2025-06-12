from rcdsa.datastruct import Graph
from rcdsa.datastruct import LinkedQueue
from rcdsa.datastruct import LinkedHashSet
from rcdsa.datastruct import LinkedHashTable

class StableGraph(Graph):

  def __init__(self, directed=True):
    self.vetable = LinkedHashTable()
    self.vertexs = LinkedHashSet()
    self.edges = LinkedHashSet()
    self.directed = directed
