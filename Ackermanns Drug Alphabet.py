def Ack(m, n):
   if m==0: return n+1
   if m>0 and n==0: return Ack(m-1, 1)
   if m>0 and n>0: return Ack(m-1, Ack(m, n-1))

thefunny = 1337
for sussy in range(69):
   for sussyy in range(420):
      thefunny = thefunny ** thefunny
      print(thefunny)

a = Ack(thefunny**thefunny, thefunny**thefunny) #these variables are just here to make everything easier
b = Ack(a**a, a**a)
c = Ack(b**b, b**b)
d = Ack(c**c, c**c)
e = Ack(d**d, d**d)
f = Ack(e**e, e**e)
g = Ack(f**f, f**f)
h = Ack(g**g, g**g)
i = Ack(h**h, h**h)
j = Ack(i**i, i**i)
k = Ack(j**j, j**j)
l = Ack(k**k, k**k)
m = Ack(l**l, l**l)
n = Ack(m**m, m**m)
o = Ack(n**n, n**n)
p = Ack(o**o, o**o)
q = Ack(p**p, p**p)
r = Ack(q**q, q**q)
s = Ack(r**r, r**r)
t = Ack(s**s, s**s)
u = Ack(t**t, t**t)
v = Ack(u**u, u**u)
w = Ack(v**v, v**v)
x = Ack(w**w, w**w)
y = Ack(x**x, x**x)
z = Ack(y**y, y**y)


while True:
   input()
   z = z - 1
   print(z)
   if z == 0:
      print("gg")
      exit()
