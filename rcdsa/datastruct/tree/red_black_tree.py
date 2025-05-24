from rcdsa.datastruct import BinarySearchTree 
from rcdsa.datastruct import LinkedStack
from enum import Enum

class RedBlackTree(BinarySearchTree):
  class Color(Enum):
    RED = 1
    BLACK = 2

  def __init__(self, cmp=BinarySearchTree.default_cmp, tbo=BinarySearchTree.default_tie_break_order):
    super().__init__(cmp, tbo)

  # util for getting node color
  def _get_color(self, node):
    if node is None:
      return self.Color.BLACK
    return node.attrs.get("color")

  # util for setting node color
  def _set_color(self, node, color):
    if node is None:
      return
    node.attrs["color"] = color

  # reduce right subtree's height by 1 while keeping bst attr
  def _left_rotate(self, node):
    new_tree = node.right
    node.right = new_tree.left
    new_tree.left = node
    new_tree.parent = node.parent
    node.parent = new_tree
    if node.right is not None:
      node.right.parent = node
    return new_tree

  # reduce left subtree's height by 1 while keeping bst attr
  def _right_rotate(self, node):
    new_tree = node.left
    node.left = new_tree.right
    new_tree.right = node
    new_tree.parent = node.parent
    node.parent = new_tree
    if node.left is not None:
      node.left.parent = node
    return new_tree

  def _insert(self, data):
    node = super()._insert(data)
    if self.root == node:
      self._set_color(node, self.Color.BLACK)
    else: 
      self._set_color(node, self.Color.RED)

    # rebalance tree
    curr = node
    curr_parent = curr.parent if curr.parent is not None else None
    red_violations = self._get_color(curr_parent) == self.Color.RED
    if red_violations:
      curr = curr_parent # start from node which is newly inserted
      while curr is not None and curr.parent is not None:
        curr_parent = curr.parent
        curr_grandparent = curr_parent.parent if curr_parent.parent is not None else None 
        curr_parent_succ = None

        # detect curr layout
        layout_state = 0 # bit 0 -> left, bit 1 -> right 
        curr_sibling = None 
        if curr == curr_parent.left:
          layout_state &= 0xd
          curr_sibling = curr_parent.right
        if curr == curr_parent.right:
          layout_state |= 0x2
          curr_sibling = curr_parent.left
        
        # sibling red case
        if self._get_color(curr_sibling) == self.Color.RED:
          self._set_color(curr, self.Color.BLACK)
          self._set_color(curr_sibling, self.Color.BLACK)          
          if curr_parent != self.root:
            self._set_color(curr_parent, self.Color.RED)
            if self._get_color(curr_grandparent) == self.Color.RED:
              curr = curr_grandparent
              continue
          break

        # sibling black case
        if self._get_color(curr.left) == self.Color.RED:
          layout_state &= 0xe
        if self._get_color(curr.right) == self.Color.RED:
          layout_state |= 0x1

        if layout_state == 0:
          # LL case
          self._set_color(curr, self.Color.BLACK)
          self._set_color(curr_parent, self.Color.RED)
          curr_parent_succ = self._right_rotate(curr_parent)
        elif layout_state == 1:
          # LR case
          self._set_color(curr.right, self.Color.BLACK)
          self._set_color(curr_parent, self.Color.RED)
          curr_parent.left = self._left_rotate(curr)
          curr_parent_succ = self._right_rotate(curr_parent)
        elif layout_state == 2:
          # RL case
          self._set_color(curr.left, self.Color.BLACK)
          self._set_color(curr_parent, self.Color.RED)
          curr_parent.right = self._right_rotate(curr)
          curr_parent_succ = self._left_rotate(curr_parent)
        elif layout_state == 3:
          # RR case
          self._set_color(curr, self.Color.BLACK)
          self._set_color(curr_parent, self.Color.RED)
          curr_parent_succ = self._left_rotate(curr_parent)

        self._transplant(curr_grandparent, curr_parent, curr_parent_succ)
        break

  def _delete(self, data):
    if self.root is None:
      return
    node = self._search(data, self.root)
    if node is None:
      return
    target = node
    if target.left is not None and target.right is not None:
      temp = target
      target = target.right
      while target.left is not None:
        target = target.left
      (temp.data, target.data) = (target.data, temp.data)
    
    # rebalance tree, the target node will be deleted later 
    target_succ = target.left if target.left is not None else target.right
    black_violations = self._get_color(target) == self._get_color(target_succ) == self.Color.BLACK
    if not black_violations:
      # simple case
      if target_succ is not None:
        self._set_color(target_succ, self.Color.BLACK)
    else:
      # double black case
      curr = target # start from node which will be delete soon
      while curr is not None and curr.parent is not None:
        curr_parent = curr.parent
        curr_grandparent = curr_parent.parent if curr_parent.parent is not None else None
        curr_parent_succ = None

        # detect double black layout
        layout_state = 0 # bit 0 -> left, bit 1 -> right 
        curr_sibling = None
        if curr == curr_parent.left:
          layout_state |= 0x2
          curr_sibling = curr_parent.right
        else:
          layout_state &= 0xd 
          curr_sibling = curr_parent.left
        
        if curr_sibling is None:
          curr = curr_parent
          continue
        
        # sibling red case
        if self._get_color(curr_sibling) == self.Color.RED:
          self._set_color(curr_sibling, self.Color.BLACK)
          self._set_color(curr_parent, self.Color.RED)
          if layout_state >> 1 == 0:
            # left case
            curr_parent_succ = self._right_rotate(curr_parent)
          else:
            # right case
            curr_parent_succ = self._left_rotate(curr_parent)
          self._transplant(curr_grandparent, curr_parent, curr_parent_succ)
          continue
        
        # sibling black black case
        if self._get_color(curr_sibling.left) == self.Color.BLACK \
          and self._get_color(curr_sibling.right) == self.Color.BLACK:
          self._set_color(curr_sibling, self.Color.RED)
          if self._get_color(curr_parent) == self.Color.RED:
            self._set_color(curr_parent, self.Color.BLACK)
            break
          else:
            curr = curr_parent
            continue

        # sibling black red case
        if layout_state >> 1  == 0:
          if self._get_color(curr_sibling.left) == self.Color.BLACK:
            layout_state |= 0x1
          else:
            layout_state &= 0xe
        else:
          if self._get_color(curr_sibling.right) == self.Color.BLACK:
            layout_state &= 0xe
          else:
            layout_state |= 0x1
          
        if layout_state == 0:
          # LL case
          self._set_color(curr_sibling, self._get_color(curr_parent))
          self._set_color(curr_parent, self.Color.BLACK)
          self._set_color(curr_sibling.left, self.Color.BLACK)
          curr_parent_succ = self._right_rotate(curr_parent)
        elif layout_state == 1:
          # LR case
          self._set_color(curr_sibling, self.Color.RED)
          self._set_color(curr_sibling.right, self.Color.BLACK)
          curr_parent.left = self._left_rotate(curr_parent.left)
          curr_parent_succ = self._right_rotate(curr_parent)
        elif layout_state == 2:
          # RL case
          self._set_color(curr_sibling, self.Color.RED)
          self._set_color(curr_sibling.left, self.Color.BLACK)
          curr_parent.right = self._right_rotate(curr_parent.right)
          curr_parent_succ = self._left_rotate(curr_parent)
        elif layout_state == 3:
          # RR case
          self._set_color(curr_sibling, self._get_color(curr_parent))
          self._set_color(curr_parent, self.Color.BLACK)
          self._set_color(curr_sibling.right, self.Color.BLACK)
          curr_parent_succ = self._left_rotate(curr_parent)
        
        self._transplant(curr_grandparent, curr_parent, curr_parent_succ)
        break

    # delete the node
    self._transplant(
      target.parent, 
      target, 
      target.left if target.left is not None else target.right
    )
    return target
