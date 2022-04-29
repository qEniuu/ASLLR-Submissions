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

make = powerexpansion(9999999999, 9999999999)
gay = powerexpansion(make**make, make**make)
femboy = powerexpansion(gay**gay, gay**gay)
sex = powerexpansion(femboy**femboy, femboy**femboy)
while True:
    input()
    sex = sex - 1
    print(sex)
    if sex == 0:
        print("gg")
        exit()