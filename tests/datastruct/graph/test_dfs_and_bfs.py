from rcdsa.datastruct import StableGraph
from rcdsa.algorithm.graph import cycle_detect

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


def test_cycle_detected():
  graph = StableGraph(directed=True)
  edges = [
    [0,1],
    [2,1],
    [2,3],
    [3,4],
    [4,5],
    [5,3],
  ]
  for v in range(6):
    graph.insert_vertex(v)
  for e in edges:
    graph.insert_edge(e[0], e[1], None)
  
  assert cycle_detect(graph)  == True


  graph2 = StableGraph(directed=False)
  edges2 = [
    [0,1],
    [2,3],
    [3,4],
    [4,5],
    [5,3],
  ]
  for v in range(6):
    graph2.insert_vertex(v)
  for e in edges2:
    graph2.insert_edge(e[0], e[1], None)
  
  assert cycle_detect(graph2)  == True