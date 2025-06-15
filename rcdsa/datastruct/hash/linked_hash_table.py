from rcdsa.datastruct import LinkedHashMap
from rcdsa.datastruct import LinkedHashSet
from rcdsa.datastruct import HashTable

class LinkedHashTable(HashTable):
  def __init__(self):
    super().__init__()
  
  def _new_map(self):
    return LinkedHashMap()

  def _new_set(self):
    return LinkedHashSet()