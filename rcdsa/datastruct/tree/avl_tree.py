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

  # util for setting tree height from attribute
  def _set_height(self, node, height):
    if node is None:
      return
    node.attrs["height"] = height

  # util for getting tree balance factor
  def _get_balance(self, node):
    if node is None:
      return 0
    return self._get_height(node.left) - self._get_height(node.right)

  # reduce right subtree's height by 1 while keeping bst attr
  def _left_rotate(self, node):
    new_tree = node.right
    node.right = new_tree.left
    new_tree.left = node
    self._set_height(
      node, 
      1 + max(self._get_height(node.left), self._get_height(node.right))
    )
    self._set_height(
      new_tree, 
      1 + max(self._get_height(new_tree.left), self._get_height(new_tree.right))
    )
    return new_tree

  # reduce left subtree's height by 1 while keeping bst attr
  def _right_rotate(self, node):
    new_tree = node.left
    node.left = new_tree.right
    new_tree.right = node
    self._set_height(
      node, 
      1 + max(self._get_height(node.left), self._get_height(node.right))
    )
    self._set_height(
      new_tree, 
      1 + max(self._get_height(new_tree.left), self._get_height(new_tree.right))
    )
    return new_tree

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
      self._set_height(
        curr, 
        1 + max(self._get_height(curr.left), self._get_height(curr.right))
      )
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

    if curr.left is not None and curr.right is not None:
      temp = curr
      stack.push(curr)
      curr = curr.right
      while curr.left is not None:
        stack.push(curr)
        curr = curr.left
      temp.data = curr.data
    
    # delete the node
    curr_parent = stack.top() if not stack.is_empty() else None
    curr_succ = curr.left if curr.left is not None else curr.right
    self._transplant(curr_parent, curr, curr_succ)
    
    # rebalance tree
    while not stack.is_empty():
      curr = stack.top()
      stack.pop()
      curr_parent = stack.top() if not stack.is_empty() else None
      self._set_height(
        curr, 
        1 + max(self._get_height(curr.left), self._get_height(curr.right))
      )
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
        self._transplant(curr_parent, curr, new_subtree)
        # we can't break here, all the ancestors should be fixed.