from abc import ABCMeta, abstractmethod
from random import randint
from typing import Any, List, Sequence, TypeVar
from typing_extensions import Protocol

###############################################################################
#####                       Comparable type                               #####
###############################################################################
C = TypeVar("C", bound="Comparable")


class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...

    def __lt__(self: C, other: C) -> bool:
        ...

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other


###############################################################################
#####                         Quicksort                                   #####
###############################################################################
def quicksort(array: List[C]) -> List[C]:
    """Returns a sorted list
    Params:
    ------
        List[CT] - a list of comparable elements
    Returns:
        List[CT] - a sorted list of comparable elements
    -------
    """
    if len(array) < 2:
        return array
    else:
        # or use the median
        r = randint(0, len(array) - 1)  # a random integer N such that a <= N <= b.
        pivot = array[r]
        del array[r]
        less = [i for i in array if i <= pivot]
        greater = [i for i in array if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
