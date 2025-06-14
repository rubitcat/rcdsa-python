

class LinkedList:
  class Node:
    def __init__(self, data=None, prev=None, next=None):
      self.data = data
      self.next = next
      self.prev = prev
  
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  def insert(self, data, index=-1):
    if index == 0 or index == -1 or index == self.size - 1:
      return self.append(data)
    elif index < -1 or index >= self.size:
      raise IndexError(index)

    curr = self.head
    for _ in range(index):
      curr = curr.next
    node = self.Node(data, curr.prev, curr)
    curr.prev.next = node
    curr.prev = node
    self.size += 1

  def delete(self, index=-1):
    if index < 0 or index > self.size:
      raise IndexError(index)

    curr = self.head
    for _ in range(index):
      curr = curr.next
    if curr.prev is not None:
      curr.prev.next = curr.next
    else:
      self.head = curr.next

    if curr.next is not None:
      curr.next.prev = curr.prev
    else:
      self.tail = curr.prev

    self.size -= 1
    return curr.data

  def append(self, data):
    node = self.Node(data)
    if self.tail is not None:
      node.prev = self.tail
      self.tail.next = node
      self.tail = node
    else:
      self.head = node
      self.tail = node
    self.size += 1
  
  def pop(self):
    if self.tail is None:
      return
    tail = self.tail
    self.tail.next = None
    self.tail = self.tail.prev
    return tail.data
  
  def traversal(self, callback, reverse=False):
    if not reverse:
      curr = self.head
      while curr is not None:
        callback(curr.data)
        curr = curr.next
    else:
      curr = self.tail
      while curr is not None:
        callback(curr.data)
        curr = curr.prev

      