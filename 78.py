import math
Decimal = int(input("Digite el numero Decimal que quiere convertir a Binario: "))
Binario = ""
if (Decimal > 0):
    while(Decimal > 0):
        if (Decimal%2 == 0):
            Binario = "0" + Binario
        else:
            Binario = "1" + Binario
        Decimal = int(math.floor(Decimal/2))
else:
    if (Decimal == 0):
        Binario = "0"
    else:
        Binario = "ERROR404 :v (Asegurese que es un numero decimal y que sea positivo)"
print ("El Decimal convertido a Binario es: "+Binario)

        
    

        

