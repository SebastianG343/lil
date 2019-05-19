import random
ln=[ ]
ln2=[ ]
cont=0
while cont<100:
    for i in range (0,201):
        ln.append(i)
        random.shuffle(ln)
    if ln[0] % 2 == 0:
        if ln[0] not in ln2:
            ln2.append(ln[0])
            cont += 1
        print("Numeros leidos:",ln2)
        print("Cantidad numeros leidos:",cont)

        

