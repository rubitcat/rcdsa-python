

def default_cmp(x, y):
  if x > y:
    return 1
  elif x < y:
    return -1
  else:
    return 0


from .selection_sort import selection_sort
from .bubble_sort import bubble_sort
from .insertion_sort import insertion_sort
from .quick_sort import quick_sort
from .heap_sort import heap_sort
from .merge_sort import merge_sort