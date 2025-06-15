from rcdsa.datastruct import HashMap

class HashSet:

  def __init__(self):
    self._map = self._new_map()
  
  def _new_map(self):
    return HashMap()

  def is_empty(self):
    return self._map.size() == 0
  
  def size(self):
    return self._map.size()

  def put(self, data, overwrite=True):
    self._map.put(data, None, overwrite=True)

  def remove(self, data):
    self._map.remove(data)
     
  def contains(self, data):
    return self._map.contains(data)

  def traversal(self, callback):
    self._map.traversal(lambda e: callback(e.key))
  
  def first(self):
    entry = self._map.first()
    return entry.key if entry is not None else None

  def values(self):
    return self._map.keys()
