from rcdsa.datastruct import LinkedQueue
from rcdsa.datastruct import HashSet
from rcdsa.datastruct import HashTable

class Graph:

  def __init__(self, directed=True):
    self._vetable = HashTable()
    self.vertexs = HashSet()
    self.edges = HashSet()
    self.directed = directed

  def insert_vertex(self, vertex, overwrite=True):
    self.vertexs.put(vertex, overwrite)

  def insert_edge(self, vertex_from,  vertex_to, edge, overwrite=True):
    if not self.vertexs.contains(vertex_from) or not self.vertexs.contains(vertex_to):
      raise RuntimeError("Vertex is not exists")
    self._vetable.put(vertex_from, vertex_to, edge, overwrite)
    if self.directed is False and vertex_from is not vertex_to:
      self._vetable.put(vertex_to, vertex_from, edge, overwrite)
    self.edges.put(edge, overwrite)

  def delete_vertex(self, vertex):
    if not self.vertexs.contains(vertex):
      return
    self.vertexs.remove(vertex)
    self._vetable.remove_row(vertex)
    self._vetable.remove_col(vertex)

  def delete_edge(self, vertex_from,  vertex_to):
    if not self.vertexs.contains(vertex_from) or not self.vertexs.contains(vertex_to):
      return
    self._vetable.remove(vertex_from, vertex_to)

  def traversal_bfs(self, callback, vertex_from=None):
    visited = HashSet()
    def _traversal(vertex):
      nonlocal self
      nonlocal visited
      nonlocal callback
      if visited.contains(vertex) is True:
        return
      
      queue = LinkedQueue()
      queue.enqueue(vertex)
      visited.put(vertex, True)
      while not queue.is_empty():
        curr = queue.front()
        queue.dequeue()
        callback(curr)
        adjs = self._vetable.get_keys_by_row(curr)
        for adj in adjs:
          if not visited.contains(adj):
            visited.put(adj)
            queue.enqueue(adj)
    if vertex_from is not None:
      _traversal(vertex_from)
    self.vertexs.traversal(_traversal)
  
  def traversal_dfs(self, vertex_from=None):
    pass