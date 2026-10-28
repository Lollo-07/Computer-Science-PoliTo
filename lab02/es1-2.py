#Es 02.1.2 Resistenze

r1 = float(input("Inserisci il valore della resistenza r1 -> "))
r2 = float(input("Inserisci il valore della resistenza r2 -> "))
r3 = float(input("Inserisci il valore della resistenza r3 -> "))

r_totale = r1 + (r2*r3/(r2+r3))

print(r_totale)
