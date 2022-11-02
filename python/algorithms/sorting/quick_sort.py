from inspect import _void
from typing import List


# Python program for implementation of Quicksort


def partition(arr, start, end, ascending):
    i = start
    pivot = arr[end]
    for j in range(start, end):
        if ascending:
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        else:
            if arr[j] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
    arr[i], arr[end] = arr[end], arr[i]

    return i

def quickSort(arr, start, end, ascending=True):
    # Elements have been processed
    if start >= end:
        return
    partitionIdx = partition(arr, start, end, ascending)
    quickSort(arr, start, partitionIdx - 1, ascending)
    quickSort(arr, partitionIdx, end, ascending)

def main():
	array = [4,5,3,1,2]
	quickSort(array,0, len(array)-1)
	assert array == [1,2,3,4,5]

	array = [4,5,3,1,2]
	quickSort(array,0, len(array)-1, False)
	assert array == [5,4,3,2,1]

if __name__ == "__main__":
	main()