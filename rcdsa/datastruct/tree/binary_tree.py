from rcdsa.datastruct import Tree
from rcdsa.datastruct import LinkedStack
from rcdsa.datastruct import LinkedQueue

class BinaryTree(Tree):
  class Node:
    def __init__(self, data=None, left=None, right=None, parent=None, **attributes):
      self.data  = data
      self.parent = parent
      self.left  = left
      self.right = right
      self.attrs = attributes

  def __init__(self):
    self.root = None

  def is_empty(self):
    return self.root is None
  
  def root(self):
    return self.root

  def insert(self, data=None):
    node = self.Node(data)
    if self.root is None:
      self.root = node
    else:
      queue = LinkedQueue()
      queue.enqueue(self.root)
      while not queue.is_empty():
        curr = queue.front()
        queue.dequeue()
        if curr.left is None:
          curr.left = node
          break
        else:
          queue.enqueue(curr.left)

        if curr.right is None:
          curr.right = node
          break
        else:
          queue.enqueue(curr.right)

  def delete(self, data=None):
    if self.root is None:
      return

    # find the node we want to delete
    target_root = None
    queue = LinkedQueue()
    queue.enqueue(self.root)
    while not queue.is_empty():
      curr = queue.front()
      queue.dequeue()
      if curr.data == data:
        target_root = curr
        break
      if curr.left is not None:
        queue.enqueue(curr.left)
      if curr.right is not None:
        queue.enqueue(curr.right)
    
    if target_root is None:
      return

    # find the latest node and it's parent node
    last_node = None
    last_node_parent = None 
    queue = LinkedQueue()
    queue.enqueue((self.root, None))
    while not queue.is_empty():
      curr, parent = queue.front()
      queue.dequeue()
      last_node = curr
      last_node_parent = parent
      if curr.left is not None:
        queue.enqueue((curr.left, curr))
      if curr.right is not None:
        queue.enqueue((curr.right, curr))

    # using the lastes node replace the node we want to delete
    target_root.data = last_node.data
    if last_node_parent is not None:
      if last_node_parent.left == last_node:
        last_node_parent.left = None
      else:
        last_node_parent.right = None

  def traversal_preorder(self, func):
    if self.root is None:
      return
    stack = LinkedStack()
    stack.push(self.root)
    while not stack.is_empty():
      curr = stack.top()
      stack.pop()
      if curr.right is not None:
        stack.push(curr.right)
      if curr.left is not None:
        stack.push(curr.left)
      func(curr.data)
      
  def traversal_inorder(self, func):
    if self.root is None:
      return
    stack = LinkedStack()
    curr = self.root
    while curr is not None or not stack.is_empty():
      while curr is not None:
        stack.push(curr)
        curr = curr.left
      curr = stack.top()
      stack.pop()
      func(curr.data)
      curr = curr.right
    
  def traversal_postorder(self, func):
    if self.root is None:
      return
    stack = LinkedStack()
    track_map = {}
    stack.push(self.root)
    while not stack.is_empty():
      curr = stack.top()
      track_map[curr] = True
      if curr.left is not None and not track_map.get(curr.left):
        stack.push(curr.left)
        continue
      if curr.right is not None and not track_map.get(curr.right):
        stack.push(curr.right)
        continue
      func(curr.data)
      stack.pop()

  def traversal_levelorder(self, func):
    if self.root is None:
      return
    queue = LinkedQueue()
    queue.enqueue(self.root)
    while not queue.is_empty():
      curr = queue.front()
      queue.dequeue()
      if curr.left is not None:
        queue.enqueue(curr.left)
      if curr.right is not None:
        queue.enqueue(curr.right)
      func(curr.data)
  
  def clear(self):
    self.root = None
    
  def get_parent_levelorder_seq(self) -> tuple[list,list]:
    if self.root is None:
      return [], []
    parent_seq = []
    levelorder_seq= []
    queue = LinkedQueue()
    queue.enqueue((self.root, -1))
    i = 0
    while not queue.is_empty():
      curr, parent_idx = queue.front()
      queue.dequeue()
      parent_seq.append(parent_idx)
      levelorder_seq.append(curr.data)
      if curr.left is not None:
        queue.enqueue((curr.left, i))
      if curr.right is not None:
        queue.enqueue((curr.right, i))
      i += 1
    return parent_seq, levelorder_seq, i

  def load_from_parent_levelorder_seq(self, parent_seq, levelorder_seq, count):
    assert len(parent_seq) == len(levelorder_seq) == count
    if count < 1:
      return
    nodes = [BinaryTree.Node(levelorder_seq[i]) for i in range(count)]
    self.root = None
    for i in range(count):
      if parent_seq[i] == -1:
        self.root = nodes[i]
      else:
        if nodes[parent_seq[i]].left is None:
          nodes[parent_seq[i]].left = nodes[i]
        else:
          nodes[parent_seq[i]].right = nodes[i]

  def get_levelorder_seq(self) -> list:
    levelorder_seq = []
    self.traversal_levelorder(lambda v: levelorder_seq.append(v))
    return levelorder_seq

  def load_from_cbt_levelorder_seq(self, levelorder_seq, count):
    if len(levelorder_seq) == 0:
      self.root = None
      return
    self.root = self.Node(levelorder_seq[0])
    queue = LinkedQueue()
    queue.enqueue(self.root)
    i = 1
    while not queue.is_empty():
      curr = queue.front()
      queue.dequeue()
      if i < count:
        curr.left = self.Node(levelorder_seq[i])
        queue.enqueue(curr.left)
        i += 1
      if i < count:
        curr.right = self.Node(levelorder_seq[i])
        queue.enqueue(curr.right)
        i += 1

