from rcdsa.datastruct import HashMap
from rcdsa.datastruct import Graph
from rcdsa.datastruct import Heap

def pair_cmp(p1, p2):
  if p1.dist < p2.dist:
    return 1
  elif p2.dist > p1.dist:
    return -1
  else:
    return 0

class pair:
  def __init__(self, dist=None, vertex=None):
    self.dist = dist
    self.vertex = vertex

def dijkstra(graph: Graph, from_vertex, get_weight):
  vetable = graph.vetable
  vsize = graph.vertexs.size()
  dist = HashMap(vsize)
  dist.put(from_vertex, 0)
  min_heap = Heap(vsize, pair_cmp)
  min_heap.push(pair(0, from_vertex))
  while not min_heap.is_empty():
    vertex = min_heap.top().vertex
    min_heap.pop()
    adjs = vetable.get_keys_by_row(vertex)
    for adj in adjs:
      old_dist = dist.get(adj)
      new_dist = dist.get(vertex) + get_weight(vetable.get(vertex, adj)) 
      if old_dist is None or (new_dist is not None and new_dist < old_dist):
        dist.put(adj, new_dist)
        min_heap.push(pair(new_dist, adj))
  return dist

    
    
  
  

