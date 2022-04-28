import time
a = 69420
aa = 0
b = 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
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
ackerman = 1
ackermana = 1
ackermanb = 1
ackermanc = 1
prevval = 1

def dank():
    for i in range(5):
        global a
        a = a * a 
    a = a ** cage1 ** cage2 ** cage3 ** cage4 ** cage5 ** cage6 ** cage7 ** cage8 ** cage9 ** cage10 ** ackerman ** ackermana ** ackermanb ** ackermanc ** aa ** prevval
    prevval = a

def Ack(m, n):
   if m==0: return n+1
   if m>0 and n==0: return Ack(m-1, 1)
   if m>0 and n>0: return Ack(m-1, Ack(m, n-1))
        
start_time = time.time()
dank()
aa = a
print("Tower Of IF Statements V0.3 (Probably Final) - Really bad coding btw")
print("This program crashes because of the recursion limit, However it can be bypassed")
while True:
        input()
        cage1 = cage1 + 1
        a = a - b
        print(a, cage1, cage2, cage3, cage4, cage5, cage6, cage7, cage8, cage9, cage10, ackerman, ackermana, ackermanb, ackermanc, aa)
        if a < 1:
            dank()
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
                                                    ackerman = ackerman - 1
                                                    if ackerman == 0:
                                                        ackerman = int(Ack(cage1, cage1))                  
                                                        ackermana = ackermana - 1
                                                        if ackermana == 0:
                                                            ackermana = int(Ack(ackerman, ackerman))  
                                                            ackermanb = ackermanb - 1
                                                            if ackermanb == 0:
                                                                ackermanb = int(Ack(ackermana, ackermana))
                                                                ackermanc = ackermanc - 1
                                                                if ackermanc == 0:
                                                                    ackermanc = int(Ack(ackermanb, ackermanb))
                                                                    aa = aa - b
                                                                    if aa < 1:
                                                                        end_time = time.time()
                                                                        le_time = round((end_time - start_time) * 1000)
                                                                        if le_time > 10:
                                                                                print('you lost')
                                                                                exit()
                                                                        print("gg you won")
                                                                        exit() 
