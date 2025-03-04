class ArrayQueue:
  def __init__(self, capacity):
    self._data = [None] * capacity
    self._capacity = capacity
    self._size = 0
    self._front = 0
  def is_empty(self):
    return self._size == 0
  def is_full(self):
    return self._size == self._capacity
  def enqueue(self, item):
    if self.is_full():
      raise RuntimeError("Queue overflow")
    rear = (self._front + self._size) % self._capacity
    self._data[rear] = item
    self._size += 1
  def dequeue(self):
    if self.is_empty():
      raise RuntimeError("Queue underflow")
    self._front = (self._front + 1) % self._capacity
    self._size -= 1
  def front(self):
    if self.is_empty():
      raise RuntimeError("Queue is empty")
    return self._data[self._front]
  def rear(self):
    if self.is_empty():
      raise RuntimeError("Queue is empty")
    rear = (self._front + self._size - 1) % self._capacity
    return self._data[rear]