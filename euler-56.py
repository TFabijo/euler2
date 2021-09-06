def vsota_stevk(n):
    s = str(n)
    vsota = 0
    for x in s:
        vsota += int(x)
    return vsota

def euler56():
    najvecja_vsota = 0
    for a in range(1,100):
        for b in range(1,100):
            st = a ** b
            s = vsota_stevk(st)
            if s > najvecja_vsota:
                najvecja_vsota = s
    return najvecja_vsota


euler56()
            
