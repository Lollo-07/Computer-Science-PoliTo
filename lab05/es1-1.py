#Es 05.1.1 ATM

PIN = "1234"
indovinato = False
n_tentativi = 0

while not indovinato and n_tentativi < 3:
    pin = input("Inserisci PIN -> ")
    n_tentativi += 1
    
    if pin == PIN:
        indovinato = True
        print("Il PIN è corretto!")
    else:
        print("Il PIN non è corretto!")
        
if not indovinato:
    print("La tua carta bancaria è bloccata!")