a = 0
b = 0
c = 1
d = 0
z = 0
print("NumberExperimentationAlpha made by Eniuu/uuine")
while True:
    a = a + 1
    if a == 100000000:
        z = z + 1
        a = 0
        b = b + 1
    elif b == 100000000:
        b = 0
        c = c - 1
        if c == 0:
            c = z
            d = d + 1
    print("wynik", a, '|', b, '|', c, "|", z, "|", d)
    if d == 100000000:
        break
print('Finished!')
