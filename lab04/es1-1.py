#Es 04.1.1 Numeri interi

numero = int(input("Inserisci un numero o lascia vuoto per terminare -> "))
somma = 0
massimo = numero
minimo = numero
nPari = 0
nDispari = 0
while numero != "":
    print("Numero")
    numero = int(numero)
    
    #Calcolo della somma parziale
    somma += numero
    print(f"La somma parziale è {somma}")
    
    #Controllare se il numero è un massimo o un minimo
    if numero > massimo:
        massimo = numero
    if numero < minimo:
        minimo = numero
        
    #Guardare se il numero è pari o dispari
    if numero % 2 == 0:
       nPari += 1
    else:
        nDispari += 1
    
    numero = input("Inserisci un numero o lascia vuoto per terminare -> ")
    
    
print(f"Il minimo tra i numeri inseriti è {minimo}")
print(f"Il massimo tra i numeri inseriti è {massimo}")
print(f"Il numero di pari è {nPari}")
print(f"Il numero di dispari è {nDispari}")