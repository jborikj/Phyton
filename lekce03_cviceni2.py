y = int(input ("Zadej číslo: "))

for i in range(y, -1, -1):
    print (i)


x = int(input ("Zadej číslo: "))

for i in range(0, x+1, 2): #1reseni
        print(i)

for i in range(x+1):
      if i%2 ==0:
            print(i)
print("Konec")


a = int(input ("Zadej číslo: "))

for i in range(a+1):
    if i%2 ==0:
        print(str(i) + "Číslo je sudé")
    else:
        print(f" {i} je liché")
    