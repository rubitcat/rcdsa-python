from rcdsa.datastruct import StableGraph
from rcdsa.algorithm.graph import topo_sort
from rcdsa.algorithm.graph import all_topo_sort


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