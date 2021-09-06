def euler_48():
    vsota = 0
    for n in range(1,1001):
        vsota += n ** n
    st = str(vsota)
    l = len(st)
    return int(st[l - 10:])

euler_48()