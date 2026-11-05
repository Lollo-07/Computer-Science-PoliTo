#Es 06.1.4 Saldo bancario

def conto_bancario(anni, saldo_iniziale, tasso_interesse):
    saldo_aggiornato = saldo_iniziale
    for _ in range(anni):
        saldo_aggiornato = saldo_aggiornato + (saldo_aggiornato*tasso_interesse/100)
    return saldo_aggiornato


anni = int(input("Inserisci il numero di anni di cui bisogna calcolare l'interesse -> "))
saldo_iniziale = float(input("Inserisci il saldo iniziale -> "))
tasso_interesse = float(input("Inserisci il tasso di interesse annuo -> "))

print(f"Dopo {anni} anni il conto sarà di {conto_bancario(anni, saldo_iniziale, tasso_interesse)}")


