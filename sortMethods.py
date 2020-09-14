# To do:
# insertionSort()
# selection
# merge
# quick

import sys

def insertion_sort(arr):
	for j in range(1, len(arr)):
		
		temp = arr[j]
		i = j - 1

		while i >= 0 and temp < arr[i]:
			arr[i + 1] = arr[i]
			i -= 1
		arr[i + 1] = temp


def selection_sort(arr):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i + 1, len(arr)):
			if arr[min_idx] > arr[j]: 
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
	if len(arr) > 1:
		middle = len(arr) // 2 

		left = arr[:middle]
		right = arr[middle:]

		merge_sort(left)
		merge_sort(right)

		i = j = k = 0

		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1
# It may happen the program to fill completely the first vector while the
# second is not completely filled yet, i.e, all elements in the left vector
# are bigger than the elements in the second.
# To prevent the loss of elements, we do this:

		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1

def partition(arr, low, high):
	pivot = arr[high]
	i = low - 1

	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[j], arr[i] = arr[i], arr[j]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1

def quick_sort(arr, low, high):
	if low < high:
		pivot_idx = partition(arr, low, high)

		quick_sort(arr, low, pivot_idx - 1)
		quick_sort(arr, pivot_idx + 1, high)
	

#### MAIN ####

arr = [ 5, 4, 3, 2, 1 ]
quick_sort(arr, 0, len(arr) - 1)
for i in range(len(arr)):
	print(arr[i])
