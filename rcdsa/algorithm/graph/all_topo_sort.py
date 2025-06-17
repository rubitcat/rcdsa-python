from rcdsa.datastruct import Graph
from rcdsa.datastruct import HashMap

def _topo_sort_util(vertexs, vetable, discovered_map, indeg_map, path, result):
  for v in vertexs:
    discovered = discovered_map.get(v)
    indeg = indeg_map.get(v)
    if indeg == 0 and not discovered:
      adjs = vetable.get_keys_by_row(v)

      if adjs is not None:
        for adj in adjs:
          indeg_map.put(adj, indeg_map.get(adj)-1)
      discovered_map.put(v, True)
      path.append(v)

      _topo_sort_util(vertexs, vetable, discovered_map, indeg_map, path, result)

      discovered_map.put(v, False)
      path.pop()
      if adjs is not None:
        for adj in adjs:
          indeg_map.put(adj, indeg_map.get(adj)+1)
  
  if len(path) == len(vertexs):
    result.append(list(path))
  
def all_topo_sort(graph: Graph) -> list:
  res = []
  discovered_map = HashMap()
  indeg_map = HashMap()
  graph.vertexs.traversal(lambda v: indeg_map.put(v, 0))
  graph.edges.traversal(lambda e: indeg_map.put(e.to_vertex, indeg_map.get(e.to_vertex)+1))
  _topo_sort_util( graph.vertexs.values(), graph.vetable, discovered_map, indeg_map, [], res)
  return res
