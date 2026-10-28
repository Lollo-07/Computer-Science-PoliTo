#Es 04.1.3 Lati

n = int(input("Inserisci un numero intero -> "))
'''
#Stampa un quadrato di * n x n
for i in range(n):
    print("*"*n)
'''
#Stampa un rombo di asterischi con lato n
for k in range(2*n):
    numero_asterischi = 2*k+1
    numero_spazi = 2*n-1         #Asterischi + spazi vuoti
    
    spazi_destra_sinistra = (numero_spazi - numero_asterischi) // 2
    
    if k < n:
       print(" "*spazi_destra_sinistra+"*"*numero_asterischi+" "*spazi_destra_sinistra)
    
        