#Es 02.1.3 Cifre

N = int(input("Inserisci un numero intero positivo di cinque cifre -> "))

c1 = N % 10
c2 = int((N % 100 - c1 )/10)
c3 = int((N % 1000 - c1 - c2)/100)
c4 = int((N % 10000 - c1 - c2 - c3)/1000)
c5 = int((N % 100000 - c1 - c2 - c3 - c4)/10000)

print(c5)
print(c4)
print(c3)
print(c2)
print(c1)
