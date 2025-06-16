from rcdsa.algorithm.sort import default_cmp

"""
Insertion Sort
:param arr:
"""
def insertion_sort(arr, cmp=default_cmp):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and cmp(arr[j], key) > 0:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key