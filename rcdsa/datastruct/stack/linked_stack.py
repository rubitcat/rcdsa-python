class LinkedStack:
  class Node:
    def __init__(self, data=None, next=None):
      self.data = data
      self.next = next
  def __init__(self):
    self._top = None
  def is_empty(self):
    return self._top is None
  def push(self, item):
    node = LinkedStack.Node(item,self._top)
    self._top = node
  def pop(self):
    if self.is_empty():
      raise RuntimeError("Stack underflow")
    tmp = self._top
    self._top = tmp.next
  def top(self):
    if self.is_empty():
      raise RuntimeError("Stack is empty")
    return self._top.data
  def secondary(self):
    if self.is_empty():
      raise RuntimeError("Stack is empty")
    return self._top.next.data if self._top.next is not None else None