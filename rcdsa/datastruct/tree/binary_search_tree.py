from rcdsa.datastruct import BinaryTree

class BinarySearchTree(BinaryTree):
  def __init__(self, cmp=lambda x, y: (x.__gt__(y)) - (x.__lt__(y))):
    super().__init__()
    self.cmp = cmp

  def insert(self, data):
    if self.root is None:
      self.root = self.Node(data)
      return
    # find the leaf node to be inserted
    curr = self.root
    curr_parent = None
    while curr is not None:
      if self.cmp(data, curr.data) < 0 :
        curr_parent = curr
        curr = curr.left
      elif self.cmp(data, curr.data) > 0:
        curr_parent = curr
        curr = curr.right 
      else:
        return

    if self.cmp(data, curr_parent.data) < 0:
      curr_parent.left = self.Node(data)
    elif self.cmp(data, curr_parent.data) > 0:
      curr_parent.right = self.Node(data)

  def delete(self, data):
    if self.root is None:
      return
    
    # find the node we want to delete
    curr = self.root
    curr_parent = None
    while curr is not None:
      if self.cmp(data, curr.data) < 0 :
        curr_parent = curr 
        curr = curr.left
      elif self.cmp(data, curr.data) >0:
        curr_parent = curr 
        curr = curr.right
      else:
        break
    if curr is None:
      return

    if curr.left is not None and curr.right is not None:
      temp = curr
      curr_parent = curr
      curr = curr.right
      while curr.left is not None:
        curr_parent = curr
        curr = curr.left
      temp.data = curr.data
    
    # delete the node
    curr_succ = curr.left if curr.left is not None else curr.right
    if curr_parent is None:
      self.root = curr_succ
    else:
      if curr_parent.left == curr:
        curr_parent.left = curr_succ
      else:
        curr_parent.right = curr_succ

  def search(self, data):
    curr = self.root
    while curr is not None:
      if self.cmp(data, curr.data) < 0:
        curr = curr.left
      elif self.cmp(data, curr.data) > 0:
        curr = curr.right
      else:
        break
      
    if curr is not None:
      return data
    else:
      return None
    