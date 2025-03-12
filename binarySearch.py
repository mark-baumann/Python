# Funktion zur Durchführung der Binärsuche in einer sortierten Liste
def binarySearch(arr, target):
    left, right = 0, len(arr) - 1  # Start- und Endindex der Liste

    while left <= right:  # Solange die Suchgrenze gültig ist
        mid = (left + right) // 2  # Berechnung des mittleren Indexes

        if arr[mid] == target:  # Falls das mittlere Element das gesuchte ist
            return mid + 1  # Rückgabe der Position (1-basierter Index)

        elif arr[mid] < target:  # Falls das Ziel größer ist als das mittlere Element
            left = mid + 1  # Suche im rechten Teil der Liste fortsetzen

        else:  # Falls das Ziel kleiner ist als das mittlere Element
            right = mid - 1  # Suche im linken Teil der Liste fortsetzen

    return -1  # Rückgabe von -1, falls das Ziel nicht gefunden wurde


# Gegebene sortierte Liste zur Suche
numbers = [1, 3, 5, 7, 9, 11, 12]

try:
    # Eingabe des Suchwerts
    target = int(input("Gebe eine gesuchte Zahl ein: "))

    # Aufruf der Binärsuche-Funktion
    result = binarySearch(numbers, target)

    # Ausgabe des Ergebnisses
    if result != -1:
        print(f"Gefunden an der {result}. Stelle")
    else:
        print("Nicht gefunden")

except ValueError:
    print("Bitte eine gültige Zahl eingeben!")  # Fehlerbehandlung für ungültige Eingaben
