from rcdsa.datastruct import Graph
from rcdsa.datastruct import HashMap

def bellman_ford(graph: Graph, from_vertex, get_weight=lambda e: e.value, path: HashMap = None) -> HashMap:
  vsize = graph.vertexs.size()
  vertexs = graph.vertexs.values()
  edges = graph.edges.values()
  dist = HashMap(vsize)
  dist.put(from_vertex, 0)
  iteration = 0
  for vertex in vertexs:
    for edge in edges:
      if (mid := dist.get(edge.from_vertex)) is not None:
        if (adj_dist := dist.get(edge.to_vertex)) is None:
          new_dist = mid + get_weight(edge)
          dist.put(edge.to_vertex, new_dist)
        elif (new_dist := mid + get_weight(edge)) < adj_dist:
          if iteration == vsize - 1:
            raise RuntimeError("cycle detected!")
          dist.put(edge.to_vertex, new_dist)
    iteration += 1
  return dist