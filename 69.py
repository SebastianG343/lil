l=[ ]
n=int(input("Digite un numero"))
for i in range (1,1000000000):
    if n % i == 0:
        l.append(i)
        print(l)
        
    
