zadany_vek = input("Zadej věk:")

vek =int(zadany_vek)


if vek >= 18:
    print ("Jsi starej je ti " + str (vek))
else:
    print ("Jsi mladej,") #bloky se scitaji +    nebo druha moznost (f"{}")
    if (18 - vek) == 1:
        print (f"do dospělosti ti zbývá {18 - vek} rok" )
    elif (18 - vek) <=4:
        print (f"do dospělosti ti zbývají {18 - vek} roky")
    else:
        print (f"do dospělosti ti zbývá {18 - vek} let")



