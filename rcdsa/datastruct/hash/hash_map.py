from rcdsa.datastruct import RedBlackTree

class HashMap:
  class DataBin:
    def __init__(self, data=None):
      self.data = data

  class TreeDataBin(DataBin):
    def __init__(self, data=None):
      super().__init__(data)

  class Entry:
    def __init__(self, key=None, value=None, hash=None, next=None):
      self.hash = hash
      self.key = key
      self.value = value
      self.next = next 

  def __init__(self, capacity=16, load_factor=0.75):
    self._load_factor = load_factor
    self._treeify_threshold = 8
    self._capacity = self._table_size_for(capacity)
    self._threshold = int(self._capacity * self._load_factor)
    self._max_capacity = 1 << 30
    self._size = 0
    self._table = None

  def _table_size_for(self, capacity):
    """
    util for getting power of 2 size
    """
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

  def _new_data_bin(self, data=None):
    return self.DataBin(data)

  def _new_tree_data_bin(self, data):
    return self.TreeDataBin(data)

  def _new_entry(self, key=None, value=None, hash=None, next=None):
    """
    hook for entry creation, this method will be invoke when there need
    to create an entry in "put" method
    """
    return self.Entry(key, value, hash, next)

  def _after_entry_insert(self, entry):
    """
    hook for inserted entry, this method will be invoke when an entry 
    is inserted in "put" method
    """
    pass

  def _after_entry_remove(self, entry):
    """
    hook for deleted entry, this method will be invoke when an entry 
    is removed in "remove" method.
    """
    pass

  def _treeify(self, table, index):
    """
    treeify bin, convert linked list to rbt
    """
    if not isinstance(table[index], self.TreeDataBin):
      curr = table[index].data
      rbt = RedBlackTree(self._rbtcmp, self._rbttbo)
      table[index] = self._new_tree_data_bin(rbt)
      while curr is not None:
        rbt.insert(curr)
        curr = curr.next

  def _move_linked_list(self, old_table, old_index, old_capacity, new_table):
    lo_head = None
    lo_tail = None
    hi_head = None
    hi_tail = None
    curr_entry = old_table[old_index].data
    while curr_entry is not None:
      if (curr_entry.hash & old_capacity) == 0:
        # lower case
        if lo_tail is None:
          lo_head = curr_entry
        else:
          lo_tail.next = curr_entry
        lo_tail = curr_entry
      else:
        # higher case
        if hi_tail is None:
          hi_head = curr_entry
        else:
          hi_tail.next = curr_entry
        hi_tail = curr_entry
      curr_entry = curr_entry.next
    if lo_tail is not None:
      lo_tail.next = None
      new_table[old_index].data = lo_head
    if hi_tail is not None:
      hi_tail.next = None
      new_table[old_index + old_capacity].data = hi_head

  def _move_tree(self, old_table, old_index, old_capacity, new_table):
    lo_head = None
    lo_tail = None
    lo_count = 0
    hi_head = None
    hi_tail = None
    hi_count = 0
    def _processor(entry):
      # using closure vas
      nonlocal lo_head
      nonlocal lo_tail
      nonlocal lo_count
      nonlocal hi_head
      nonlocal hi_tail
      nonlocal hi_count
      if (entry.hash & old_capacity) == 0:
        # lower case
        if lo_tail is None:
          lo_head = entry
        else:
          lo_tail.next = entry
        lo_tail = entry
        lo_count += 1
      else:
        # higher case
        if hi_tail is None:
          hi_head = entry
        else:
          hi_tail.next = entry
        hi_tail = entry
        hi_count += 1
    old_table[old_index].data.traversal_preorder(_processor)

    if lo_tail is not None:
      if hi_head is None:
        new_table[old_index] = old_table[old_index]
        return
      lo_tail.next = None
      new_table[old_index].data = lo_head
      if lo_count > self._treeify_threshold:
        self._treeify(new_table, old_index)
    if hi_tail is not None:
      if lo_head is None:
        new_table[old_index + old_capacity].data = old_table[old_index].data
        return
      hi_tail.next = None
      new_table[old_index + old_capacity].data = hi_head
      if hi_count > self._treeify_threshold:
        self._treeify(new_table, old_index + old_capacity)

  def _resize(self):
    """
    resize hash table, the size is the power of 2
    """
    if self._table is None:
      self._table = [self.DataBin() for i in range(self._capacity)]
      return
    old_capacity = self._capacity
    old_threshold = self._threshold
    old_table = self._table
    self._capacity = self._capacity << 1
    self._threshold = self._threshold << 1
    self._table = [self.DataBin() for i in range(self._capacity)]
    for i in range(old_capacity):
      bin = old_table[i]
      if bin.data is None:
        continue
      elif isinstance(bin, self.TreeDataBin):
        self._move_tree(old_table, i, old_capacity, self._table)
      else:
        self._move_linked_list(old_table, i, old_capacity, self._table)

  def _rbtcmp(self, entry1, entry2):
    """
    compare tow entry
    """
    if entry1.hash > entry1.hash:
      return 1
    elif entry1.hash < entry1.hash:
      return -1
    elif entry1.hash == entry1.hash and (entry1.key is entry2.key or entry1.key == entry2.key):
      return 0
    else:
      if  entry1.key > entry2.key:
        return 1
      elif entry1.key < entry2.key :
        return -1

  def _rbttbo(self, entry1, entry2):
    """
    tie break order for entries 
    """
    ide1 = id(entry1.key)
    ide2 = id(entry2.key)
    return 1 if ide1 > ide2 else -1

  def traversal(self, callback):
    for bin in self._table:
      if bin.data is None:
        continue
      elif isinstance(bin, self.TreeDataBin):
        bin.data.traversal_preorder(lambda entry: callback(entry))
      else:
        curr_entry = bin.data
        while curr_entry is not None:
          callback(curr_entry)
          curr_entry = curr_entry.next

  def size(self):
    return self._size

  def put(self, key, value, overwrite=True) -> int:
    if self._table is None:
      self._resize()
    hash = self._hash(key)
    entry = self._new_entry(key, value, hash)
    bin = self._table[(self._capacity-1) & entry.hash]
    entry_presented = None

    if bin.data is None:
      bin.data = entry
    elif isinstance(bin, self.TreeDataBin):
      res = bin.data.insert(entry)
      entry_presented = res if res is not entry else None
    else:
      curr_entry = bin.data
      count = 0
      while True:
        if curr_entry.hash == hash and (curr_entry.key is key or curr_entry.key == key):
          entry_presented = curr_entry
          break
        if curr_entry.next is None:
          curr_entry.next = entry
          if count >= self._treeify_threshold-1:
            self._treeify(self._table, (self._capacity-1) & entry.hash)
          break
        curr_entry = curr_entry.next
        count += 1
    
    # overwrite
    if entry_presented is not None:
      if overwrite:
        old_value = entry_presented.value
        entry_presented.value = value
        return old_value
      return
    else:
      self._size += 1
      self._after_entry_insert(entry)
      if self._size > self._threshold:
        self._resize()
      return value

  def _get_entry(self, key):
    if self._table is None:
      return
    hash = self._hash(key)
    bin = self._table[(self._capacity-1) & hash]
    if bin.data is None:
      return None
    elif isinstance(bin, self.TreeDataBin):
      return bin.data.search(self.Entry(key=key, hash=hash))
    else:
      curr_entry = bin.data
      while curr_entry is not None:
        if curr_entry.hash == hash and (curr_entry.key is key or curr_entry.key == key):
          return curr_entry
        curr_entry = curr_entry.next

  def get(self, key):
    entry = self._get_entry(key)
    return entry.value if entry is not None else None

  def contains(self, key):
    entry = self._get_entry(key)
    return entry is not None

  def first(self):
    for bin in self._table:
      if bin.data is None:
        continue
      elif isinstance(bin, self.TreeDataBin):
        return bin.data.root().data
      else:
        return bin.data
    
  def remove(self, key):
    if self._table is None:
      return
    hash = self._hash(key)
    bin = self._table[(self._capacity-1) & hash]
    deleted_entry = None
    if bin.data is None:
      pass
    elif isinstance(bin, self.TreeDataBin):
      deleted_entry = bin.data.delete(self.Entry(key=key, hash=hash))
      if bin.data.is_empty():
        self._table[(self._capacity-1) & hash] = self.DataBin()
        del bin.data
    else:
      curr_entry = bin.data
      curr_entry_parent = None
      while curr_entry is not None:
        if curr_entry.hash == hash and (curr_entry.key is key or curr_entry.key == key):
          break
        curr_entry_parent = curr_entry
        curr_entry = curr_entry.next
      if curr_entry is not None:
        deleted_entry = curr_entry
        if curr_entry_parent is None:
          bin.data = curr_entry.next
        else:
          curr_entry_parent.next = curr_entry.next

    if deleted_entry is not None:
      self._size -= 1
      self._after_entry_remove(deleted_entry)
      return deleted_entry

  def clear(self):
    pass

  def keys(self) -> list:
    if self._size == 0:
      return []
    res = [None] * self._size
    pt = 0
    def _processor(entry):
      nonlocal res
      nonlocal pt
      res[pt] = entry.key
      pt += 1 
    self.traversal(_processor)
    return res

  def values(self) -> list:
    if self._size == 0:
      return []
    res = [None] * self._size
    pt = 0
    def _processor(entry):
      nonlocal res
      nonlocal pt
      res[pt] = entry.value
      pt += 1 
    self.traversal(_processor)
    return res
  
  def entries(self) -> list:
    if self._size == 0:
      return []
    res = [None] * self._size
    pt = 0
    def _processor(entry):
      nonlocal res
      nonlocal pt
      res[pt] = entry
      pt += 1 
    self.traversal(_processor)
    return res
