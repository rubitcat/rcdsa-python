from rcdsa.datastruct import HashMap
from rcdsa.datastruct import Graph
from rcdsa.datastruct import Heap


def dijkstra(graph: Graph, from_vertex, get_weight) -> HashMap:
  vetable = graph.vetable
  vsize = graph.vertexs.size()
  dist = HashMap(vsize)
  dist.put(from_vertex, 0)
  min_heap = Heap(vsize, lambda x,y: Heap.default_cmp(x[0], y[0]))
  min_heap.push((0, from_vertex))
  while not min_heap.is_empty():
    vertex = min_heap.top()[1]
    min_heap.pop()
    adjs = vetable.get_keys_by_row(vertex)
    for adj in adjs:
      old_dist = dist.get(adj)
      new_dist = dist.get(vertex) + get_weight(vetable.get(vertex, adj)) 
      if old_dist is None or (new_dist is not None and new_dist < old_dist):
        dist.put(adj, new_dist)
        min_heap.push((new_dist, adj))
  return dist

    
    
  
  

