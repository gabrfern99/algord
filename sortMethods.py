comps = 0
moves = 0
def insertion_sort(arr):
    global comps, moves
    for j in range(1, len(arr)):
        temp = arr[j]
        i = j - 1
        comps += 1
        while i >= 0 and temp < arr[i]:
            arr[i + 1] = arr[i]
            i -= 1
            moves += 1
        arr[i + 1] = temp

    return comps, moves

def selection_sort(arr):
    global comps, moves
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comps += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if arr[i] != arr[min_idx]:
            moves += 1

    return comps, moves

def merge_sort(arr):
    global comps, moves
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

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return comps, moves

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
            comps += 1
            moves += 2
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    moves += 2
    return i + 1, comps, moves

def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    return comps, moves
