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

def pentation(a, b):
    result = 1
    for i in range(b):
        result = tetration(a, b)
    return result

def tetration(a, b):
    result = 1
    for i in range(b):
        result = a ** result
    return result

def powerofdeath(a, b):
    for i in range(b):
        a = a ** a

def tetraofdeath(a, b):
    for i in range(b):
        a = tetration(a, a)

def pentaofdeath(a, b):
    for i in range(b):
        a = pentation(a, a)

def destroy(a):
    for k in range(a):
        for j in range(a):
            for i in range(a):
                a = tetration(a, a)
            for i in range(a):
                a = pentation(a, a)
            for i in range(a):
                a = powerofdeath(a, a)
            for i in range(a):
                a = tetraofdeath(a, a)
            for i in range(a):
                a = pentaofdeath(a, a)
            for i in range(a):
                a = fbeaf(a, a, a, a)

num = fbeaf(9, 9, 9, 9)
for s in range(destroy(num)):
    for z in range(num):
        for x in range(num):
            for c in range(num):
                for v in range(num):
                    for b in range(num):
                        for n in range(num):
                            for m in range(num):
                                for l in range(num):
                                    for k in range(num):
                                        num = destroy(num)

while True:
    input()
    print(num)
    num = num - 1
    if num == 0:
        exit()
