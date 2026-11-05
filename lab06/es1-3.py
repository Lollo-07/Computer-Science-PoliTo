#Es 06.1.3 Solidi geometrici

import math

def sphere_volume(r):       
    return 4/3*math.pi*r**3

def sphere_surface(r):
    return 4*math.pi*r**2

def cylinder_volume(r, h):
    return math.pi*r**2*h

def cylinder_surface(r, h):
    area_base = math.pi*r**2
    area_laterale = 2*math.pi*r*h
    return area_base*2 + area_laterale

def cone_volume(r, h):
    return (math.pi*r**2*h)/3

def cone_surface(r, h):
    area_base = math.pi*r**2
    apotema = math.sqrt(r**2 + h**2)
    area_laterale = math.pi*r*apotema
    return area_base + area_laterale


raggio = float(input("Inserisci il raggio dei solidi -> "))
altezza = float(input("Inserisci l'altezza dei solidi -> "))

print(f"Il volume della sfera è {sphere_volume(raggio)}, mentre la sua superficie è {sphere_surface(raggio)}")
print(f"Il volume del cilindro è {cylinder_volume(raggio, altezza)}, mentre la sua superficie è {cylinder_surface(raggio, altezza)}")
print(f"Il volume del cono è {cone_volume(raggio, altezza)}, mentre la sua superficie è {cone_surface(raggio, altezza)}")


