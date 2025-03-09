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
    parent = None
    while curr is not None:
      parent = curr
      if self.cmp(data, curr.data) < 0 :
        curr = curr.left
      elif self.cmp(data, curr.data) > 0:
        curr = curr.right 
      else:
        return

    if self.cmp(data, parent.data) < 0:
      parent.left = self.Node(data)
    elif self.cmp(data, parent.data) > 0:
      parent.right = self.Node(data)

  def delete(self, data):
    if self.root is None:
      return
    
    # find the node we want to delete
    curr = self.root
    curr_parent = None
    while curr is not None and self.cmp(data, curr.data) != 0:
      curr_parent = curr 
      if self.cmp(data, curr.data) < 0 :
        curr = curr.left
      else:
        curr = curr.right
    if curr is None:
      return
    
    # check the subtree number of curr node  
    if curr.left is None or curr.right is None:
      # find the curr_parent's new subtree,
      # it must be one of the subtree of the curr
      new_subtree = None
      if curr.left is not None:
        new_subtree = curr.left
      else:
        new_subtree = curr.right
      
      if curr_parent is None:
        self.root = new_subtree
      else:
        if curr_parent.left == curr:
          curr_parent.left = new_subtree
        else:
          curr_parent.right = new_subtree
    else:
      # find the curr's inorder succ,  
      # use it's data to overwirte curr's data
      # use successor's right subtree to replace 
      # parent's subtree
      succ = curr.right
      succ_parent = None
      while succ.left is not None:
        succ_parent = succ
        succ = succ.left
      curr.data = succ.data

      if succ_parent is not None:
        succ_parent.left = succ.right
      else:
        curr.right = succ.right

  def search(self, data):
    curr = self.root
    while curr is not None and self.cmp(data, curr.data) != 0:
      if self.cmp(data, curr.data) < 0:
        curr = curr.left
      else:
        curr = curr.right
    if curr is not None:
      return data
    else:
      return None
    