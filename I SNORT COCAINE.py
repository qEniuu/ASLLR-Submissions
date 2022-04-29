def Ack(m, n):
   if m==0: return n+1
   if m>0 and n==0: return Ack(m-1, 1)
   if m>0 and n>0: return Ack(m-1, Ack(m, n-1))
v0 = 69420
for i in range(69420):
   v0 = v0 ** v0
for i in range(1, 69421):
   globals()[f"v{i}"] = Ack(globals()[f"v{i-1}"] ** globals()[f"v{i-1}"], globals()[f"v{i-1}"] ** globals()[f"v{i-1}"])


while True:
   input()
   v69420 = v69420 - 1
   print(v69420)
   if v69420 == 0:
      print('gg')
      exit()