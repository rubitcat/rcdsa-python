
def _cmp(x, y):
  if x.__gt__(y):
    return 1
  elif x.__lt__(y):
    return -1
  else:
    return 0


def linear_search(arr, x, low=None, high=None, cmp=_cmp):

  low = 0 if low is None or low < 0 else low
  high = len(arr) if high is None or high > len(arr) else high

  if low < high:
    for i in range(low, high):
      if cmp(arr[i], x) == 0:
        return i
  return -1


def binary_search(arr, x, low=None, high=None, cmp=_cmp):

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