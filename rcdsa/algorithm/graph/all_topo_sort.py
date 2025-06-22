from rcdsa.datastruct import Graph
from rcdsa.datastruct import HashMap
from rcdsa.datastruct import LinkedStack

class StackFrame:
  def __init__(self, status=0, index=0):
    self.index = index
    self.adjs = None
    self.indeg = None
    self.discovered = None
    self.recu = None
    self.status = status

def all_topo_sort(graph: Graph):
  res = []
  path = []
  vertexs = graph.vertexs.values()
  vsize = graph.vertexs.size()
  discovered_map = HashMap()
  indeg_map = HashMap()
  graph.vertexs.traversal(lambda v: indeg_map.put(v, 0))
  graph.edges.traversal(lambda e: indeg_map.put(e.to_vertex, indeg_map.get(e.to_vertex)+1))
  #  _topo_sort_util(graph.vertexs.values(), graph.vetable, discovered_map, indeg_map, [], res)

  stack = LinkedStack()
  stack.push(StackFrame())
  while not stack.is_empty():
    curr :StackFrame = stack.top()
    if curr.index == vsize:
      stack.pop()
      if len(path) == vsize:
        res.append(list(path))
    elif curr.status == 0:
      v = vertexs[curr.index]
      curr.discovered = discovered_map.get(v)
      curr.indeg = indeg_map.get(v)
      if curr.indeg == 0 and not curr.discovered:
        curr.adjs = graph.vetable.get_keys_by_row(v)
        if curr.adjs is not None:
          for adj in curr.adjs:
            indeg_map.put(adj, indeg_map.get(adj)-1)
        discovered_map.put(v, True)
        path.append(v)
        stack.push(StackFrame())
      curr.status = 1
    elif curr.status == 1:
      if curr.indeg == 0 and not curr.discovered:
        v = vertexs[curr.index]
        discovered_map.put(v, False)
        path.pop()
        if curr.adjs is not None:
          for adj in curr.adjs:
            indeg_map.put(adj, indeg_map.get(adj)+1)
      curr.index += 1
      curr.status = 0 
  return res

def _topo_sort_util(vertexs, vetable, discovered_map, indeg_map, path, result):
  for v in vertexs:
    discovered = discovered_map.get(v)
    indeg = indeg_map.get(v)
    if indeg == 0 and not discovered:
      adjs = vetable.get_keys_by_row(v)

      if adjs is not None:
        for adj in adjs:
          indeg_map.put(adj, indeg_map.get(adj)-1)
      discovered_map.put(v, True)
      path.append(v)

      _topo_sort_util(vertexs, vetable, discovered_map, indeg_map, path, result)

      discovered_map.put(v, False)
      path.pop()
      if adjs is not None:
        for adj in adjs:
          indeg_map.put(adj, indeg_map.get(adj)+1)
  
  if len(path) == len(vertexs):
    result.append(list(path))
