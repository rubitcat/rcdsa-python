from rcdsa.datastruct import Graph
from rcdsa.datastruct import LinkedStack
from rcdsa.datastruct import HashSet

class StackFrame:
  def __init__(self, status=0, vertex=None):
    self.vertex = vertex
    self.status = status

def _cycle_detect_undirected(graph: Graph):
  visited = HashSet()
  for vertex in graph.vertexs.values():
    if visited.contains(vertex):
      continue
    stack = LinkedStack()
    stack.push((None, vertex))
    while not stack.is_empty():
      parent, curr_vertex = stack.top()
      stack.pop()
      if visited.contains(curr_vertex):
        continue
      visited.put(curr_vertex)
      adjs = graph.vetable.get_keys_by_row(curr_vertex)
      if adjs is not None:
        for i in range(len(adjs)-1, -1, -1):
          if not visited.contains(adj := adjs[i]):
            stack.push((curr_vertex, adj))
          elif adj is not parent:
            return True
  return False

def _cycle_detect_directed(graph: Graph):
  curr_visited = HashSet()
  visited = HashSet()
  for vertex in graph.vertexs.values():
    if visited.contains(vertex):
      continue
    stack = LinkedStack()
    stack.push(StackFrame(0, vertex))
    while not stack.is_empty():
      curr = stack.top()
      if curr.status == 0 and visited.contains(curr.vertex):
        stack.pop()
        continue
      if curr.status == 0:
        curr_visited.put(curr.vertex)
        visited.put(curr.vertex)
        adjs = graph.vetable.get_keys_by_row(curr.vertex)
        if adjs is not None:
          for i in range(len(adjs)-1, -1, -1):
            if not visited.contains(adj := adjs[i]):
              stack.push(StackFrame(0, adj))
            elif curr_visited.contains(adj):
              return True
        curr.status = 1
      elif curr.status == 1:
        curr_visited.remove(curr.vertex)
        stack.pop()
  return False      

def cycle_detect(graph: Graph):
  if graph.directed:
    return _cycle_detect_directed(graph)
  else:
    return _cycle_detect_undirected(graph)