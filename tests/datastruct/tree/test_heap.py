from rcdsa.datastruct import Heap


def test_heap():
  arr = [10, 20, 30, 40, 50, 15, 25, 35, 45]

  heap1 = Heap(10)
  for i in range(len(arr)):
    heap1.push(arr[i])
  
  assert heap1.top() == 50

  heap2 = Heap(10, cmp=lambda x, y: x < y)
  for i in range(len(arr)):
    heap2.push(arr[i])
  
  assert heap2.top() == 10


