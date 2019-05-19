cont1=0
cont2=0
print("Digite ¨000¨ para acabar el bucle")
while True:
    print("Digite un numero")
    n=int(input( ))
    if n>=100:
        cont1 += 1
    else:
        cont2 += 1
    if n==000:
        print("Numeros mayores a 100:",cont1)
        print("Numeros menores a 100:",cont2-1)
        break
    
    
