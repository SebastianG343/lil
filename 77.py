import random
lp = [ ]
capmax = 18000
peso = 0
ganancias = 0
nt= 0
mp= [ ]
ml= [ ]
for i in range (1,650):
    lp.append(i)
    random.shuffle(lp)
while peso < capmax:
    print("Peso del bulto:",lp[0])
    if lp[0] < 25:
        ganancias += 0
        peso += lp[0]
        nt += 1
        ml.append (lp[0])
    else:
        if lp[0] < 300:
            ganancias += 1500
            peso += lp[0]
            nt += 1
            ml.append (lp[0])
        else:
            if lp[0] < 500:
                ganancias += 2500
                peso += lp[0]
                nt += 1
                ml.append (lp[0])
            else:
                print("Muy pesado, no se permite")
print("Bultos ingresados al vuelo", nt)

    
    
