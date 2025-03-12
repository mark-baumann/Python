def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


numbers = [5, 3, 8, 1, 2]
print("Sortierte Liste:", BubbleSort(numbers))