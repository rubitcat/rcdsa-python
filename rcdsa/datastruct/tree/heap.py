
class Heap:
  @staticmethod
  def default_cmp(x, y):
    if x > y:
      return 1
    elif x < y:
      return -1
    else:
      return 0

  def __init__(self, capacity, cmp=default_cmp):
    self.cmp = cmp
    self.capacity = capacity
    self.heap = [None] * capacity
    self.size = 0
    
  def is_empty(self):
    return self.size == 0
  
  def is_full(self):
    return self.size == self.capacity

  def push(self, data):
    if self.is_full():
      raise RuntimeError("heap overflow")
    self.heappush(data, self.heap, self.size, self.cmp)
    self.size += 1

  def pop(self):
    if self.is_empty():
      raise RuntimeError("heap underflow")
    self.heappop(self.heap, self.size, self.cmp)
    self.size -= 1

  def top(self):
    if self.is_empty():
      raise RuntimeError("heap is empty")
    return self.heap[0]
  
  @classmethod
  def heappush(cls, data, arr, size, cmp=default_cmp):
    arr[size] = data
    cls.heapify_bottom_up(arr, size, cmp)

  @classmethod
  def heappop(cls, arr, size, cmp=default_cmp):
    last = size - 1
    arr[0] = arr[last]
    arr[last] = None
    cls.heapify(arr, size-1, 0, cmp)

  @classmethod
  def heapify(cls, arr, size, start, cmp=default_cmp):
    top = arr[start]
    curr = start
    mxx = start*2+1
    while mxx < size:
      if mxx+1 < size and cmp(arr[mxx], arr[mxx+1]) > 0:
         mxx += 1
      if cmp(arr[mxx], top) > 0:
        break
      arr[curr] = arr[mxx]
      curr = mxx
      mxx = mxx*2+1
    if curr != start:
      arr[curr] = top
  
  @classmethod
  def heapify_bottom_up(cls, arr, index, cmp=default_cmp):
    data = arr[index]
    curr = index
    while curr != 0 and cmp(arr[(curr-1)//2], data) > 0:
      arr[curr] = arr[(curr-1)//2]
      curr = (curr-1)//2
    if curr != index:
      arr[curr] = data