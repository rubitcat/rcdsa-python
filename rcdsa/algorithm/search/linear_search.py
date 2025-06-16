from rcdsa.algorithm.search import default_cmp 

def linear_search(arr, x, low=None, high=None, cmp=default_cmp):

  low = 0 if low is None or low < 0 else low
  high = len(arr) if high is None or high > len(arr) else high

  if low < high:
    for i in range(low, high):
      if cmp(arr[i], x) == 0:
        return i
  return -1
