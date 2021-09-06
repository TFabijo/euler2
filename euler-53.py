def fakulteta(n):
    z = 1
    if n == 0:
        return 1
    for x in range(1,n+1):
        z *= x
    return z


def binomski(n,r):
    s = n - r
    return (fakulteta(n)) / (fakulteta(r) * fakulteta(s))

def euler_53():
    st = 0
    for n in range(2,101):
        for t in range(1,n+1 // 2 ):
            if binomski(n,t) >= 1000000:
                st += 1
    return st

euler_53()
    