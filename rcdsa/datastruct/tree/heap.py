from rcdsa.datastruct import LinkedQueue

class Heap:
  
  def __init__(self, capacity, cmp=lambda x, y: (x.__gt__(y)) - (x.__lt__(y))):
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
  def heappush(cls, data, heap, size, cmp=lambda x, y: (x.__gt__(y)) - (x.__lt__(y))):
    curr = size
    while curr != 0 and cmp(data, heap[(curr-1)//2]) > 0:
      heap[curr] = heap[(curr-1)//2]
      curr = (curr-1)//2
    heap[curr] = data

  @classmethod
  def heappop(cls, heap, size, cmp=lambda x, y: (x.__gt__(y)) - (x.__lt__(y))):
    last = size - 1
    curr = 0 
    mxx = 1
    while curr*2+1 < size:
      if cmp(heap[mxx+1], heap[mxx]) > 0:
         mxx += 1
      if cmp(heap[last], heap[mxx]) > 0:
        break
      heap[curr] = heap[mxx]
      curr = mxx
      mxx = mxx*2+1
    heap[curr] = heap[last]

  @classmethod
  def heapfify(cls, arr, size, cmp=lambda x, y: (x.__gt__(y)) - (x.__lt__(y))):
    pass





