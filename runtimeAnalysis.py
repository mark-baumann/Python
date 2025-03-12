import time
import random
import matplotlib.pyplot as plt
import numpy as np

# 🔹 Lineare Suche - O(n)
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 🔹 Binäre Suche - O(log n) (nur für sortierte Listen)
def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 🔹 Bubble Sort - O(n^2)
def bubbleSort(arr):
    arr = arr.copy()  # Originaldaten nicht verändern!
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr  # Sortierte Liste zurückgeben

# 🔹 Quick Sort - O(n log n) im Durchschnitt
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

# 🔹 Laufzeitanalyse (robuster gegen Schwankungen: Median statt Mittelwert)
def measureTime(algorithm, arr, *args, runs=7):
    times = []
    for _ in range(runs):
        arr_copy = arr.copy()  # Vermeidet Veränderung des Originals
        start_time = time.time()
        algorithm(arr_copy, *args) if args else algorithm(arr_copy)
        times.append(time.time() - start_time)
    return np.median(times)  # Median für weniger Ausreißer

# 🔹 Testparameter
sizes = [5, 10, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
times_linear, times_binary, times_bubble, times_quick = [], [], [], []

for size in sizes:
    arr = random.sample(range(size * 10), size)  # Zufällige Liste
    sorted_arr = sorted(arr)  # Für binäre Suche nötig

    # 🔹 Messung der Laufzeiten (robust)
    times_linear.append(measureTime(linearSearch, arr, random.choice(arr)))
    times_binary.append(measureTime(binarySearch, sorted_arr, random.choice(sorted_arr)))
    times_bubble.append(measureTime(bubbleSort, arr))
    times_quick.append(measureTime(quickSort, arr))

# 🔹 Plot der Ergebnisse
plt.figure(figsize=(10, 6))
plt.plot(sizes, times_linear, label="Linear Search (O(n))", marker='o', linestyle='--', color='blue')
plt.plot(sizes, times_binary, label="Binary Search (O(log n))", marker='s', linestyle='-', color='orange')
plt.plot(sizes, times_bubble, label="Bubble Sort (O(n^2))", marker='d', linestyle='-', color='green')
plt.plot(sizes, times_quick, label="Quick Sort (O(n log n))", marker='x', linestyle='-', color='red')

# 🔹 Achsenanpassung
plt.xscale("log")  # Log-Skalierung für bessere Übersicht
plt.yscale("log")  # Da Unterschiede sehr groß sind
plt.xlabel("Input Size (n)")
plt.ylabel("Time (s) (log scale)")
plt.legend()
plt.title("Runtime Analysis of Sorting & Search Algorithms")

# 🔹 Diagramm
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()
