from rcdsa.datastruct import HashSet

class LinkedHashSet(HashSet):

  class EntryEx(HashSet.Entry):
    def __init__(self, data=None, before=None, after=None):
      super().__init__(data)
      self.before = before
      self.after = after

  def __init__(self):
    super().__init__()
    self.head = None
    self.tail = None
  
  def _new_entry(self, data=None):
    return self.EntryEx(data)
  
  def _after_entry_insert(self, entry):
    if self.tail is None:
      self.head = entry
    else:
      self.tail.after = entry
      entry.before = self.tail
    self.tail = entry

  def _after_entry_remove(self, entry):
    if entry.before is None:
      self.head = entry.after 
    else:
      entry.before.after = entry.after
    if entry.after is None:
      self.tail = entry.before
    else:
      entry.after.before = entry.before
    entry.before = None
    entry.after = None

  def traversal(self, callback):
    if self.head is not None:
      curr = self.head
      while curr is not None:
        callback(curr.data)
        curr = curr.after