from rcdsa.datastruct import Graph 
from rcdsa.datastruct import UnionFindSet
from rcdsa.datastruct import LinkedList
from rcdsa.algorithm import sort


def kruskal_mst(graph: Graph, mst: Graph, get_weight):
  edges = graph.edges.values()
  sort.quick_sort(edges, cmp=lambda x, y: sort.default_cmp(
    get_weight(x.edge), 
    get_weight(y.edge))
  )
  ufs = UnionFindSet()
  graph.vertexs.traversal(lambda v: (ufs.add(v), mst.insert_vertex(v)))
  count = 0
  cost = 0
  vsize = graph.vertexs.size()
  for edge in edges:
    # cycle detect using union-find set
    if not ufs.is_united(edge.from_vertex, edge.to_vertex):
      mst.insert_edge(edge.from_vertex, edge.to_vertex, edge.edge)
      ufs.union(edge.from_vertex, edge.to_vertex)
      count += 1
      cost += get_weight(edge.edge)
      if count == vsize - 1: 
        break
  return cost
