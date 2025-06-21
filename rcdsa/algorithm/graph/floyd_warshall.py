from rcdsa.datastruct import Graph
from rcdsa.datastruct import HashTable

def floyd_warshall(graph: Graph, get_weight=lambda e: e.value, path: HashTable = None) -> HashTable:
  dist = HashTable()
  graph.vetable.traversal(lambda e: dist.put(e.row, e.col, get_weight(e)))
  vertexs = graph.vertexs.values()
  for v in vertexs:
    dist.put(v, v, 0)
  for k in vertexs:
    for i in vertexs:
      if i is k:
        continue
      for j in vertexs:
        if j is k or i is j:
          continue
        ik = dist.get(i, k)
        kj = dist.get(k, j)
        ij = dist.get(i, j)
        if ik is not None and kj is not None:
          if ij is None:
            dist.put(i, j, ik+kj)
          else:
            dist.put(i, j, min(ij, ik+kj))
  return dist