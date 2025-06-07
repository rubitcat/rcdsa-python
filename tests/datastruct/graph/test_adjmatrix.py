from rcdsa.datastruct import AdjMatrix


def test_adjmatrix():
  data = [[1,2], [0,2,3], [0,1,4], [1,4], [2,3]]
  adjMatrix = AdjMatrix(directed=False)
  res = []
  for i in range(5):
    adjMatrix.insert_vertex(i)
  for i in range(5):
    for j in range(len(data[i])):
      adjMatrix.insert_edge(i,  data[i][j], 1)
  
  adjMatrix.traversal_bfs(lambda x: res.append(x), 0)
  assert res == [0, 1, 2, 3, 4]
  print("hello world")

