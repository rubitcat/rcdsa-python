from rcdsa.datastruct import HashMap
from rcdsa.datastruct import HashSet

class HashTable:
  
  class Entry:
    def __init__(self, row=None, col=None, value=None):
      self.row = row
      self.col = col
      self.value = value

  def __init__(self):
    self.data = self._new_map()
    self._size = 0
  
  def _new_map(self):
    return HashMap()
  
  def _new_set(self):
    return HashSet()

  def size(self):
    return self._size

  def put(self, row, col, value, overwrite=True):
    col_map = self.data.get(row)
    if col_map is None:
      col_map = self._new_map()
      self.data.put(row, col_map, overwrite)
    res = col_map.put(col, value, overwrite)
    if res == value:
      self._size += 1

  def get(self, row, col):
    col_map = self.data.get(row)
    if col_map is None:
      return
    return col_map.get(col)

  def get_values_by_row(self, row):
    col_map = self.data.get(row)
    if col_map is None:
      return
    return col_map.values()
  
  def get_keys_by_row(self, row):
    col_map = self.data.get(row)
    if col_map is None:
      return
    return col_map.keys()

  def remove(self, row, col):
    col_map = self.data.get(row)
    if col_map is None:
      return
    removed = col_map.remove(col)
    if removed is not None:
      self._size -= 1
    return removed

  def remove_row(self, row):
    return self.data.remove(row)

  def remove_col(self, col):
    rows = self.data.values()
    for row in rows:
      row.remove(col)

  def get_rows(self):
    return self.data.keys()
  
  def get_cols(self):
    res = []
    rows = self.data.keys()
    res_set = self._new_set()
    for row in rows:
      col_map = self.data.get(row)
      cols = col_map.keys()
      for col in cols:
        res_set.put(col, False)
    res_set.traversal(lambda col: res.append(col))
    return res
  
  def traversal(self, callback):
    def _process_row(row):
      nonlocal callback
      def _process_col(col):
        nonlocal callback
        nonlocal row
        callback(self.Entry(row.key, col.key, col.value))
      row.value.traversal(_process_col)
    self.data.traversal(_process_row)
  
  def entries(self):
    res = [None] * self._size 
    pt = 0
    def _processor(entry):
      nonlocal res
      nonlocal pt
      res[pt] = entry
      pt += 1
    self.traversal(_processor)
    return res
