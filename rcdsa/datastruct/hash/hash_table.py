from rcdsa.datastruct import HashMap
from rcdsa.datastruct import HashSet

class HashTable:
  def __init__(self):
    self.data = HashMap()
  
  def _new_map(self):
    return HashMap()
  
  def _new_set(self):
    return HashSet()

  def put(self, row, col, value, overwrite=True):
    col_map = self.data.get(row)
    if col_map is None:
      col_map = self._new_map()
      self.data.put(row, col_map, overwrite)
    col_map.put(col, value, overwrite)

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
    return col_map.remove(col)

  def remove_row(self, row):
    self.data.remove(row)

  def remove_col(self, col):
    rows = self.data.keys()
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