from rcdsa.algorithm.sort import default_cmp
from rcdsa.datastruct import Heap

"""
Heap Sort
:param arr:
"""
def heap_sort(arr, cmp=default_cmp):
  n = len(arr)
  for i in range(n//2, -1, -1):
    Heap.heapify(arr, n, i, lambda x,y: -cmp(x, y))
  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    Heap.heapify(arr, i, 0, lambda x,y: -cmp(x, y))