from rcdsa.algorithm import search


def test_linear_search():
  arr = [64, 34, 25, 12, 22, 90, 11]
  assert search.linear_search(arr, 22) == 4
  assert search.linear_search(arr, 1000) == -1

def test_binary_search():
  arr = [11, 12, 22, 25, 34, 64, 90] 
  assert search.binary_search(arr, 90) == 6
  assert search.binary_search(arr, 1000) == -1
