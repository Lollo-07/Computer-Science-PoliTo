#Es 03.1.5 Questione logica

x = int(input("Inserisci un numero intero -> "))

espressione1 = x > 0 and x < 100
espressione2 = x > 0 or x < 100
espressione3 = x > 0 or 100 < x
espressione4 = x > 0 and x < 100 or x == -1


print(f"x > 0 and x < 100    {espressione1}")
print(f"x > 0 or x < 100   {espressione2}")
print(f"x > 0 or 100 < x  {espressione2}")
print(f"x > 0 and x < 100 or x == -1    {espressione4}")