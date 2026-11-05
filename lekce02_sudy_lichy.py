zadane_cislo = input("zadej číslo:")

cislo = int(zadane_cislo)


if cislo % 2 == 0: # %celo číselné dělení, musi byt vzdycky ==
    print (f"Číslo {cislo} je sudé")
else:
    print (f"Číslo {cislo} je liché")