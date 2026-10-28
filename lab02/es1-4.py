#Es 02.1.4 Auto ibrida

costo_nuova = float(input("Inserisci il costo dell'auto nuova -> "))
stima_km = int(input("Inserisci la stima dei km percorsi in un anno -> "))
stima_carb = float(input("Inserisci la stima del costo del carburante -> "))
efficienza = float(input("Inserisci l'efficienza in km al litro -> "))
stima_vendita = float(input("Inserisci la stima del valore di rivendita dell'auto usata dopo 5 anni -> "))

costo_totale = costo_nuova + (stima_km/efficienza*stima_carb)*5 - stima_vendita

print(f"Il costo totale in 5 anni (compresa la rivendita e il relativo guadagno) è {costo_totale}")