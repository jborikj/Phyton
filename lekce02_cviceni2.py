cislo1 = input("zadej stranu a: ")
cislo2 = input("zadej stranu b: ")
cislo3 = input("zadej stranu c: ")

a= float(cislo1)
b= float(cislo2)
c= float(cislo3)

if a + b > c and b + c >a and c + a > b: #musí platit vsechny tri podmiky jinak else
    print("trojúhelník je sestrojitelný")
else:
    print("trojúhelník není sestrojitelný")


