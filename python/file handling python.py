#open('o.txt','x')
n='o.txt'

"""f=open(n,'w')
f.write('hello')"""

"""f=open(n,'r')
print(f.read())"""

"""f=open(n,'a')
f.write('world')
f.close()"""

"""with open(n,'w') as p:
    p.write('hello world')"""

"""f=open(n,'r')
c=f.readlines()
print(c)
f.close()
"""

"""f=open(n,'r')
while True:
    l=f.readline()
    if not l:
        break
    l1=l.rstrip('\n')
    print(l1)
f.close()"""

"""f=open(n,'r') #when we know how many lines
for i in range(4):
    l=f.readline()
    l1=l.rstrip('\n')
    print(l1)
f.close()"""

"""f=open(n,'w')
f.writelines(['hello ','world ','is ','mine'])
f.close()"""

"""f=open(n,'w')
l=['i am learning python','i am learning file handline','i am using harry course']
for i in l:
    f.write(i+'\n')
f.close()"""

"""with open(n,'r') as f:
    f.seek(5)
    print(f.read())
    f.seek(0)
    print(f.read())"""

"""g=open('p.txt','w')
g.write('hello')
print(g.tell())
g.close()"""

"""with open('p.txt','r') as g:
    g.seek(4)
    print(g.read())"""

"""g=open('p.txt','w')
g.write('helloiamnishnt')
g.truncate(5)
g=open('p.txt','r')
print(g.read())"""

"""h=open('l.txt','w')
h.write("to be deleted")
h.close()"""

"""import os
#os.rename("l.txt","k.txt")
#os.rename("k.txt","containsmodule/j.txt")
#os.remove("containsmodule/j.txt")"""