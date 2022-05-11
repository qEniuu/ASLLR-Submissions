def fbeaf(x,y,z,q):
    if q == 1:
        if z == 1:
            return x**y
        else:
            for i in range(y):
                a = fbeaf(x,b,z-1,1)
                b = fbeaf(x,a,z-1,1)
            return a
    else:
        if z == 1:
            return fbeaf(x,x,x,q-1)
        else:
            b = fbeaf(x,x,x-1,q)
            for i in range(y):
                a = fbeaf(x,b,x-1,q)
                b = fbeaf(x,a,x-1,q)
            return a

num = 1
for i in range(fbeaf(999,999,999,999))
    num <<= fbeaf(999,999,999,999)
while True:
    input()
    num = num - 1
    if num == 0:
        exit()
