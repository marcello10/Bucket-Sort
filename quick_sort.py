def quick_sort(arr):
    """
    Sorts the array using QuickSort algorithm.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return np.concatenate([quick_sort(left), middle, quick_sort(right)])