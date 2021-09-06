def palindrom(n):
    return n == n[::-1]

def euler55():
    st = 0
    for n in range(1,10001):
        for i in range(50):
            n +=int(str(n)[::-1])
            if palindrom(str(n)):
                st += 1
                break
    return 10000 - st

euler55()

# če  dobimo palindrom ni Lychrel number za pocemo vsa stevila,ki
#niso Lychrel number in odejemo od 10000