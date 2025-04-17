def dezBin(zahl):
    """
    Funktion zur Umwandlung einer Dezimalzahl in eine Binärzahl.
    Die Ausgabe ist ein String, der die Binärdarstellung der Zahl enthält.
    """

    binaer = ""  # Speichert die Binärdarstellung als String
    potenz = 0  # Initialisierung der Potenz für die größte Zweierpotenz

    # Finde die größte Zweierpotenz, die kleiner oder gleich der Zahl ist
    while 2 ** potenz <= zahl:
        potenz += 1
    potenz -= 1  # Korrigiert die Potenz, da die Schleife um eins zu weit läuft

    # Berechnung der Binärzahl durch Subtraktion der Zweierpotenzen
    while potenz >= 0:
        if zahl >= 2 ** potenz:  # Prüfen, ob die aktuelle Potenz in der Zahl enthalten ist
            binaer += "1"  # Setze eine "1" an dieser Stelle der Binärzahl
            zahl -= 2 ** potenz  # Reduziere die Zahl um den Wert der aktuellen Zweierpotenz
        else:
            binaer += "0"  # Falls die Potenz nicht enthalten ist, setze eine "0"

        potenz -= 1  # Reduziere die Potenz für die nächste Stelle in der Binärdarstellung

    return binaer  # Rückgabe der vollständigen Binärzahl als String

# Testaufruf der Funktion
print(dezBin(10))  # Erwartete Ausgabe: "1010"
