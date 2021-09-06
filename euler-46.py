def goldbach():
    prastevila = [2,3,5,7,11,13,17]
    i = len(prastevila)
    d = True
    stevilo = 3
    while d == True:
        if stevilo in prastevila:
            stevilo += 2
        elif stevilo > prastevila[-1]:
            i += 1
            s = prastevila[-1]
            while len(prastevila) != i:
                s += 1
                l = True
                for x in range(2, int(s ** 0.5) + 1):
                    if l == False:
                        break
                    elif s % x == 0:
                        l = False
                if l == True:
                    prastevila.append(s)
        else:
            k = True
            for pra in prastevila:
                st = 1
                vsota = 0
                if k == False:
                    stevilo += 2
                    break
                while vsota < stevilo:
                    vsota = pra + 2 * st ** 2
                    st += 1
                    if vsota == stevilo:
                        k = False
                        break
            if k == True:
                return stevilo


goldbach()


                    




        
