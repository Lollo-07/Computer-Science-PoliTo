#Es 03.1.6 De Morgan

x = int(input("Inserisci un numero intero -> "))

#Caso 1
espressione1 = not (x > 0 and x < 100)
espressione2 = not (x > 0) or not (x < 100)
print(f"{espressione1}")
print(f"{espressione2}")
print