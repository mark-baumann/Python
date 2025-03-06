def euklid_algorithmus(a, b):
    original_a, original_b = a, b
    while a != b:
        if a > b:
            a-=b
        else:
            b-=a
    return a, original_a, original_b

a = int(input("Gib eine natürliche Zahl a ein: "))
b = int(input("Gib eine natürliche Zahl b ein: "))

ggt, zahl1, zahl2 = euklid_algorithmus(a, b)

print(f"Der größte gemeinsame Teiler von {zahl1} und {zahl2} ist {ggt}.")