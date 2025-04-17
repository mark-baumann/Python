# Ein Knoten (Node) enthält Daten und einen Zeiger auf den nächsten Knoten
class Node:
    def __init__(self, daten):
        self.daten = daten      # Der gespeicherte Wert
        self.next = None        # Zeiger auf den nächsten Knoten (zuerst leer)

# Die verkettete Liste selbst
class LinkedList:
    def __init__(self):
        self.head = None        # Kopf der Liste (erstes Element)

    # Methode zum Anhängen eines neuen Knotens ans Ende
    def append(self, daten):
        neuer_knoten = Node(daten)
        # Wenn die Liste leer ist, wird der neue Knoten der Kopf
        if not self.head:
            self.head = neuer_knoten
        else:
            # Sonst bis zum letzten Knoten durchlaufen
            aktueller = self.head
            while aktueller.next:
                aktueller = aktueller.next
            # Und dort anhängen
            aktueller.next = neuer_knoten

    # Methode zum Ausgeben der gesamten Liste
    def anzeigen(self):
        aktueller = self.head
        while aktueller:
            print(aktueller.daten, end=" -> ")
            aktueller = aktueller.next
        print("None")  # Ende der Liste

# --- Hauptteil (zum Ausführen) ---

# Eine neue verkettete Liste erstellen
meine_liste = LinkedList()

# Daten anhängen
meine_liste.append(10)
meine_liste.append(20)
meine_liste.append(30)

# Liste anzeigen
meine_liste.anzeigen()
