# Funktion zum Sortieren einer Liste mit dem BubbleSort-Verfahren
def BubbleSort(arr):
    n = len(arr)  # Länge der Liste ermitteln

    # Schleife über jedes Element der Liste
    for i in range(n):
        # Schleife, um nebeneinander liegende Elemente paarweise zu vergleichen
        for j in range(n - 1):
            # Wenn aktuelles Element größer als das nächste Element ist, werden sie vertauscht
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Vertauschen der beiden Elemente

    # Die sortierte Liste wird zurückgegeben
    return arr

# Beispiel-Liste zum Testen des Algorithmus
numbers = [5, 3, 8, 1, 2]

# Ausgabe der sortierten Liste
print("Sortierte Liste:", BubbleSort(numbers))
