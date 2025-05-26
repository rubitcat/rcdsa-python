from .hash_map import HashMap
from rcdsa.datastruct import RedBlackTree

class HashTable:
  def __init__(self):
    self.data = HashMap()
    
  def put(self, row, col, value):
    col_map = self.data.get(row)
    if col_map is None:
      col_map = HashMap()
      self.data.put(row, col_map)
    col_map.put(col, value)

  def get(self, row, col):
    col_map = self.data.get(row)
    if col_map is None:
      return
    else:
      return col_map.get(col)
  
  def rows(self):
    return self.data.keys()
  
  def cols(self):
    res = []
    rbt = RedBlackTree()
    rows = self.data.keys()
    for row in rows:
      col_map = self.data.get(row)
      cols = col_map.keys()
      for col in cols:
        rbt.insert(col, False)
    rbt.traversal_preorder(lambda col: res.append(col))
    return res