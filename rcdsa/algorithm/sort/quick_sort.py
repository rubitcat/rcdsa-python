from rcdsa.algorithm.sort import default_cmp
from rcdsa.datastruct import LinkedStack

"""
Quick Sort
"""
def quick_sort(arr, start=None, end=None, cmp=default_cmp):
  if start is None or end is None:
    start = 0
    end = len(arr) - 1

  stack = LinkedStack()
  stack.push((start, end))
  
  while not stack.is_empty():
    low, high = stack.top()
    stack.pop()

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
      if cmp(pivot, arr[j]) > 0:
        i = i + 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    if low < i+1-1:
      stack.push((low, i+1-1))
    if i+1+1 < high:
      stack.push((i+1+1, high))