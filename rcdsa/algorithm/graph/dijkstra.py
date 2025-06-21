from rcdsa.datastruct import Graph
from rcdsa.datastruct import HashMap
from rcdsa.datastruct import Heap


def dijkstra(graph: Graph, from_vertex, get_weight=lambda e: e.value, path: HashMap = None) -> HashMap:
  vetable = graph.vetable
  vsize = graph.vertexs.size()
  dist = HashMap(vsize)
  dist.put(from_vertex, 0)
  min_heap = Heap(vsize, cmp=lambda x,y: Heap.default_cmp(x[0], y[0]))
  min_heap.push((0, from_vertex))
  while not min_heap.is_empty():
    vertex = min_heap.top()[1]
    min_heap.pop()
    adjs = vetable.get_keys_by_row(vertex)
    if adjs is not None and (mid := dist.get(vertex)) is not None:
      for adj in adjs:
        if (adj_dist := dist.get(adj)) is None:
          new_dist = mid + get_weight(Graph.Edge(vertex, adj, vetable.get(vertex, adj)))
          dist.put(adj, new_dist)
          min_heap.push((new_dist, adj))
        elif (new_dist := mid + get_weight(Graph.Edge(vertex, adj, vetable.get(vertex, adj)))) < adj_dist:
          dist.put(adj, new_dist)
          min_heap.push((new_dist, adj))
  return dist

    
    
  
  

