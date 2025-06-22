class ArrayStack:
  def __init__(self, capacity):
    self._data = [None] * capacity
    self._capacity = capacity
    self._size = 0
    self._top = -1
  def is_empty(self):
    return self._size == 0
  def is_full(self):
    return self._size == self._capacity
  def push(self, item):
    if self.is_full():
      raise RuntimeError("Stack overflow")
    self._top += 1
    self._data[self._top] = item
    self._size += 1
  def pop(self):
    if self.is_empty():
      raise RuntimeError("Stack underflow")
    self._top -= 1
    self._size -= 1
  def top(self):
    if self.is_empty():
      raise RuntimeError("Stack is empty")
    return self._data[self._top]
  def secondary(self):
    if self.is_empty():
      raise RuntimeError("Stack is empty")
    return self._data[self._top-1]