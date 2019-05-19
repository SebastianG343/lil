contfail = 0
us=input("Digite usuario")
ps=input("Digite contraseña")
print("--------------->.<---------------")
while True and contfail < 3:
    uss=input("Digite usuario")
    pss=input("Digite contraseña")
    if uss==us and ps==pss:
        print("El usuario y el psw coinciden")
        break
    else:
        print("Asegurece de digitar bien")
        contfail += 1
    if contfail == 3:
        print("Vuelva mas tarde")
        
    

