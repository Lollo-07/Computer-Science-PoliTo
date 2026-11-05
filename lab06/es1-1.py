#Es 06.1.1 Conteggio vocali

vocali = "AEIOUaeiou"

def count_vowels(string):
    cont = 0
    for carattere in string:
        if carattere in vocali:
            cont +=1
    return cont



stringa = input("Inserisci una stringa -> ")
numero_vocali = count_vowels(stringa)
print(f"Ul numero di vocali è: {numero_vocali}")