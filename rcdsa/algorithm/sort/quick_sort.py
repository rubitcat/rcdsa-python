from rcdsa.algorithm.sort import default_cmp
from rcdsa.datastruct import LinkedStack

"""
Quick Sort
:param arr:
"""
def quick_sort(arr, start=None, end=None, cmp=default_cmp):
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