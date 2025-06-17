from rcdsa.algorithm import sort

def test_selection_sort():
  arr = [64, 25, 12, 22, 11]
  sort.selection_sort(arr)
  assert arr == [11, 12, 22, 25, 64]
  sort.selection_sort(arr, cmp=lambda x,y: -sort.default_cmp(x,y))
  assert arr == [64, 25, 22, 12, 11]


def test_bubble_sort():
  arr = [64, 34, 25, 12, 22, 90, 11]
  sort.bubble_sort(arr)
  assert arr == [11, 12, 22, 25, 34, 64, 90]
  sort.bubble_sort(arr, cmp=lambda x,y: -sort.default_cmp(x,y))
  assert arr == [90, 64, 34, 25, 22, 12, 11]

def test_insertion_sort():
  arr = [12, 11, 13, 5, 6]
  sort.insertion_sort(arr)
  assert arr == [5, 6, 11, 12, 13]
  sort.insertion_sort(arr, cmp=lambda x,y: -sort.default_cmp(x,y))
  assert arr == [13, 12, 11, 6, 5]

def test_quick_sort():
  arr = [12, 11, 13, 5, 6]
  sort.quick_sort(arr)  
  assert arr == [5, 6, 11, 12, 13]
  sort.quick_sort(arr, cmp=lambda x,y: -sort.default_cmp(x,y))
  assert arr == [13, 12, 11, 6, 5]

def test_heap_sort():
  arr = [12, 11, 13, 5, 6, 7]
  sort.heap_sort(arr)
  assert arr == [5, 6, 7, 11, 12, 13]
  sort.heap_sort(arr, cmp=lambda x,y: -sort.default_cmp(x,y))
  assert arr == [13, 12, 11, 7, 6, 5]

def test_merge_sort():
  arr = [12, 11, 13, 5, 6, 7]
  sort.merge_sort(arr)
  assert arr == [5, 6, 7, 11, 12, 13]
  sort.merge_sort(arr, cmp=lambda x,y: -sort.default_cmp(x,y))
  assert arr == [13, 12, 11, 7, 6, 5]