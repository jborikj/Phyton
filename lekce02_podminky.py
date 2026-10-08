vek = 20
print ("Muj vek je: " + str(vek))

if vek >=18 and vek < 65:       #pokud toto plati, pokud ne skoci na dalis instrkuci, tab je dulezitej aby byl pod if, bez se vykona print i bez 
     print("Jsem dospělý")      #vykona se totok
     print("a můžu chlastat")
elif vek >=15:                  #neplati podminka soupe se sem (elseif)
     print("Jsem mladiství")
else:                           #kdyz neplati if ani elif
     print("Jsem dítě")
     print("a můžu pít vodu")

print("Tečka.")


muj_vek = 18

if muj_vek >=18: #if if dve nezavisli podminky
     print("Jsem dospělý, protože je mi " + str(muj_vek))

if muj_vek >=65:
        print("Krmim holuby protože je mi "+str(muj_vek))

else: #za if a elif musi byt podminka, za else nesmi byt
        print("Jsem děcko protože je mi " +str(muj_vek))


