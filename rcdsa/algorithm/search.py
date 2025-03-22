def linear_search(arr, N, x):
  for i in range(0, N):
    if (arr[i] == x):
      return i
  return -1



def binary_search(arr, low, high, x):
  while low <= high:
    mid = low + (high - low) // 2
    if arr[mid] == x:
      return mid
    elif arr[mid] < x:
      low = mid + 1
    else:
      high = mid - 1
  return -1