from rcdsa.datastruct import BinaryTree

class BinarySearchTree(BinaryTree):
  @staticmethod
  def default_cmp(x, y):
    hx = x.__hash__()
    hy = y.__hash__()
    if hx > hy:
      return 1
    elif hx < hy:
      return -1
    elif x is y or x == y:
      return 0
    else:
      raise RuntimeError((x,y))  
    
  @staticmethod
  def default_tie_break_order(x, y):
    hx = hash(x)
    hy = hash(y)
    return 1 if hx > hy else -1

  def __init__(self, cmp=default_cmp, tbo=default_tie_break_order):
    super().__init__()
    self.cmp = cmp
    self.tbo = tbo

  # util for replace u with v
  def _transplant(self, p, u, v):
    if v is not None:
      v.parent = p
    if p is None:
      self.root = v
    elif u == p.left:
      p.left = v
    elif u == p.right:
      p.right = v

  # insert data
  def _insert(self, data):
    if self.root is None:
      self.root = self.Node(data)
      return self.root
    # find the leaf node to be inserted
    curr = self.root
    curr_parent = None
    direction = None
    searched = False
    node_presented = None
    while curr is not None:
      try:
        direction = self.cmp(data, curr.data) 
        if direction > 0:
          curr_parent = curr
          curr = curr.right 
        elif direction < 0 :
          curr_parent = curr
          curr = curr.left
        else:
          node_presented = curr
          break
      except Exception:
        if not searched:
          searched = True
          node = self._search(data, curr)
          if node is not None:
            node_presented = node
            break
        # tie break order
        direction = self.tbo(data, curr.data)
        if direction > 0:
          curr_parent = curr
          curr = curr.right 
        elif direction < 0 :
          curr_parent = curr
          curr = curr.left
    
    if node_presented is not None:
      raise Exception(node_presented)

    if direction < 0:
      curr_parent.left = self.Node(data, parent=curr_parent)
      return curr_parent.left
    elif direction > 0:
      curr_parent.right = self.Node(data, parent=curr_parent)
      return curr_parent.right
    
  # delete data
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
    
    # delete the node
    self._transplant(
      target.parent, 
      target, 
      target.left if target.left is not None else target.right
    )
    return target

  def _search(self, data, root):
    if root is None:
      return None
    while root is not None:
      try:
        if self.cmp(data, root.data) < 0:
          root = root.left
        elif self.cmp(data, root.data) > 0:
          root = root.right
        else:
          return root
      except Exception:
        node = self._search(data, root.left)
        if node is not None:
          return node
        root = root.right
    return None

  def is_empty(self):
    return True if self.root is None else False 

  def insert(self, data, overwrite=True):
    try:
      self._insert(data)
      return data
    except Exception as e:
      if overwrite:
        node = e.args[0]
        old_data = node.data
        node.data = data
        return old_data
    
  def delete(self, data):
    node = self._delete(data)
    return node.data if node is not None else None

  def search(self, data):
    if self.root is None:
      return None
    node = self._search(data, self.root)
    return node.data if node is not None else None
  
  def contains(self, data):
    if self.root is None:
      return False
    node = self._search(data, self.root)
    return True if node is not None else False

    