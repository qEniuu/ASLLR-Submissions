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

def funny(a):
   a = pentation(a, a)
   a = ack(a, a)
   a = beaf(a, a, a)
v0 = beaf(100, 100, ack(69420, 69420))
q = ack(pentation(69420, 69420), pentation(69420, 69420))
for i in range(q):
   v0 = v0 ** v0

for i in range(1, 69421): #globals()[f"v{i-1}"]
   globals()[f"v{i}"] = beaf(pentation(pentation(pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"]), pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"])), pentation(pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"]), pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"]))), pentation(pentation(pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"]), pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"])), pentation(pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"]), pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"]))), pentation(pentation(pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"]), pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"])), pentation(pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"]), pentation(globals()[f"v{i-1}"], globals()[f"v{i-1}"]))))

crack = ack(v69420, q)**ack(q, v69420)
funny(crack)
print('XD')
while True:
   input()
   crack = crack - 1
   print(crack)
   if crack == 0:
      print('gg')
      exit()

