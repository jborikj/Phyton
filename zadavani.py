vstup1 = input("Zadej číslo: ")
vstup2 = input("Zadej číslo: ")

print(type(vstup1))

cislo1 =int(vstup1)  #int delani vstupu na cela cisla (musi byt cislo) float 
cislo2 =float(vstup2) #float cte i cisla s desetinou carkou

v = vstup1 +vstup2
vysledek = cislo1 + cislo2

print("Soucet cisel je:" +str(vysledek))

print(f"Soucet cisel je: {vysledek}.") #to stejny jako o radku nad

print(f"Soucet cisel je: (vysledek.)")