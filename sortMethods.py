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


#### MAIN ####

arr = [12, 11, 13, 5, 6]
selection_sort(arr)
for i in range(len(arr)):
    print("%d" %arr[i])
