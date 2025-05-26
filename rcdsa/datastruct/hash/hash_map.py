from rcdsa.datastruct import RedBlackTree
import time

class HashMap:
  class DataBin:
    def __init__(self, data=None, treeified=False):
      self.treeified = treeified
      self.data = data

  class Node:
    def __init__(self, data=None, next=None):
      self.data = data
      self.next = next

  class KeyPair:
    def __init__(self, key=None, value=None, hash=None):
      self.hash = hash
      self.key = key
      self.value = value

  # init hashmap
  def __init__(self, capacity=16, load_factor=0.75):
    self._load_factor = load_factor
    self._treeify_threshold = 8
    self._capacity = self._table_size_for(capacity)
    self._threshold = int(self._capacity * self._load_factor)
    self._max_capacity = 1 << 30
    self._size = 0
    self._table = [self.DataBin() for i in range(self._capacity)]

  # util for getting power of 2 size
  def _table_size_for(self, capacity):
    if capacity <= 0:
      return 1
    power = 1
    while power < capacity:
      power <<= 1
    return power

  # util for pre-processing key's hash value
  def _hash(self, key):
    h = key.__hash__()
    return h ^ (h >> 16) if h is not None else 0

  # treeify bin, convert linked list to rbt
  def _treeify(self, bin):
    if not bin.treeified:
      p = bin.data
      rbt = RedBlackTree(self._rbtcmp, self._rbttbo)
      while p is not None:
        rbt.insert(p.data)
        p = p.next
      bin.data = rbt

  # resize hash table, the size is the power of 2
  def _resize(self):
    old_captcity = self._capacity
    old_threshold = self._threshold
    old_table = self._table
    self._capacity = self._capacity << 1
    self._threshold = self._threshold << 1
    self._table = [self.DataBin() for i in range(self._capacity)]
    for i in range(old_captcity):
      bin = old_table[i]
      if bin.data is None:
        continue
      elif not bin.treeified:
        lo_head = None
        lo_tail = None
        hi_head = None
        hi_tail = None
        node = bin.data
        while node is not None:
          if (node.data.hash & old_captcity) == 0:
            # lower case
            if lo_tail is None:
              lo_head = node
            else:
              lo_tail.next = node
            lo_tail = node
          else:
            # higher case
            if hi_tail is None:
              hi_head = node
            else:
              hi_tail.next = node
            hi_tail = node
          node = node.next
        if lo_tail is not None:
          lo_tail.next = None
          self._table[i].data = lo_head
        if hi_tail is not None:
          hi_tail.next = None
          self._table[i + old_captcity].data = hi_head
      else:
        lo_head = None
        lo_tail = None
        lo_count = 0
        hi_head = None
        hi_tail = None
        hi_count = 0
        def _processor(pair):
          # using closure vas
          nonlocal lo_head
          nonlocal lo_tail
          nonlocal lo_count
          nonlocal hi_head
          nonlocal hi_tail
          nonlocal hi_count
          node = self.Node(pair)
          if (pair.hash & old_captcity) == 0:
            # lower case
            if lo_tail is None:
              lo_head = node
            else:
              lo_tail.next = node
            lo_tail = node
            lo_count += 1
          else:
            # higher case
            if hi_tail is None:
              hi_head = node
            else:
              hi_tail.next = node
            hi_tail = node
            hi_count += 1
        bin.data.traversal_preorder(_processor)

        if lo_tail is not None:
          new_bin = self._table[i]
          if hi_head is None:
            new_bin.data = bin.data
            new_bin.treeified = True
            return
          lo_tail.next = None
          new_bin.data = lo_head
          if lo_count > self._treeify_threshold:
            self._treeify(new_bin)
            new_bin.treeified = True
        if hi_tail is not None:
          new_bin = self._table[i + old_captcity]
          if lo_head is None:
            new_bin.data = bin.data
            new_bin.treeified = True
            return
          hi_tail.next = None
          new_bin.data = hi_head
          if hi_count > self._treeify_threshold:
            self._treeify(new_bin)
            new_bin.treeified = True

  # compare tow key
  def _rbtcmp(self, pair1, pair2):
    if pair1.hash > pair1.hash:
      return 1
    elif pair1.hash < pair1.hash:
      return -1
    elif pair1.hash == pair1.hash and (pair1.key is pair2.key or pair1.key == pair2.key):
      return 0
    else:
      if  pair1.key > pair2.key:
        return 1
      elif pair1.key < pair2.key :
        return -1

  # tie break order
  def _rbttbo(self, pair1, pair2):
    idp1 = id(pair1.key)
    idp2 = id(pair2.key)
    return 1 if idp1 > idp2 else -1

  def put(self, key, value):
    hash = self._hash(key)
    pair = self.KeyPair(key, value, hash)
    bin = self._table[(self._capacity-1) & pair.hash]
    pair_presented = None

    # insert
    if bin.data is None:
      # linked list insert
      bin.data = self.Node(pair)
      bin.treeified = False
    elif not bin.treeified: 
      # linked list insert
      node = bin.data
      count = 0
      while True:
        curr_pair = node.data
        if curr_pair.hash == hash and (curr_pair.key is key or curr_pair.key == key):
          pair_presented = curr_pair
          break
        if node.next is None:
          node.next = self.Node(pair)
          if count >= self._treeify_threshold-1:
            self._treeify(bin)
            bin.treeified = True
          break
        node = node.next
        count += 1
    else:
      # red-black tree insert
      pair_presented = bin.data.insert(pair)
    
    # overwrite
    if pair_presented is not None:
      pair_presented.value = value
    else:
      self._size += 1
      if self._size > self._threshold:
        self._resize()

  def get(self, key):
    hash = self._hash(key)
    bin = self._table[(self._capacity-1) & hash]
    if bin.data is None:
      return None
    elif not bin.treeified:
      node = bin.data
      while node is not None:
        curr_pair = node.data
        if curr_pair.hash == hash and (curr_pair.key is key or curr_pair.key == key):
          return curr_pair.value
        node = node.next
    else:
      pair = bin.data.search(self.KeyPair(key=key, hash=hash))
      return pair.value if pair is not None else None

  def remove(self, key):
    hash = self._hash(key)
    bin = self._table[(self._capacity-1) & hash]
    if bin.data is None:
      return
    elif not bin.treeified:
      node = bin.data
      node_parent = None
      while node is not None:
        curr_pair = node.data
        if curr_pair.hash == hash and (curr_pair.key is key or curr_pair.key == key):
          break
        node_parent = node
        node = node.next
      if node is None:
        return
      elif node_parent is None:
        bin.data = None
        return node.data.value
      else:
        node_parent.next = node.next
        return node.data.value
    else:
      deleted_pair = bin.data.delete(self.KeyPair(key=key, hash=hash))
      if bin.data.is_empty():
        del bin.data
        bin.treeified = False
      if deleted_pair is not None:
        self._size -= 1
        return deleted_pair.value


