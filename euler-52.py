def euler():
    d = True
    x = 1
    while d == True:
        x += 1
        x_1 = str(x)
        x_2 = f"{2 * x}"
        x_3 = f"{3 * x}"
        x_4 = f"{4 * x}"
        x_5 = f"{5 * x}" 
        x_6 = f"{6 * x}"
        if len(x_1) !=  len(x_6):
            continue
        sez1 = []
        sez2 = []
        sez3 = []
        sez4 = []
        sez5 = []
        sez6 = []
        for t in range(len(x_1)):
            sez1.append( x_1[t])
            sez2.append(x_2[t])
            sez3.append(x_3[t])
            sez4.append(x_4[t])
            sez5.append(x_5[t])
            sez6.append(x_6[t])
        sez1.sort()
        sez2.sort()
        sez3.sort() 
        sez4.sort()
        sez5.sort()
        sez6.sort()
        if sez1 == sez2 == sez3 == sez4 == sez5 == sez6:
            return x
    return False

euler()
            
