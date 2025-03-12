# Funktion zur Berechnung des größten gemeinsamen Teilers (GGT) mit dem euklidischen Algorithmus
def euklidischer_algorithmus_1(a, b):
    # Speichert die ursprünglichen Werte von a und b zur späteren Ausgabe
    original_a, original_b = a, b

    # Solange die beiden Zahlen nicht gleich sind, wird die größere um die kleinere reduziert
    while a != b:
        if a > b:
            a -= b  # Subtrahiere b von a, wenn a größer ist
        else:
            b -= a  # Subtrahiere a von b, wenn b größer ist

    # Wenn die Schleife endet, ist a (bzw. b) der größte gemeinsame Teiler
    return a, original_a, original_b


# Nutzereingabe: Zwei natürliche Zahlen werden abgefragt
a = int(input("Gib eine natürliche Zahl a ein: "))
b = int(input("Gib eine natürliche Zahl b ein: "))

# Aufruf der Funktion zur Berechnung des GGTs
ggt, zahl1, zahl2 = euklidischer_algorithmus_1(a, b)

# Ausgabe des Ergebnisses
print(f"Der größte gemeinsame Teiler von {zahl1} und {zahl2} ist {ggt}.")
