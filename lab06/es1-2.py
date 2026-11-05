#Es 06.1.2 Conteggio parole

def count_words(string):
    cont = 1      #Parto da 1 perchè conto il numero di spazi, ma la prima parola non ne ha.
    for carattere in string:
        if carattere == " ":
            cont += 1
    return cont



stringa = input("Inserisci una stringa -> ")
numero_parole = count_words(stringa)
print(f"Il numero di parole è: {numero_parole}")