from rcdsa.algorithm.search import default_cmp 

def binary_search(arr, x, low=None, high=None, cmp=default_cmp):

  low = 0 if low is None or low < 0 else low
  high = len(arr)-1 if high is None or high > len(arr)-1 else high
    
  while low <= high:
    mid = (low + high)//2
    if cmp(x, arr[mid]) > 0:
      low = mid + 1
    elif cmp(arr[mid], x) > 0:
      high = mid - 1
    else:
      return mid
  return -1
