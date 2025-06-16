from rcdsa.algorithm.sort import default_cmp

"""
Bubble Sort
:param arr:
"""
def bubble_sort(arr, cmp=default_cmp):
  n = len(arr)
  for i in range(n):
    swapped = False
    for j in range(n-i-1):
      if cmp(arr[j], arr[j+1]) > 0:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
    if (swapped is False):
      break