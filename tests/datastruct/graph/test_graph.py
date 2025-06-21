import pytest
from rcdsa.datastruct import StableGraph
from rcdsa.algorithm.graph import dijkstra
from rcdsa.algorithm.graph import kruskal_mst
from rcdsa.algorithm.graph import prim_mst
from rcdsa.algorithm.graph import boruvka_mst
from rcdsa.algorithm.graph import topo_sort
from rcdsa.algorithm.graph import all_topo_sort
from rcdsa.algorithm.graph import floyd_warshall
from rcdsa.algorithm.graph import bellman_ford

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

def test_shortest_path():
  graph = StableGraph(directed=False)
  res = []
  vn = 5
  edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]] 
  for i in range(vn):
    graph.insert_vertex(i)
  for edge in edges:
    graph.insert_edge(edge[0], edge[1], edge[2])
  
  dist = dijkstra(graph, 0, lambda x: x)
  assert dist.get(0) == 0
  assert dist.get(1) == 4
  assert dist.get(2) == 8
  assert dist.get(3) == 10
  assert dist.get(4) == 10

  dist2 = floyd_warshall(graph, lambda x: x)
  assert dist2.get(0,0) == 0
  assert dist2.get(0,1) == 4
  assert dist2.get(0,2) == 8
  assert dist2.get(0,3) == 10
  assert dist2.get(0,4) == 10

  graph2 = StableGraph(directed=True)
  edge2 = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
  for v in range(5):
    graph2.insert_vertex(v)
  for e in edge2:
    graph2.insert_edge(e[0], e[1], e[2])
  dist3 = bellman_ford(graph2, 0, lambda x: x)
  assert dist3.get(0) == 0
  assert dist3.get(1) == 5
  assert dist3.get(2) == 6
  assert dist3.get(3) == 6
  assert dist3.get(4) == 7

  graph3 = StableGraph(directed=True)
  edge3 = [[0, 1, 1], [1, 2, 1], [2, 0, -4]]
  for v in range(3):
    graph3.insert_vertex(v)
  for e in edge3:
    graph3.insert_edge(e[0], e[1], e[2])
  with pytest.raises(RuntimeError) as exc_info:
    dist4 = bellman_ford(graph3, 0, lambda x: x)

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

def test_topo_sort():
  graph = StableGraph()
  vertex = 7
  edge = [
    [0,1],
    [0,2],
    [1,2],
    [1,3],
    [2,4],
    [4,5],
    [3,6],
    [3,5],
  ]
  for v in range(vertex):
    graph.insert_vertex(v)
  for e in edge:
    graph.insert_edge(e[0], e[1], None)
  
  res = topo_sort(graph)
  for e in edge:
    for i in range(len(res)):
      if res[i] == e[0]:
        j = i + 1
        finded = False
        while j < len(res):
          if res[j] == e[1]:
            finded = True
            break
          j += 1
        assert finded == True
        break
  
  res2 = all_topo_sort(graph)
  for res in res2:
    for e in edge:
      for i in range(len(res)):
        if res[i] == e[0]:
          j = i + 1
          finded = False
          while j < len(res):
            if res[j] == e[1]:
              finded = True
              break
            j += 1
          assert finded == True
          break