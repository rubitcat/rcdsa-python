from rcdsa.datastruct import HashSet
from rcdsa.datastruct import LinkedHashMap

class LinkedHashSet(HashSet):


  def __init__(self):
    super().__init__()

  def _new_map(self):
    return LinkedHashMap()