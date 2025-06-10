from rcdsa.datastruct import StableGraph


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