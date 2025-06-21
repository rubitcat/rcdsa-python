from rcdsa.datastruct import LinkedQueue
from rcdsa.datastruct import LinkedStack
from rcdsa.datastruct import HashSet
from rcdsa.datastruct import HashTable

class Graph:
  class Edge:
    def __init__(self, from_vertex=None, to_vertex=None, value=None):
      self.from_vertex = from_vertex
      self.to_vertex = to_vertex
      self.value = value
    def __eq__(self, e):
      return self.from_vertex == e.from_vertex and  self.to_vertex and e.to_vertex 
    def __hash__(self):
      return self.from_vertex.__hash__() + self.to_vertex.__hash__()

  def __init__(self, directed=True):
    self.vetable = HashTable()
    self.vertexs = HashSet()
    self.edges = HashSet()
    self.directed = directed

  def insert_vertex(self, vertex, overwrite=True):
    self.vertexs.put(vertex, overwrite)

  def insert_edge(self, vertex_from,  vertex_to, edge, overwrite=True):
    if not self.vertexs.contains(vertex_from) or not self.vertexs.contains(vertex_to):
      raise RuntimeError("Vertex is not exists")
    self.vetable.put(vertex_from, vertex_to, edge, overwrite)
    self.edges.put(self.Edge(vertex_from, vertex_to, edge), True)
    if self.directed is False and vertex_from is not vertex_to:
      self.vetable.put(vertex_to, vertex_from, edge, overwrite)
      self.edges.put(self.Edge(vertex_to, vertex_from, edge), True)

  def delete_vertex(self, vertex):
    if not self.vertexs.contains(vertex):
      return
    self.vertexs.remove(vertex)
    self.vetable.remove_row(vertex)
    self.vetable.remove_col(vertex)
    self.edges.traversal(lambda e: (vertex is e.from_vertex or vertex is e.to_vertex) and self.edges.remove(e))

  def delete_edge(self, vertex_from,  vertex_to):
    if not self.vertexs.contains(vertex_from) or not self.vertexs.contains(vertex_to):
      return
    self.vetable.remove(vertex_from, vertex_to)

  def traversal_bfs(self, callback, vertex_from=None):
    discovered = HashSet()
    def _traversal(vertex):
      nonlocal self
      nonlocal discovered
      nonlocal callback
      if discovered.contains(vertex) is True:
        return
      
      queue = LinkedQueue()
      queue.enqueue(vertex)
      discovered.put(vertex)
      while not queue.is_empty():
        curr = queue.front()
        queue.dequeue()
        callback(curr)
        adjs = self.vetable.get_keys_by_row(curr)
        for adj in adjs:
          if not discovered.contains(adj):
            queue.enqueue(adj)
            discovered.put(adj)
    if vertex_from is not None and self.vertexs.contains(vertex_from):
      _traversal(vertex_from)
    self.vertexs.traversal(_traversal)
  
  def traversal_dfs(self, callback, vertex_from=None):
    visited = HashSet()
    def _traversal(vertex):
      nonlocal self
      nonlocal visited
      nonlocal callback
      if visited.contains(vertex) is True:
        return
      
      stack = LinkedStack()
      stack.push(vertex)
      while not stack.is_empty():
        curr = stack.top()
        stack.pop()
        if visited.contains(curr):
          continue
        callback(curr)
        visited.put(curr)
        adjs = self.vetable.get_keys_by_row(curr)
        for i in range(len(adjs)-1, -1, -1):
          adj = adjs[i]
          if not visited.contains(adj):
            stack.push(adj)
    if vertex_from is not None and self.vertexs.contains(vertex_from):
      _traversal(vertex_from)
    self.vertexs.traversal(_traversal)