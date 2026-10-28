#Es 02.1.5 Forza elettrica

import math

EPSILON = 8.854 / 1000000000000

q1 = float(input("Inserisci il valore della carica q1 -> "))
q2 = float(input("Inserisci il valore della carica q2 -> "))
r = float(input("Inserisci il valore della distanza r in metri -> "))

f = (q1*q2)/(4*math.pi*EPSILON*r**2)

print(f)