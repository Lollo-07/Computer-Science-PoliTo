#Es 05.1.2 Noms des pays

vocali = "AEIOU"

nazione = input("Inserisci il nome di una nazione in francese -> ")

while nazione[0].islower():
    print("La nazione deve iniziare con la lettera maiuscola!")
    nazione = input("Inserisci il nome di una nazione in francese -> ")
    
#Non uso le liste perchè non sono ancora state fatte
if nazione == "Belize" or nazione == "Cambodge" or nazione == "Mexique" or nazione == "Mozambique" or nazione == "Zaire" or nazione == "Zimbawe":
    print(f"le {nazione}")

elif nazione == "Etats-Unis" or nazione == "Pays-Bas":
    print(f"les {nazione}")
    
elif nazione[0] in vocali:
    print(f"l'{nazione}")

elif nazione[-1] == "e":
    print(f"la {nazione}")

else:
    print(f"le {nazione}")