from rcdsa.datastruct import RedBlackTree

class HashSet:
  
  def __init__(self):
    self._rbt = RedBlackTree()
    self.size = 0

  def is_empty(self):
    return self.size == 0

  def put(self, data, overwrite=True):
    self.size += 1
    self._rbt.insert(data, overwrite)

  def remove(self, data):
    if self.is_empty():
      raise RuntimeError("HashSet underflow")
    self.size -= 1
    return self._rbt.delete(data)
     
  def contains(self, data):
    return self._rbt.contains(data)

  def traversal(self, callback):
    self._rbt.traversal_preorder(callback)