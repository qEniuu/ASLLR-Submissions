def multiexpansion(a, b):
    result = a
    for i in range(b-1):
        result = expansion(a, result)
    return result

def expansion(a, b):
    result = a
    for i in range(b-1):
        result = hyper(a, a, result + 2)
    return result

def hyper(a, b, n):
    if n == 1:
        return a + b
    result = a
    for i in range(b-1):
        result = hyper(a, result, n - 1)
    return result

lolz = multiexpansion(99999**99999, 99999**99999)
lmfao = multiexpansion(lolz**lolz, lolz**lolz)
bruh = multiexpansion(lmfao**lmfao, lmfao**lmfao)
while True:
    input()
    bruh = bruh - 1
    print(bruh)
    if bruh == 0:
        print("gg")
        exit()