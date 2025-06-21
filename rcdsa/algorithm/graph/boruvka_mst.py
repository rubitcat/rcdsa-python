from rcdsa.datastruct import Graph
from rcdsa.datastruct import UnionFindSet
from rcdsa.datastruct import HashMap

def boruvka_mst(graph: Graph, mst: Graph, get_weight=lambda e: e.value, path: HashMap = None):
  if graph.directed:
    raise RuntimeError("graph must be an undirected graph") 
  edges = graph.edges.values()
  ufs = UnionFindSet()
  graph.vertexs.traversal(lambda v: (ufs.add(v), mst.insert_vertex(v)))
  tree_count = graph.vertexs.size()
  cost = 0
  while tree_count > 1:
    cheapest_edge = HashMap()
    for edge in edges:
      xroot = ufs.find(edge.from_vertex)
      yroot = ufs.find(edge.to_vertex)
      if xroot is not yroot:
        xedge = cheapest_edge.get(xroot)
        yedge = cheapest_edge.get(yroot)
        if xedge is None or get_weight(edge) < get_weight(xedge):
          cheapest_edge.put(xroot, edge)
        if yedge is None or get_weight(edge) < get_weight(yedge):
          cheapest_edge.put(yroot, edge)

    for edge in cheapest_edge.values():
      xroot = ufs.find(edge.from_vertex)
      yroot = ufs.find(edge.to_vertex)
      if xroot is not yroot:
        mst.insert_edge(edge.from_vertex, edge.to_vertex, edge.value)
        ufs.union(xroot, yroot)
        cost += get_weight(edge)
        tree_count -= 1
  return cost