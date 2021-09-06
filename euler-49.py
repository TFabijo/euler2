from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement

def je_prastevilo(n):
    for x in range(2,int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

def euler_49():
    konbinacije = list(combinations_with_replacement([0,1,2,3,4,5,6,7,8,9],4))
    for k in konbinacije:
        variacije = []
        l = list(permutations(k))
        for p in l:
            i = 1000
            vsota = 0
            for x in p:
                if i == 1000 and x == 0:
                    break
                vsota += x * i
                i //= 10
            if vsota == 0:
                continue
            if int(vsota) not in variacije:
                variacije.append(int(vsota))
        l = 0
        for v in variacije:
            if l == len(variacije) - 2:
                break
            l += 1
            if je_prastevilo(v) == False:
                continue
            for t in range(l,len(variacije)-1):
                d = variacije[t] - v
                if (v + d) in variacije and (v + 2 * d) in variacije and je_prastevilo(v + d) and je_prastevilo(v + 2 * d):
                    stevilo = str(v) + str(v + d) + str(v + 2 * d)
                    if stevilo == '148748178147':
                        pass
                    else:
                        return int(stevilo)
    return False


euler_49()



            
                


