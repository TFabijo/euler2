# upostevamo da je pri istem n-ju trikotno stevilo najmajse drugo je pentagonalno in tretje je heksagonalno



def Euler_45():
    t_i = 285
    p_i = 165
    h_i = 143
    trikotna = []
    petagonalna = []
    heksagonalna = []
    d = True
    while d == True:
        t_i += 1
        p_i += 1
        h_i += 1
        t = int((t_i * (t_i + 1)) / 2)
        p = int((p_i * (3 * p_i - 1)) / 2)
        h = int(h_i * (2 * h_i - 1))
        trikotna.append(t)
        if t in petagonalna and t in heksagonalna:
            return t
        else:
            petagonalna.append(p)
            heksagonalna.append(h)
    return False

Euler_45()