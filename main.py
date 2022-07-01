import random
from typing import List, Any


ELEMENTS = ['a'] * 100000


def shuffle_fy_original(arr: List[Any]) -> List[Any]:
  """Returns a new shuffled array. The shuffling is
  done using the original Fisher Yates Shuffling Algorithm.

  Note: Original Algorithm was not designed to be used for computers
  """
  # _arr creates a copy of the given array so that we
  # do not accidentally modify it
  # _sarr will contain the shuffled array
  _arr, _sarr = list(arr), []

  while _arr:
    k = random.randint(0, len(_arr) - 1)
    e = _arr.pop(k)
    _sarr.append(e)

  return _sarr


def shuffle_fy_efficient(arr: List[Any]) -> List[Any]:
  """Returns a new shuffled array. The shuffling is
  done using the efficient Fisher Yates Shuffling Algorithm
  as suggested by Richard Durstenfeld.
  """
  # creating a copy of the array and shuffling will be
  # done in-place using efficinet Fisher Yates
  _sarr = list(arr)

  for i in range(0, len(_sarr) - 1):
    j = random.randint(i, len(_sarr) - 1)
    _sarr[i], _sarr[j] = _sarr[j], _sarr[i]

  return _sarr


print(shuffle_fy_original(ELEMENTS))
print(shuffle_fy_efficient(ELEMENTS))
