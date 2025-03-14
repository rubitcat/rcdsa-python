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
    
    # check the subtree number of curr node  
    if curr.left is None or curr.right is None:
      # find the curr_parent's new subtree,
      # it must be one of the subtree of the curr
      new_subtree = curr.left if curr.left is not None else curr.right
      
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
      succ_parent = curr
      while succ.left is not None:
        succ_parent = succ
        succ = succ.left
      curr.data = succ.data

      if succ_parent == curr:
        succ_parent.right = succ.right
      else:
        succ_parent.left = succ.right

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
    