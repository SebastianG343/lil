cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
print("Digite ¨000¨ para acabar el bucle")
while True:
    print("Digite un numero")
    n=int(input( ))
    if n>0:
        cont1 += 1
        if n%2==0:
            cont3 += 1
        else:
            cont4 += 1
        if n%8==0:
            cont5 +=1
    else:
        cont2 += 1
    if n==000:
        print("Numeros positivos:",cont1)
        print("Numeros negativos:",cont2-1)
        print("Numeros pares:",cont3)
        print("Numeros impares:",cont4)
        print("Numeros multiplos de 8:",cont5)
        break
    
    
