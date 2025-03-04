class LinkedQueue:
  class Node:
    def __init__(self, data=None, next=None):
      self.data = data
      self.next = next
  def __init__(self):
    self._front = None
    self._rear = None
  def is_empty(self):
    return self._front is None and self._rear is None
  def enqueue(self, item):
    node = LinkedQueue.Node(item, None)
    if self.is_empty():
      self._front = node
      self._rear = node
    else:
      self._rear.next = node
      self._rear = node
  def dequeue(self):
    if self.is_empty():
      raise RuntimeError("Queue underflow")
    tmp = self._front
    self._front = self._front.next
    if self._front is None:
      self._rear = None
  def front(self):
    if self.is_empty():
      raise RuntimeError("Queue is empty")
    return self._front.data
  def rear(self):
    if self.is_empty():
      raise RuntimeError("Queue is empty")
    return self._rear.data
