import pytest
from rcdsa.datastruct import StableGraph
from rcdsa.algorithm.graph import dijkstra
from rcdsa.algorithm.graph import floyd_warshall
from rcdsa.algorithm.graph import bellman_ford
from rcdsa.algorithm.graph import johnson


def test_shortest_path():
  graph = StableGraph(directed=False)
  res = []
  vn = 5
  edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]] 
  for i in range(vn):
    graph.insert_vertex(i)
  for edge in edges:
    graph.insert_edge(edge[0], edge[1], edge[2])
  
  # dijkstra
  dist = dijkstra(graph, 0)
  assert dist.get(0) == 0
  assert dist.get(1) == 4
  assert dist.get(2) == 8
  assert dist.get(3) == 10
  assert dist.get(4) == 10

  # floyd_warshall
  dist2 = floyd_warshall(graph)
  assert dist2.get(0,0) == 0
  assert dist2.get(0,1) == 4
  assert dist2.get(0,2) == 8
  assert dist2.get(0,3) == 10
  assert dist2.get(0,4) == 10

  # bellman_ford
  graph2 = StableGraph(directed=True)
  edge2 = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
  for v in range(5):
    graph2.insert_vertex(v)
  for e in edge2:
    graph2.insert_edge(e[0], e[1], e[2])
  dist3 = bellman_ford(graph2, 0)
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
    bellman_ford(graph3, 0)

  # johnson
  graph4 = StableGraph(directed=True)
  edge4 = [[0,1,-5],[0,3,3],[0,2,2],[1,2,4],[2,3,1]]
  for v in range(4):
    graph4.insert_vertex(v)
  for e in edge4:
    graph4.insert_edge(e[0], e[1], e[2])
  dist4 = johnson(graph4)
  assert dist4.get(0,0) == 0
  assert dist4.get(0,1) == 0
  assert dist4.get(0,2) == 0
  assert dist4.get(0,3) == 0
  

