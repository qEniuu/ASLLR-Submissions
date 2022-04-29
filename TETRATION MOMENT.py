def tetration(a, b):
    result = 1
    for i in range(b):
        result = a ** result
    return result

z = 10**5000
x = 83278323**18446744073709551615

clicks = tetration(z, x)
while True:
    input()
    clicks = clicks - 1
    print(clicks)
    if clicks == 0:
        print("gg you have beaten tetration moment")
        exit()