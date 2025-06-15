from rcdsa.datastruct import HashMap
from rcdsa.datastruct import LinkedStack
from rcdsa.datastruct import LinkedList

class UnionFindSet:
  def __init__(self, enable_path_compress=True, enable_union_by_rank=True):
    self._parent = HashMap()
    if enable_union_by_rank:
      self._rank = HashMap()
    self.path_compress = enable_path_compress
    self.union_by_rank= enable_union_by_rank

  def add(self, x):
    self._parent.put(x, x)

  def union(self, x, y):
    xroot = self.find(x)
    yroot = self.find(y)
    if xroot == yroot:
      return
    
    if self.union_by_rank: 
      xrank = self._rank.get(xroot)
      yrank = self._rank.get(yroot)
      if xrank is None:
        xrank = 0
      if yrank is None:
        yrank = 0
      if xrank < yrank:
        self._parent.put(xroot, yroot)
      elif xrank > yrank: 
        self._parent.put(yroot, xroot)
      else:
        self._parent.put(xroot, yroot)
        self._rank.put(yroot, yrank + 1)
    else:
      self._parent.put(xroot, yroot)
    
  def find(self, x):
    xp = self._parent.get(x)
    xpp = self._parent.get(xp)
    if xp != xpp:
      if self.path_compress:
        path = LinkedList()
        while xp != xpp:
          path.append(xp)
          xp = xpp
          xpp = self._parent.get(xp)
        if path.size > 1:
          path.traversal(lambda p: self._parent.put(p, x))
      else:
        while xp != xpp:
          xp = xpp
          xpp = self._parent.get(xp)
    return xp

  def is_united(self, x, y):
    res = self.find(x) == self.find(y)
    return res 