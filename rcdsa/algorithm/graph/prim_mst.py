from rcdsa.datastruct import Graph
from rcdsa.datastruct import HashSet
from rcdsa.datastruct import Heap

def prim_mst(graph: Graph, mst: Graph, get_weight=lambda e: e.value):
  if graph.directed:
    raise RuntimeError("graph must be an undirected graph") 
  vetable = graph.vetable 
  visited = HashSet()
  min_heap = Heap(graph.edges.size(), lambda x,y: Heap.default_cmp(x[0], y[0]))
  first_vertex = graph.vertexs.first()
  min_heap.push((0, None, first_vertex, None))
  graph.vertexs.traversal(lambda v: mst.insert_vertex(v))
  cost = 0
  while not min_heap.is_empty():
    weight, from_vertex, to_vertex, edge = min_heap.top()
    min_heap.pop()
    if visited.contains(to_vertex):
      continue
    cost += weight
    if edge is not None:
      mst.insert_edge(from_vertex, to_vertex, edge)
    visited.put(to_vertex)
    adjs = vetable.get_keys_by_row(to_vertex)
    for adj in adjs:
      if not visited.contains(adj):
        adj_edge = vetable.get(to_vertex, adj)
        adj_edge_weight = get_weight(Graph.Edge(to_vertex, adj, adj_edge))
        min_heap.push((adj_edge_weight, to_vertex, adj, adj_edge))
  return cost