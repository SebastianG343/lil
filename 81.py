caracter = rawinput("Caracter =",[0])
pisos = int(input("Pisos = ")) 
for i in range(pisos): 
    print (" ") * (pisos - 1 - i) + caracter * (i * 2 + 1) 

