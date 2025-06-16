from rcdsa.algorithm.sort import default_cmp

"""
Selection Sort
:param arr:
"""
def selection_sort(arr, cmp=default_cmp):
  for i in range(len(arr)-1):
    mxx = i
    for j in range(i+1, len(arr)):
      if cmp(arr[mxx], arr[j]) > 0:
        mxx = j
    if mxx != i:
      arr[i], arr[mxx] = arr[mxx], arr[i]