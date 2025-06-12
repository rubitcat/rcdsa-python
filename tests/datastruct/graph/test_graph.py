from rcdsa.datastruct import StableGraph
from rcdsa.algorithm.dijkstra import dijkstra

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
