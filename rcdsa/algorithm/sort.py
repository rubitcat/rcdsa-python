from rcdsa.datastruct import LinkedStack
from rcdsa.datastruct import Heap

def _cmp(x, y):
  if x > y:
    return 1
  elif x < y:
    return -1
  else:
    return 0

"""
Selection Sort
:param arr:
"""
def selection_sort(arr, cmp=_cmp):
  for i in range(len(arr)-1):
    mxx = i
    for j in range(i+1, len(arr)):
      if cmp(arr[mxx], arr[j]) > 0:
        mxx = j
    if mxx != i:
      arr[i], arr[mxx] = arr[mxx], arr[i]

"""
Bubble Sort
:param arr:
"""
def bubble_sort(arr, cmp=_cmp):
  n = len(arr)
  for i in range(n):
    swapped = False
    for j in range(n-i-1):
      if cmp(arr[j], arr[j+1]) > 0:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
    if (swapped is False):
      break
    
"""

Insertion Sort
:param arr:
"""
def insertion_sort(arr, cmp=_cmp):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and cmp(arr[j], key) > 0:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

"""
Quick Sort
:param arr:
"""
def quick_sort(arr, start=None, end=None, cmp=_cmp):
  class Param:
    def __init__(self, low, high):
      self.low = low
      self.high = high

  if start is None or end is None:
    start = 0
    end = len(arr) - 1

  stack = LinkedStack()
  stack.push(Param(start, end))
  
  while not stack.is_empty():
    param = stack.top()
    stack.pop()

    pivot = arr[param.high]
    i = param.low - 1
    for j in range(param.low, param.high):
      if cmp(pivot, arr[j]) > 0:
        i = i + 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[param.high] = arr[param.high], arr[i + 1]

    if param.low < i+1-1:
      stack.push(Param(param.low, i+1-1))
    if i+1+1 < param.high:
      stack.push(Param(i+1+1, param.high))

"""
Heap Sort
:param arr:
"""
def heap_sort(arr, cmp=_cmp):
  n = len(arr)
  for i in range(n//2, -1, -1):
    Heap.heapify(arr, n, i, cmp)
  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    Heap.heapify(arr, i, 0, cmp)