from rcdsa.datastruct import HashMap
from rcdsa.datastruct import HashTable
from rcdsa.datastruct import HashSet
import time
import random



def test_hash_map_badkey():
  class BadKey:
    def __hash__(self):
      return 0 
  mp = HashMap()
  badkeys = [BadKey() for i in range(1000)]
  start_time = time.time()
  for i in range(len(badkeys)):
    if i == 13:
      mp.put(badkeys[i], "hello world")
      continue
    mp.put(badkeys[i], i)
  end_time = time.time()
  print("插入耗时: {:.2f}秒".format(end_time - start_time))

  start_time = time.time()
  assert mp.get(badkeys[13]) == "hello world"
  end_time = time.time()
  print("查询耗时: {:.2f}秒".format(end_time - start_time))

def test_hash_map_numberkey():
  num = 100*10000
  mp = HashMap(num)
  keys = random.sample([i for i in range(num)], num)

  start_time = time.time()
  for i in keys:
    if i == 1000:
      mp.put(keys[i], "hello world")
      continue
    mp.put(keys[i], i)
  end_time = time.time()
  print("插入耗时: {:.2f}秒".format(end_time - start_time))

  start_time = time.time()
  assert mp.get(keys[1000]) == "hello world"
  end_time = time.time()
  print("查询耗时: {:.2f}秒".format(end_time - start_time))

def test_hash_table():
  ht = HashTable()
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
    
  res = []
  ht.traversal(lambda x: res.append(x))
  for i in range(len(res)):
    assert res[i].row + res[i].col == res[i].value
  assert ht.size() == 100

def test_hash_set():
  size = 100
  hs = HashSet()
  for i in range(size):
    hs.put(i)
  assert hs.contains(5) == True

  hs.remove(0)
  hs.remove(2)
  hs.remove(1)
  hs.remove(4)
  hs.remove(3)
  hs.remove(5)
  res = []
  hs.traversal(lambda data: res.append(data))
  assert len(res) == size - 6
  assert hs.contains(5) == False