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

x = 9753623592376853787**77626612700943763392363247943871
y = 736198346756**3597914465626576582461001998236453678
clicks = pentation(x, y)
while True:
    input()
    clicks = clicks - 1
    print(clicks)
    if clicks == 0:
        print("gg you have beaten pentation moment")
        exit()
