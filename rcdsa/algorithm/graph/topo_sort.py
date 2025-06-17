from rcdsa.datastruct import Graph
from rcdsa.datastruct import HashMap
from rcdsa.datastruct import LinkedQueue

def topo_sort(graph: Graph) -> list:
  if not graph.directed:
    raise RuntimeError("graph must be a directed graph") 

  res = []
  vetable = graph.vetable
  indeg_map = HashMap()
  queue = LinkedQueue()
  graph.vertexs.traversal(lambda v: indeg_map.put(v, 0))
  graph.edges.traversal(lambda e: indeg_map.put(e.to_vertex, indeg_map.get(e.to_vertex)+1))
  indeg_map.traversal(lambda e: e.value == 0 and queue.enqueue(e.key))
  while not queue.is_empty():
    vertex = queue.front()
    queue.dequeue()
    res.append(vertex)
    adjs = vetable.get_keys_by_row(vertex)
    if adjs is not None:
      for adj in adjs:
        indeg = indeg_map.get(adj) - 1
        indeg_map.put(adj, indeg)
        if indeg == 0:
          queue.enqueue(adj)
  return res