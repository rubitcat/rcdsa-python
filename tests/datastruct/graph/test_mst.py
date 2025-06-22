from rcdsa.datastruct import StableGraph
from rcdsa.algorithm.graph import kruskal_mst
from rcdsa.algorithm.graph import prim_mst
from rcdsa.algorithm.graph import boruvka_mst


def test_mst():
  graph = StableGraph(directed=False)
  vn = 9
  edges = [
    [0, 1, 4],
    [0, 7, 8],
    [1, 7, 11],
    [1, 2, 8],
    [7, 8, 7],
    [7, 6, 1],
    [2, 8, 2],
    [8, 6, 6],
    [2, 3, 7],
    [2, 5, 4],
    [6, 5, 2],
    [3, 5, 14],
    [3, 4, 9],
    [5, 4, 10],
  ]
  for i in range(vn):
    graph.insert_vertex(i)
  for edge in edges:
    graph.insert_edge(edge[0], edge[1], edge[2])

  # kruskal_mst
  kruskal_mst_res = StableGraph(directed=False)
  assert kruskal_mst(graph, kruskal_mst_res) == 37

  # prim_mst
  prim_mst_res = StableGraph(directed=False)
  assert prim_mst(graph, prim_mst_res) == 37

  boruvka_mst_res = StableGraph(directed=False)
  assert boruvka_mst(graph, boruvka_mst_res) == 37