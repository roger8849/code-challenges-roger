
from inspect import _void
from typing import List


def bubbleSort(array: List, ascending = True) -> _void:
    size = len(array)
    swapped = True
    # assuming the array is not sorted.
    while swapped:
        swapped = False
        for i in range(size - 1):
            if (ascending and array[i] > array[i + 1]) or (not ascending and array[i] < array[i+1]):
                 array[i], array[i+1] = array[i+1], array[i]
                 swapped = True

def main():
    array = [4,5,3,1,2]
    bubbleSort(array)
    assert array == [1,2,3,4,5]

    array = [4,5,3,1,2]
    bubbleSort(array, False)
    assert array == [5,4,3,2,1]

if __name__ == "__main__":
    main()