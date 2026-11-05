#Es 05.1.3 Fattorizzazione di interi

numero = int(input("Inserisci un numero intero -> "))
cont = 2
numero_corrente = numero

while numero_corrente > 1 and cont <= numero // 2:
    divisori = 0
    for k in range(2, cont):
        if k / cont % 1 == 0:
            divisori += 1
    
    if numero_corrente / cont % 1 == 0 and divisori == 0:
        numero_corrente = numero_corrente / cont
        print(cont)
    else:
        cont += 1
    

        
            
        
    