def binarySearch(arr, target):
    left, right = 0, len(arr) -1 #len(arr) - 1 bedeutet, dass wir den Index des letzten Elements einer Liste (arr) bestimmen
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid +1
        elif arr[mid] < target:
            left = mid +1
        else:
            right = mid -1
    return -1

numbers = [1, 3, 5, 7, 9, 11, 12]

try:
    target = int(input("Gebe eine gesuchte Zahl ein: "))
    result = binarySearch(numbers, target)

    if result != -1:
        print(f"Gefunden an der {result}. Stelle")
    else:
        print("Nicht gefunden")
except ValueError:
    print("Bitte eine gültige Zahl eingeben!")