def prastevila_do_n(n):
    pra = [2,3,5,7]
    for x in range(8,n+1):
        d = True
        for y in range(2,int(x ** 0.5) + 1):
            if d == False:
                break
            elif x % y == 0:
                d = False
        if d == True:
            pra.append(x)
    return pra


def euler_50():
    pra = prastevila_do_n(1000000)
    najvecja_vsot_ki_je_prastevilo = 0
    stevilo_z_najvec_p = 0
    for p in pra:
        i = pra.index(p)
        if sum(pra[i:i+stevilo_z_najvec_p]) > 1000000:
            break
        stevilo_p = 0
        vsota = pra[i]
        for p1 in range(i+1,len(pra)):
            stevilo_p += 1
            vsota += pra[p1]
            if vsota > 1000000:
                break
            elif vsota in pra and stevilo_z_najvec_p < stevilo_p:
                najvecja_vsot_ki_je_prastevilo = vsota
                stevilo_z_najvec_p = stevilo_p
    return najvecja_vsot_ki_je_prastevilo




euler_50()