from inspect import _void
import sys
from typing import List

def selectionSort(array: List, ascending = True) -> _void:
    size = len(array)
    for i in range(size - 1):
        # Mutable tuple to track index and element.
        max_or_min = [-1, sys.maxsize]
        
        # Array is sorted and we're done.
        if i + 1 == size:
            return
            
        if ascending:
            for j in range(i+1, size):
                if array[j] < max_or_min[1]:
                    max_or_min[0], max_or_min[1] = j, array[j]

            if array[i] > max_or_min[1]:
                array[i], array[max_or_min[0]] = array[max_or_min[0]], array[i]
        else:
            max_or_min[1] = -max_or_min[1]
            for j in range(i+1, size):
                if array[j] > max_or_min[1]:
                    max_or_min[0], max_or_min[1] = j, array[j]
            if array[i] < max_or_min[1]:
                array[i], array[max_or_min[0]] = array[max_or_min[0]], array[i]

def main():
    array = [4,5,3,1,2]
    selectionSort(array)
    assert array == [1,2,3,4,5]

    array = [4,5,3,1,2]
    selectionSort(array, False)
    assert array == [5,4,3,2,1]
    

if __name__ == "__main__":
    main()