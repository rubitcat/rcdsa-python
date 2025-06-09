from rcdsa.datastruct import RedBlackTree

class HashSet:
  
  class Entry:
    def __init__(self, data=None):
      self.data = data
    def __hash__(self):
      return self.data.__hash__()
    def __eq__(self, o):
      return self.data == o.data if o is not None else False

  def __init__(self):
    self._rbt = RedBlackTree()
    self.size = 0

  def _new_entry(self, data=None):
    return self.Entry(data)
  
  def _after_entry_insert(self, entry):
    pass

  def _after_entry_remove(self, entry):
    pass

  def is_empty(self):
    return self.size == 0

  def put(self, data, overwrite=True):
    new_entry = self._new_entry(data)
    entry = self._rbt.insert(new_entry, overwrite)
    if entry == new_entry:
      self.size += 1
      self._after_entry_insert(new_entry)

  def remove(self, data):
    if self.is_empty():
      raise RuntimeError("HashSet underflow")
    deleted_entry = self._rbt.delete(self.Entry(data))
    if deleted_entry is not None:
      self.size -= 1
    self._after_entry_remove(deleted_entry)
     
  def contains(self, data):
    return self._rbt.contains(self.Entry(data))

  def traversal(self, callback):
    self._rbt.traversal_preorder(lambda entry: callback(entry.data))