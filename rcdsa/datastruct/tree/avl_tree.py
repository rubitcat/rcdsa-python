from rcdsa.datastruct import BinarySearchTree
from rcdsa.datastruct import LinkedStack

class AVLTree(BinarySearchTree):
  
  def __init__(self, cmp=lambda x, y: (x.__gt__(y)) - (x.__lt__(y))):
    super().__init__(cmp)
  
  # util for getting tree height from attribute
  def _get_height(self, node):
    if node is None:
      return 0
    return node.attrs.get("height")

  # util for getting tree balance factor
  def _get_balance(self, node):
    if node is None:
      return 0
    return self._get_height(node.left) - self._get_height(node.right)

  # reduce right subtree's height by 1 while keeping bst attr
  def _left_rotate(self, node):
    new_subtree = node.right
    node.right = new_subtree.left
    new_subtree.left = node
    node.attrs["height"] = 1 + \
      max(self._get_height(node.left), self._get_height(node.right))
    new_subtree.attrs["height"] = 1 + \
      max(self._get_height(new_subtree.left), self._get_height(new_subtree.right))
    return new_subtree

  # reduce left subtree's height by 1 while keeping bst attr
  def _right_rotate(self, node):
    new_subtree = node.left
    node.left = new_subtree.right
    new_subtree.right = node
    node.attrs["height"] = 1 + \
      max(self._get_height(node.left), self._get_height(node.right))
    new_subtree.attrs["height"] = 1 + \
      max(self._get_height(new_subtree.left), self._get_height(new_subtree.right))
    return new_subtree

  def insert(self, data):
    if self.root is None:
      self.root = self.Node(data, height=1)
      return

    # find the leaf node to be inserted
    curr = self.root
    stack = LinkedStack()
    while curr is not None:
      if self.cmp(data, curr.data) < 0 :
        stack.push(curr)
        curr = curr.left
      elif self.cmp(data, curr.data) > 0:
        stack.push(curr)
        curr = curr.right 
      else:
        return
    curr_parent = stack.top()

    # insert data
    if self.cmp(data, curr_parent.data) < 0:
      curr_parent.left = self.Node(data, height=1)
    elif self.cmp(data, curr_parent.data) > 0:
      curr_parent.right = self.Node(data, height=1)

    # rebalance tree
    while not stack.is_empty():
      curr = stack.top()
      stack.pop()
      curr_parent = stack.top() if not stack.is_empty() else None
      curr.attrs['height'] = 1 + \
        max(self._get_height(curr.left), self._get_height(curr.right))
      curr_balance = self._get_balance(curr)

      new_subtree = None
      if curr_balance > 1 and self.cmp(data, curr.left.data) < 0:
        new_subtree = self._right_rotate(curr)
      elif curr_balance > 1 and self.cmp(data, curr.left.data) > 0:
        curr.left = self._left_rotate(curr.left)
        new_subtree = self._right_rotate(curr)
      elif curr_balance < -1 and self.cmp(data, curr.right.data) > 0:
        new_subtree = self._left_rotate(curr)
      elif curr_balance < -1 and self.cmp(data, curr.right.data) < 0:
        curr.right = self._right_rotate(curr.right)
        new_subtree = self._left_rotate(curr)

      if new_subtree is not None:
        if curr_parent is None:
          self.root = new_subtree
        else:
          if curr_parent.left == curr:
            curr_parent.left = new_subtree
          else:
            curr_parent.right = new_subtree
        break

  def delete(self, data):
    if self.root is None:
      return
    
    # find the node we want to delete
    curr = self.root
    stack = LinkedStack()
    while curr is not None:
      if self.cmp(data, curr.data) < 0 :
        stack.push(curr)
        curr = curr.left
      elif self.cmp(data, curr.data) > 0:
        stack.push(curr)
        curr = curr.right
      else:
        break
    if curr is None:
      return
    curr_parent = stack.top() if not stack.is_empty() else None

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
      stack.push(curr)
      while succ.left is not None:
        stack.push(succ)
        succ = succ.left
      succ_parent = stack.top()
      curr.data = succ.data

      if succ_parent == curr:
        succ_parent.right = succ.right
      else:
        succ_parent.left = succ.right
    
    # rebalance tree
    while not stack.is_empty():
      curr = stack.top()
      stack.pop()
      curr_parent = stack.top() if not stack.is_empty() else None
      curr.attrs['height'] = 1 + \
        max(self._get_height(curr.left), self._get_height(curr.right))
      curr_balance = self._get_balance(curr)

      new_subtree = None
      if curr_balance > 1 and self._get_balance(curr.left) >= 0:
        new_subtree = self._right_rotate(curr)
      elif curr_balance > 1 and self._get_balance(curr.left) < 0:
        curr.left = self._left_rotate(curr.left)
        new_subtree = self._right_rotate(curr)
      elif curr_balance < -1 and self._get_balance(curr.right) <= 0:
        new_subtree = self._left_rotate(curr)
      elif curr_balance < -1 and self._get_balance(curr.right) > 0:
        curr.right = self._right_rotate(curr.right)
        new_subtree = self._left_rotate(curr)

      if new_subtree is not None:
        if curr_parent is None:
          self.root = new_subtree
        else:
          if curr_parent.left == curr:
            curr_parent.left = new_subtree
          else:
            curr_parent.right = new_subtree
        # we can't break here, all the ancestors should be fixed.