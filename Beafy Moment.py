def beaf(x,y,z):
    if z == 1:
        return x**y
    result = y
    for i in range(y-1):
        result = beaf(x,result,z-1)
    return result

patty = beaf(10000, 10000, 10000**10000)
seasonedpatty = beaf(patty, patty, patty)
cookedpatty = beaf(seasonedpatty, seasonedpatty, seasonedpatty)
beafypatty = beaf(cookedpatty, cookedpatty, cookedpatty)
while True:
   input()
   beafypatty = beafypatty - 1
   print(beafypatty)
   if beafypatty == 0:
      print('gg')
      exit()
