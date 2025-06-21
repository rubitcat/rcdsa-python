from rcdsa.datastruct import Graph
from rcdsa.datastruct import HashTable
from rcdsa.algorithm.graph import bellman_ford
from rcdsa.algorithm.graph import dijkstra

def johnson(graph: Graph, get_weight=lambda e: e.value, path: HashTable = None) -> HashTable:
  res = HashTable()
  tmep_graph = Graph(graph.directed)
  tmep_graph.insert_vertex("s")
  graph.vertexs.traversal(lambda v: (tmep_graph.insert_vertex(v), tmep_graph.insert_edge("s", v, 0)))
  graph.edges.traversal(lambda e: tmep_graph.insert_edge(e.from_vertex, e.to_vertex, get_weight(e)))
  hmap = bellman_ford(tmep_graph, "s")
  tmep_graph.delete_vertex("s")
  tmep_graph.edges.traversal(lambda e: tmep_graph.insert_edge(e.from_vertex, e.to_vertex, 
    e.value + hmap.get(e.from_vertex) - hmap.get(e.to_vertex)
  ))
  tmep_graph.vertexs.traversal(lambda v: (
    dist := dijkstra(tmep_graph, v),
    dist.traversal(lambda e: res.put(v, e.key, e.value))
  ))
  return res