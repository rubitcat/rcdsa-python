from rcdsa.datastruct import LinkedStack
from rcdsa.datastruct import LinkedQueue
from rcdsa.datastruct import Tree

class BinaryTree(Tree):
      
  def __init__(self, seq=None):
    length = len(seq)
    if length == 0:
      self.root = None
    self.root = self.Node(seq[0])
    queue = LinkedQueue()
    queue.enqueue(self.root)
    i = 1
    while not queue.is_empty():
      curr = queue.front()
      queue.dequeue()
      if i < length:
        curr.left = self.Node(seq[i])
        queue.enqueue(curr.left)
        i += 1
      if i < length:
        curr.right = self.Node(seq[i])
        queue.enqueue(curr.right)
        i += 1

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
      if last_node_parent.left is not None:
        last_node_parent.left = None
      else:
        last_node_parent.right = None


  @classmethod
  def traversal_preorder(cls, root, func):    
    if root is None:
      return
    stack = LinkedStack()
    stack.push(root)
    while not stack.is_empty():
      curr = stack.top()
      stack.pop()
      if curr.right is not None:
        stack.push(curr.right)
      if curr.left is not None:
        stack.push(curr.left)
      func(curr.data)
      
  @classmethod
  def traversal_inorder(cls, root, func):
    if root is None:
      return
    stack = LinkedStack()
    curr = root
    while curr is not None or not stack.is_empty():
      while curr is not None:
        stack.push(curr)
        curr = curr.left
      curr = stack.top()
      stack.pop()
      func(curr.data)
      curr = curr.right
    
  @classmethod
  def traversal_postorder(cls, root, func):
    stack = LinkedStack()
    while True:
      while root is not None:
        stack.push(root)
        stack.push(root)
        root = root.left
      if stack.is_empty():
        return
      root = stack.top()
      stack.pop()
      if not stack.is_empty() and stack.top() == root:
        root = root.right
      else:
        func(root.data)
        root = None

  @classmethod
  def traversal_levelorder(cls, root, func):
    queue = LinkedQueue()
    queue.enqueue(root)
    while not queue.is_empty():
      curr = queue.front()
      queue.dequeue()
      if not curr.left is None:
        queue.enqueue(curr.left)
      if not curr.right is None:
        queue.enqueue(curr.right)
      func(curr.data)





    