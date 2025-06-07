from rcdsa.datastruct import LinkedQueue

class AdjList:
  class Node:
    def __init__(self, data=None, next=None):
      self.data = data
      self.next = next

  def __init__(self, vertices):
    self.vertices = vertices
    self.data = [None] * vertices
  
  def add_vertex(self):
    pass

  def add_edge(self):
    pass


  def traversal_bfs(self, func):
    pass