import random as r
c='abcdefghijklmnopqrstuvwxyz'
cl=list(c)
t=input()
a=t.split(' ')
cd=input('tell me what you want to decode or encode ')

if(cd=="decode"):
    z=0
    for i in range(len(a)):
        if(len(a[i])<3):
            d=a[i]
            if(len(d)==2):
                l=list(d)
                t=l[0]
                l[0]=l[1]
                l[1]=t
                a[i]=(l[0]+l[1])
            elif(len(d)==1):
                continue
        elif(len(a[i])>=9):
            l=list(a[i])
            l=l[3:(len(l)-3)]
            r=l.pop(len(l)-1)
            l.insert(0,r)
            f=''
            for k in l:
                f=f+k
            a[i]=f
        else:
            z=1
            break
    if(z==1):
        print('wrong input to decode')
    else:
        g=''
        for m in a:
            g=g+m
            g=g+' '
        print(g)
elif(cd=="encode"):
    for i in range(len(a)):
        if(len(a[i])<3):
            d=a[i]
            if (len(d) == 2):
                l = list(d)
                t = l[0]
                l[0] = l[1]
                l[1] = t
                a[i]=(l[0] + l[1])
            elif(len(d)==1):
                continue
        elif(len(a[i])>=3):
            l = list(a[i])
            p = l.pop(0)
            l.append(p)
            for j in range(3):
                l.append(r.choice(cl))
                l.insert(0, r.choice(cl))
            f = ''
            for k in l:
                f = f + k
            a[i]=f
    g=''
    for m in a:
        g=g+m
        g=g+' '
    print(g)