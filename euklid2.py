def euklidischer_algorithmus_2(a, b):
    original_a, original_b = a, b

    while b!=0:
        a, b = b, a%b
    return a, original_a, original_b

a = int(input("Gib eine natürliche Zahl a ein: "))
b = int(input("Gib eine natürliche Zahl b ein: "))

ggt, zahl1, zahl2 = euklidischer_algorithmus_2(a, b)

print(f"Der größte gemeinsame Teiler von {zahl1} und {zahl2} ist {ggt}.")