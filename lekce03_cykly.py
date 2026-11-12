x = 10

while(x > 5): #dokud platí (x > 5) opakuj cyklus
    print("ahoj")
    x = x-1
    if x == 7:
        continue #pokud je x 7. preskoci se print x a de rovnou na ahoj, break pokud x==7 de se printit rovnou konec
    print (x)

print("konec")

while True: 
    print("vyber možnost")
    y = input ('Zadej volbu: ')
    if y == "A":
        print("ahoj")
    if y == "X":
        break

