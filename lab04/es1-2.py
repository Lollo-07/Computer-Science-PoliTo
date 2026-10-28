#Es 04.1.2 Analisi di una stringa

stringa = input("Inserisci una stringa -> ")
caratteri_maiuscoli = ""
caratteri_pari = ""
stringa_underscore = ""
vocali = "aeiouAEIOU"
numero_cifre = 0
posizioni_vocali = ""


for i, carattere in enumerate(stringa):
    
    #Controllo ogni carattere e prendo solo quelli maiuscoli
    if carattere.isupper():
        caratteri_maiuscoli += carattere
    
    #Controllo l'indice, se è pari prendo il carattere
    if i % 2 == 0:
        caratteri_pari += carattere
        
    #Controllo ogni carattere, se è una vocale metto _, inoltre prendo la posizione del carattere
    if carattere in vocali:
        stringa_underscore += "_"
        posizioni_vocali = posizioni_vocali + str(i) + ", " 
    else: 
        stringa_underscore += carattere
    
    #Controllo se il carattere è un numero e lo conto
    if carattere.isdigit():
        numero_cifre += 1
    
        
print(f"I caratteri maiuscoli sono -> {caratteri_maiuscoli}")
print(f"Le lettere in posizioni pari sono -> {caratteri_pari}")
print(stringa_underscore)
print(f"Il numero di cifre nella stringa è -> {numero_cifre}")
print(f"Le posizioni delle vocali sono {posizioni_vocali}")