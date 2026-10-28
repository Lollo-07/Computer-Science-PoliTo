#Es 03.1.2 Identikit della stringa

stringa = input("Inserisci una stringa -> ")

if stringa.isalpha():
    print(f"La stringa {stringa} contiene soltanto lettere.")
else:
    print(f"La stringa {stringa} non contiene soltanto lettere.")


if stringa.isupper():
    print(f"La stringa {stringa} contiene soltanto caratteri maiuscoli.")
else: 
    print(f"La stringa {stringa} non contiene soltanto caratteri maiuscoli.")


if stringa.islower():
    print(f"La stringa {stringa} contiene soltanto caratteri minuscoli.")
else: 
    print(f"La stringa {stringa} non contiene soltanto caratteri minuscoli.")

if stringa.isdigit():
    print(f"La stringa {stringa} contiene soltanto cifre decimali.")
else:
    print(f"La stringa {stringa} non contiene soltanto cifre decimali.")

if stringa.isalnum():
    print(f"La stringa {stringa} contiene soltanto lettere o cifre.")
else:
    print(f"La stringa {stringa} non contiene soltanto lettere o cifre.")

if stringa[0].isupper():
    print(f"La stringa {stringa} inizia con un carattere maiuscolo.")
else:
    print(f"La stringa {stringa} non inizia con un carattere maiuscolo.")

if stringa.endswith("."):
    print(f"La stringa {stringa} termina con un punto.")
else:
    print(f"La stringa {stringa} non termina con un punto.")