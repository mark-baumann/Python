# Funktion zur Berechnung des größten gemeinsamen Teilers (GGT) mit dem effizienten euklidischen Algorithmus
def euklidischer_algorithmus_2(a, b):
    # Speichert die ursprünglichen Werte von a und b zur späteren Ausgabe
    original_a, original_b = a, b

    # Solange b nicht 0 ist, wird der Algorithmus fortgesetzt
    while b != 0:
        a, b = b, a % b  # Setze a auf b und b auf den Rest der Division von a durch b

    # Wenn b 0 ist, dann ist a der größte gemeinsame Teiler (GGT)
    return a, original_a, original_b

# Nutzereingabe: Zwei natürliche Zahlen werden abgefragt
a = int(input("Gib eine natürliche Zahl a ein: "))
b = int(input("Gib eine natürliche Zahl b ein: "))

# Aufruf der Funktion zur Berechnung des GGTs
ggt, zahl1, zahl2 = euklidischer_algorithmus_2(a, b)

# Ausgabe des Ergebnisses
print(f"Der größte gemeinsame Teiler von {zahl1} und {zahl2} ist {ggt}.")
