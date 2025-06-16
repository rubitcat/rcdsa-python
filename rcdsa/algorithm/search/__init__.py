
def default_cmp(x, y):
  if x > y:
    return 1
  elif x < y:
    return -1
  else:
    return 0
  

from .binary_search import binary_search
from .linear_search import linear_search