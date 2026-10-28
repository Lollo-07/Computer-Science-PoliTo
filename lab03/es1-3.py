#Es 03.1.3 Stringhe e sottostringhe

sequenza_lunga = input("Inserisci una sequenza di DNA di 20 caratteri (A, C, T, G)-> ")
sequenza_corta = input("Inserisci una sequenza corta di Dna di 3 caratteri (A, C, T, G) -> ")

if len(sequenza_lunga)==20 and len(sequenza_corta)==3:
    if sequenza_corta in sequenza_lunga:
        print(f"La sequenza {sequenza_lunga} contiene la sequenza {sequenza_corta}. La sequenza corta si trova a partre dalla posizione {sequenza_lunga.find(sequenza_corta)}")
        print(f"La sequenza {sequenza_corta} appare {sequenza_lunga.count(sequenza_corta)} volte in {sequenza_lunga}.")
    else:
        print(f"La sequenza {sequenza_lunga} non contiene la sequenza {sequenza_corta}.")

else:
    print("La dimensione o i caratteri inseriti non soddisfano i requisiti.")