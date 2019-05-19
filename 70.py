import math
NumeroDeci=int(input("Ingrese un número en Binario ¨Ejem:110 = 6 O 11 = 3¨ Sin encadenar:"))
j=NumeroDeci
Suma=0
i=0
Binarioxd=NumeroDeci
while(i<j):
    LastNumber=Binarioxd%10
    Binarioxd=int(Binarioxd/10)
    if(LastNumber==0 or LastNumber==1):
        Suma=Suma + 2**i *LastNumber
    i=i+1
print(Suma)


