from rcdsa.datastruct import BinarySearchTree
from rcdsa.datastruct import LinkedStack

class AVLTree(BinarySearchTree):
  
  def __init__(self, cmp=BinarySearchTree.default_cmp, tbo=BinarySearchTree.default_tie_break_order):
    super().__init__(cmp, tbo)
  
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

  # util for reduce right subtree's height by 1 while keeping bst attr
  def _left_rotate(self, node):
    new_tree = node.right
    node.right = new_tree.left
    new_tree.left = node
    new_tree.parent = node.parent
    node.parent = new_tree
    if node.right is not None:
      node.right.parent = node
    self._set_height(
      node, 
      1 + max(self._get_height(node.left), self._get_height(node.right))
    )
    self._set_height(
      new_tree, 
      1 + max(self._get_height(new_tree.left), self._get_height(new_tree.right))
    )
    return new_tree

  # util for reduce left subtree's height by 1 while keeping bst attr
  def _right_rotate(self, node):
    new_tree = node.left
    node.left = new_tree.right
    new_tree.right = node
    new_tree.parent = node.parent
    node.parent = new_tree
    if node.left is not None:
      node.left.parent = node
    self._set_height(
      node, 
      1 + max(self._get_height(node.left), self._get_height(node.right))
    )
    self._set_height(
      new_tree, 
      1 + max(self._get_height(new_tree.left), self._get_height(new_tree.right))
    )
    return new_tree

  def _insert(self, data):
    node = super()._insert(data)
    self._set_height(node, 1)

    # rebalance tree
    curr = node
    while curr.parent is not None:
      curr = curr.parent
      curr_parent = curr.parent if curr.parent is not None else None
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
        self._transplant(curr_parent, curr, new_subtree)
        break

    return node

  def _delete(self, data):
    curr = super()._delete(data)

    # rebalance tree
    while curr.parent is not None:
      curr = curr.parent
      curr_parent = curr.parent if curr.parent is not None else None
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