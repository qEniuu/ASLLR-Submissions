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

def beaf(x,y,z):
    if z == 1:
        return x**y
    result = y
    for i in range(y-1):
        result = beaf(x,result,z-1)
    return result

def ack(m, n):
   if m==0: return n+1
   if m>0 and n==0: return ack(m-1, 1)
   if m>0 and n>0: return ack(m-1, ack(m, n-1))    

def powerexpansion(a, b):
    return hyperexpansion(a, b, 3)

def hyperexpansion(a, b, n):
    result = a
    for i in range(b-1):
        if n == 1:
            result = hyper(a,a,result+2)
        else:
            result = hyperexpansion(a, result, n-1)
    return result

def hyper(a, b, n):
    if n == 1:
        return a + b
    result = a
    for i in range(b-1):
        result = hyper(a, result, n-1)
    return result

def booga(n):
    return hyperr(n, n, n)

def hyperr(a, b, n):
    if n == 1:
        return a + b
    result = b
    for i in range(b-1):
        result = hyper(a, result, n-1)
    return result

def explosion(a, b):
    result = a
    for i in range(b-1):
        result = hyperexpansion(a,a,result)
    return result

def beaff(a):
    x = beaf(a,a,69420)
    y = a**x
    return y

def femboy(x,y,z):
    if z == 0:
        if x == 0:
            return y+1
        a = y
        for i in range(y):
            a = femboy(x,a,0)
        return a
    b = y
    for i in range(y):
        b = femboy(x,b,z-1)
    return 

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

def killer(n):
    n = beaff(beaff(beaff(beaff(n))))
    n = femboy(n, n, n)
    n = explosion(n, n)
    n = powerexpansion(powerexpansion(n, n), powerexpansion(n, n))
    n = ack(n, n)
    n = fbeaf(n, n, n, n)
    n = booga(n)

prevval = 1
def funni():
    funnynumber = pentation(183183183, prevval)
    for j in range(powerexpansion(8493028940, 437265423590))
        for i in range(pentation(9999, 9999999)):
            funnynumber = funnynumber + funnynumber
            funnynumber = funnynumber * funnynumber
            funnynumber = funnynumber ** funnynumber
            funnynumber = pentation(funnynumber, funnynumber)
            funnynumber = tetration(funnynumber, funnynumber)
            funnynumber = ack(funnynumber, funnynumber)
            funnynumber = powerexpansion(funnynumber, funnynumber)
            funnynumber = beaf(funnynumber, funnynumber, funnynumber)
            funnynumber = hyperexpansion(funnynumber, funnynumber, funnynumber)
            funnynumber = hyper(funnynumber, funnynumber, funnynumber)
            funnynumber = hyperr(funnynumber, funnynumber, funnynumber)
            funnynumber = booga(funnynumber)
            funnynumber = explosion(funnynumber, funnynumber)
            funnynumber = beaff(funnynumber)
            funnynumber = femboy(funnynumber)
            funnynumber = fbeaf(funnynumber, funnynumber, funnynumber, funnynumber)
    prevval = funnynumber

cage1 = 1
cage2 = 1
cage3 = 1
cage4 = 1
cage5 = 1
cage6 = 1
cage7 = 1
cage8 = 1
cage9 = 1
cage10 = 1
booganum = 1
acknum = 1
pentanum = 1
tetranum = 1
powernum = 1
beafnum = 1
explosionnum = 1
unexpecteddifficultyspike = 1
funni()
thefinal = funnynumber
for i in range(pentation(9999, 9999999)):
    thefinal = femboy(femboy(femboy(femboy(femboy(femboy(femboy(femboy(femboy(femboy(femboy(thefinal)))))))))))
    thefinal = beaff(beaff(beaff(beaff(beaff(beaff(beaff(beaff(thefinal))))))))
print("Tower Of Genocide ----- good luck... you will need it...")
while True:
        input()
        cage1 = cage1 + 1
        funnynumber = funnynumber - 1
        if funnynumber < 1:
            funni()
            while cage2 !=0:
                cage2 = cage2 - 1
                if cage2 == 0:
                    cage2 = cage1
                    cage3 = cage3 - 1
                    if cage3 == 0:
                        cage3 = cage1
                        cage4 = cage4 - 1
                        if cage4 == 0:
                            cage4 = cage1
                            cage5 = cage5 - 1
                            if cage5 == 0:
                                cage5 = cage1
                                cage6 = cage6 - 1 
                                if cage6 == 0:
                                    cage6 = cage1
                                    cage7 = cage7 - 1
                                    if cage7 == 0:
                                        cage7 = cage1
                                        cage8 = cage8 - 1
                                        if cage8 == 0:
                                            cage8 = cage1
                                            cage9 = cage9 - 1
                                            if cage9 == 0:
                                                cage9 = cage1
                                                cage10 = cage10 - 1
                                                if cage10 == 0:
                                                    cage10 = cage1
                                                    booganum = booganum - 1
                                                    if booganum == 0:
                                                        booganum = booga(cage1)
                                                        tetranum = tetranum - 1
                                                        if tetranum == 0:
                                                            tetranum = tetration(cage1, cage1)
                                                            pentanum = pentanum - 1
                                                            if pentanum == 0:
                                                                pentanum = pentation(cage1, cage1) 
                                                                acknum = ackman - 1
                                                                if acknum == 0:
                                                                    acknum = ack(cage1, cage1)
                                                                    powernum = powernum - 1
                                                                    if powernum == 0:
                                                                        powernum = powerexpansion(cage1, cage1)
                                                                        beafnum = beafnum - 1
                                                                        if beafnum == 0:
                                                                            beafnum = beaf(cage1, cage1, cage1)
                                                                            explosionnum = explosion - 1
                                                                            if explosionnum == 0:
                                                                                explosionnum = explosion(cage1, cage1)
                                                                                unexpecteddifficultyspike = unexpecteddifficultyspike - 1
                                                                                if unexpecteddifficultyspike == 0:
                                                                                    death = femboy(pentation(cage1, cage1), pentation(cage1, cage1), pentation(cage1, cage1))
                                                                                    hell = powerexpansion(beaff(beaf(death, death, death)), beaff(beaf(death, death, death)))
                                                                                    murder = hell
                                                                                    for i in range(hell):
                                                                                        killer(murder)
                                                                                    unexpecteddifficultyspike = murder
                                                                                    thefinal = thefinal - 1
                                                                                    if thefinal == 0:
                                                                                        print("YOU DESTROYED THE TOWER OF GENOCIDE!!!")
                                                                                        exit()


