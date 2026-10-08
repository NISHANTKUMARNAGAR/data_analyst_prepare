n=11  #can be only odd
p='H'
p1='H'
q=n*p
v='i'
c=int(n/2)
hh=c+1
bh=n+1
space=' '
lastp=''

wh=len(c*space+q+(n*3)*space+q+c*space)
ch=wh-2*(len(c*space))
h=ch*p

spa=1+(n-1)*2

for i in range(n):
  print(p.center(spa,' '))
  if(i==n-1):
      lastp=p
  p=p+'HH'

b=c*space+q+(n*3)*space+q
for i in range(bh):
  print(b)

for j in range(hh):
    print(h.center(wh,' '))

b=c*space+q+(n*3)*space+q
for i in range(bh):
  print(b)

while(n>0):
    print((lastp.center(spa,' ')).rjust(wh))
    n=n-1
    lastp=p1+p1*((n-1)*2)
