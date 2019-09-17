from typing import List


def binary_search(lst: List[int], item: int) -> int:
    """Finds item in lst. Return either index of item in lst, or -1 if item
    is not in lst.

    Parameters
    ----------
    lst : List[int]
          A list of ordered integers
    item : int
           Item to be found in lst
    Returns
    -------
    int
    """
    assert all(isinstance(item, int) for item in lst)
    assert isinstance(item, int)
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = low + high
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1
