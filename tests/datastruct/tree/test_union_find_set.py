from rcdsa.datastruct import UnionFindSet


def test_union_find_set():
  ufs = UnionFindSet()
  for i in range(5):
    ufs.add(i)
  
  for i in range(5):
    assert ufs.find(i) == i

  ufs.union(1, 2)
  ufs.union(2, 3)
  
  assert ufs.is_united(1, 2) == True
  assert ufs.is_united(2, 3) == True
  assert ufs.is_united(1, 3) == True
  assert ufs.is_united(0, 3) == False
  assert ufs.is_united(4, 3) == False
  
  ufs.union(0,1)
  assert ufs.is_united(0, 3) == True

