from rcdsa.datastruct import StableGraph
from rcdsa.algorithm.dijkstra import dijkstra
from rcdsa.algorithm.kruskal_mst import kruskal_mst
from rcdsa.algorithm.prim_mst import prim_mst
from rcdsa.algorithm.boruvka_mst import boruvka_mst

def test_graph():
  data = [[1,2], [0,2,3], [0,1,4], [1,4], [2,3]]
  graph = StableGraph(directed=False)
  res = []
  for i in range(5):
    graph.insert_vertex(i)
  for i in range(5):
    for j in range(len(data[i])):
      graph.insert_edge(i,  data[i][j], 1)
  
  graph.traversal_bfs(lambda x: res.append(x), 0)
  assert res == [0, 1, 2, 3, 4]

  res.clear()
  graph.traversal_dfs(lambda x: res.append(x), 0)
  assert res == [0, 1, 2, 4, 3]

def test_dijkstra():
  graph = StableGraph(directed=False)
  res = []
  vn = 5
  edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]] 
  for i in range(vn):
    graph.insert_vertex(i)
  for edge in edges:
    graph.insert_edge(edge[0], edge[1], edge[2])
  
  dist = dijkstra(graph, 0, lambda x: x)
  dist.traversal(lambda x: res.append([x.key, x.value]))
  assert [[0,0],[1,4],[2,8],[3,10],[4,10]] == res

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
  assert kruskal_mst(graph, kruskal_mst_res, lambda x: x) == 37

  # prim_mst
  prim_mst_res = StableGraph(directed=False)
  assert prim_mst(graph, prim_mst_res, lambda x: x) == 37

  boruvka_mst_res = StableGraph(directed=False)
  assert boruvka_mst(graph, boruvka_mst_res, lambda x: x) == 37