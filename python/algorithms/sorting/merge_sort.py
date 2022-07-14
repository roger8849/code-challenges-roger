

from inspect import _void
from typing import List


# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, start, mid, end, ascending):
	n1 = mid - start + 1
	n2 = end - mid

	# create temp arrays
	left = [0] * (n1)
	right = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		left[i] = arr[start + i]

	for j in range(0, n2):
		right[j] = arr[mid + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = start	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if ascending:
			if left[i] <= right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
		else:
			if left[i] >= right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
		k += 1

	# Copy the remaining elements of left[], if there
	# are any
	while i < n1:
		arr[k] = left[i]
		i += 1
		k += 1

	# Copy the remaining elements of right[], if there
	# are any
	while j < n2:
		arr[k] = right[j]
		j += 1
		k += 1




def mergeSort(arr, start, end, ascending=True):
	if start < end:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = start+(end-start)//2

		# Sort first and second halves
		mergeSort(arr, start, m, ascending)
		mergeSort(arr, m+1, end, ascending)
		merge(arr, start, m, end, ascending)






def main():
	array = [4,5,3,1,2]
	mergeSort(array,0, len(array)-1)
	assert array == [1,2,3,4,5]

	array = [4,5,3,1,2]
	mergeSort(array,0, len(array)-1, False)
	assert array == [5,4,3,2,1]

if __name__ == "__main__":
	main()