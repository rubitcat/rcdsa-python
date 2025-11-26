from rcdsa.datastruct import LinkedHashMap
from rcdsa.datastruct import LinkedHashSet
from rcdsa.datastruct import LinkedHashTable

def test_linked_hash_map():
  size = 10000
  lmp = LinkedHashMap()
  for i in range(size):
    lmp.put(i, i)
  keys = lmp.keys()
  values = lmp.values()
  assert keys == [i for i in range(size)]
  assert values == [i for i in range(size)]


def test_linked_hash_set():
  size = 100
  lhs = LinkedHashSet()
  res = []
  for i in range(size):
    lhs.put(i)
  lhs.traversal(lambda data: res.append(data))
  assert lhs.contains(4) == True 
  assert res == [i for i in range(size)]

  res.clear()
  lhs.remove(0)
  lhs.remove(2)
  lhs.remove(1)
  lhs.remove(3)
  lhs.remove(4)
  lhs.remove(5)
  lhs.traversal(lambda data: res.append(data))
  assert len(res) == size - 6
  assert lhs.contains(4) == False
  assert res == [i for i in range(6, size)]


def test_linked_hash_table():
  ht = LinkedHashTable()
  for i in range(10):
    for j in range(10):
      ht.put(i,j, i+j)
  
  for i in range(10):
    for j in range(10):
      assert ht.get(i,j) == i+j
  
  rows = ht.get_rows()
  cols = ht.get_cols()

  for i in range(10):
    assert i in rows
    assert i in cols