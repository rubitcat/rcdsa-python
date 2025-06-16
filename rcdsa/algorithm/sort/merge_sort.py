from rcdsa.algorithm.sort import default_cmp
from rcdsa.datastruct import LinkedStack

"""
Merge Sort
:param arr:
"""
def merge_sort(arr, cmp=default_cmp):
  class Param:
    def __init__(self, left, right, divided):
      self.left = left
      self.right = right
      self.divided = divided
  
  stack = LinkedStack()
  stack.push(Param(0, len(arr)-1, False))
  while not stack.is_empty():
    curr = stack.top()
    mid = (curr.left + curr.right)//2
    if not curr.divided:
      if curr.left < mid:
        stack.push(Param(curr.left, mid, False))
      if mid+1 < curr.right:
        stack.push(Param(mid+1, curr.right, False))
      curr.divided = True
    else:
      subarr_left = arr[curr.left:mid+1]
      subarr_right = arr[mid+1:curr.right+1]
    
      ln = len(subarr_left)
      rn = len(subarr_right)
      lp = 0
      rp = 0
      ap = curr.left
      while lp < ln and rp < rn:
        if cmp(subarr_left[lp], subarr_right[rp]) > 0:
          arr[ap] = subarr_right[rp]
          rp += 1
        else:
          arr[ap] = subarr_left[lp]
          lp += 1
        ap += 1
      while lp < ln:
        arr[ap] = subarr_left[lp]
        lp += 1
        ap += 1
      while rp < rn:
        arr[ap] = subarr_right[rp]
        rp += 1
        ap += 1
        
      stack.pop()
