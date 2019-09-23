from abc import ABCMeta, abstractmethod
from random import randint
from typing import Any, List, TypeVar


###############################################################################
#####                       Comparable type                               #####
###############################################################################
class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        ...

    def __le__(self, other: Any) -> bool:
        ...

    def __gt__(self, other: Any) -> bool:
        ...

    def __ge__(self, other: Any) -> bool:
        ...


# making it a type variable
CT = TypeVar("CT", bound=Comparable)


###############################################################################
#####                         Quicksort                                   #####
###############################################################################
def quicksort(array: List[CT]) -> List[CT]:
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
        r = randint(0, len(array))
        pivot = array[r]
        del array[r]
        less = [i for i in array if i <= pivot]
        greater = [i for i in array if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
