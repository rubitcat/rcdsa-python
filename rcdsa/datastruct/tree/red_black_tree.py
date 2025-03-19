from rcdsa.datastruct import BinarySearchTree 
from rcdsa.datastruct import LinkedStack
from enum import Enum

class RedBlackTree(BinarySearchTree):
  class Color(Enum):
    RED = 1
    BLACK = 2

  def __init__(self, cmp=lambda x, y: (x.__gt__(y)) - (x.__lt__(y))):
    super().__init__(cmp)

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
    new_subtree = node.right
    node.right = new_subtree.left
    new_subtree.left = node
    return new_subtree

  # reduce left subtree's height by 1 while keeping bst attr
  def _right_rotate(self, node):
    new_subtree = node.left
    node.left = new_subtree.right
    new_subtree.right = node
    return new_subtree

  def insert(self, data):
    if self.root is None:
      self.root = self.Node(data, color=self.Color.BLACK)
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

    if self.cmp(data, curr_parent.data) < 0:
      curr_parent.left = self.Node(data, color=self.Color.RED)
    elif self.cmp(data, curr_parent.data) > 0:
      curr_parent.right = self.Node(data, color=self.Color.RED)

    # rebalance tree
    while not stack.is_empty():
      curr = stack.top()
      stack.pop()
      if not stack.is_empty():
        curr_parent = stack.top()
        stack.pop()
      else:
        curr_parent = None
      curr_grandparent = stack.top() if not stack.is_empty() else None 

      # handle red-red violations
      red_violations = False  
      layout_state = 0 # bit 0 -> left, bit 1 -> right 
      curr_brother = None 
      if self._get_color(curr) == self.Color.RED:
        if self._get_color(curr.left) == self.Color.RED:
          red_violations = True
          layout_state &= 0xe
        if self._get_color(curr.right) == self.Color.RED:
          red_violations = True
          layout_state |= 0x1

        if red_violations and curr == curr_parent.left:
          layout_state &= 0xd
          curr_brother = curr_parent.right
        if red_violations and curr == curr_parent.right:
          layout_state |= 0x2
          curr_brother = curr_parent.left
      
      if red_violations:
        if self._get_color(curr_brother) == self.Color.RED:
          if curr_parent != self.root:
            self._set_color(curr_parent, self.Color.RED)
          self._set_color(curr, self.Color.BLACK)
          self._set_color(curr_brother, self.Color.BLACK)
          continue
        
        new_subtree = None
        if layout_state == 0:
          # LL case
          self._set_color(curr, self.Color.BLACK)
          self._set_color(curr_parent, self.Color.RED)
          new_subtree = self._right_rotate(curr_parent)
        elif layout_state == 1:
          # LR case
          self._set_color(curr.right, self.Color.BLACK)
          self._set_color(curr_parent, self.Color.RED)
          curr_parent.left = self._left_rotate(curr)
          new_subtree = self._right_rotate(curr_parent)
        elif layout_state == 2:
          # RL case
          self._set_color(curr.left, self.Color.BLACK)
          self._set_color(curr_parent, self.Color.RED)
          curr_parent.right = self._right_rotate(curr)
          new_subtree = self._left_rotate(curr_parent)
        elif layout_state == 3:
          # RR case
          self._set_color(curr, self.Color.BLACK)
          self._set_color(curr_parent, self.Color.RED)
          new_subtree = self._left_rotate(curr_parent)

        if curr_grandparent is None:
          self.root = new_subtree
        else:
          if curr_parent == curr_grandparent.left:
            curr_grandparent.left = new_subtree
          else:
            curr_grandparent.right = new_subtree

      # conflict fixed and quit
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
    
    
    curr_parent = stack.top() if not stack.is_empty() else None
    curr_succ = curr.left if curr.left is not None else curr.right
    black_violations = self._get_color(curr) == self._get_color(curr_succ) == self.Color.BLACK
    
    if not black_violations and curr_succ is not None:
      curr_succ.attrs["color"] = self.Color.BLACK

    stack.push(curr)
    while black_violations:
      doblk = stack.top()
      stack.pop()
      if not stack.is_empty():
        doblk_parent = stack.top()
        stack.pop()
      else:
        break
      doblk_grandparent = stack.top() if not stack.is_empty() else None

      layout_state = 0 # bit 0 -> left, bit 1 -> right 
      doblk_sibling = None
      if doblk == doblk_parent.left:
        layout_state |= 0x2
        doblk_sibling = doblk_parent.right
      else:
        layout_state &= 0xd 
        doblk_sibling = doblk_parent.left
      
      if doblk_sibling is None:
        stack.push(doblk_parent)
        continue
      
      # sibling red case
      if self._get_color(doblk_sibling) == self.Color.RED:
        self._set_color(doblk_sibling, self.Color.BLACK)
        self._set_color(doblk_parent, self.Color.RED)
        if layout_state >> 1 == 0:
          # left case
          doblk_grandparent_succ = self._right_rotate(doblk_parent)
          stack.push(doblk_grandparent_succ)
          stack.push(doblk_grandparent_succ.right)
          stack.push(doblk)
        else:
          # right case
          doblk_grandparent = self._left_rotate(doblk_parent)
          stack.push(doblk_grandparent_succ)
          stack.push(doblk_grandparent_succ.left)
          stack.push(doblk)

        if doblk_grandparent is None:
          self.root = doblk_grandparent_succ
        else:
          if doblk_grandparent.left == doblk_parent:
            doblk_grandparent.left = doblk_grandparent_succ
          else:
            doblk_grandparent.right = doblk_grandparent_succ
        continue
      
      # sibling black black case
      if self._get_color(doblk_sibling.left) == self.Color.BLACK \
        and self._get_color(doblk_sibling.right) == self.Color.BLACK:
        self._set_color(doblk_sibling, self.Color.RED)
        if self._get_color(doblk_parent) == self.Color.RED:
          self._set_color(doblk_parent, self.Color.BLACK)
          break
        else:
          stack.push(doblk_parent)
          continue

      # sibling black red case
      if layout_state >> 1  == 0:
        if self._get_color(doblk_sibling.left) == self.Color.BLACK:
          layout_state |= 0x1
        else:
          layout_state &= 0xe
      else:
        if self._get_color(doblk_sibling.right) == self.Color.BLACK:
          layout_state &= 0xe
        else:
          layout_state |= 0x1
        
      # LL case
      if layout_state == 0:
        self._set_color(doblk_sibling, self._get_color(doblk_parent))
        self._set_color(doblk_parent, self.Color.BLACK)
        self._set_color(doblk_sibling.left, self.Color.BLACK)
        doblk_grandparent_succ = self._right_rotate(doblk_parent)
      # LR case
      elif layout_state == 1:
        self._set_color(doblk_sibling, self.Color.RED)
        self._set_color(doblk_sibling.right, self.Color.BLACK)
        doblk_parent.left = self._left_rotate(doblk_parent.left)
        doblk_grandparent_succ = self._right_rotate(doblk_parent)
      # RL case
      elif layout_state == 2:
        self._set_color(doblk_sibling, self.Color.RED)
        self._set_color(doblk_sibling.left, self.Color.BLACK)
        doblk_parent.right = self._right_rotate(doblk_parent.right)
        doblk_grandparent_succ = self._left_rotate(doblk_parent)
      # RR case
      elif layout_state == 3:
        self._set_color(doblk_sibling, self._get_color(doblk_parent))
        self._set_color(doblk_parent, self.Color.BLACK)
        self._set_color(doblk_sibling.right, self.Color.BLACK)
        doblk_grandparent_succ = self._left_rotate(doblk_parent)
        
      if doblk_grandparent is None:
        self.root = doblk_grandparent_succ
      else:
        if doblk_grandparent.left == doblk_parent:
          doblk_grandparent.left = doblk_grandparent_succ
        else:
          doblk_grandparent.right = doblk_grandparent_succ
      
      break

    # delete the node
    if curr_parent is None:
      self.root = curr_succ
    else:
      if curr_parent.left == curr:
        curr_parent.left = curr_succ
      else:
        curr_parent.right = curr_succ
