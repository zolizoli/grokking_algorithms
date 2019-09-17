from typing import List


def findSmallest(arr: List[int]) -> int:
    """Find the index of the smallest int in a list of ints

    Parameters:
    ----------
    arr: a list of integers
    Returns:
    -------
    int
    """
    assert all(isinstance(item, int) for item in arr)
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr: List[int]) -> List[int]:
    """Returns an ordered list of integers

    Parameters:
    ----------
    arr: a list of integers
    Returns:
    -------
    List[int]
    """
    assert all(isinstance(item, int) for item in arr)
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
