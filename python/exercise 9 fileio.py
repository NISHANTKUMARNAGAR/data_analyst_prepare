p='o.txt'

#question 1
"""f=open(p,'w')
f.write("how i wonder what you are twinkle twinkle little star")
f.close()"""

"""f=open(p,'r')
g=f.read()
h=g.find("twinkle")
print("twinkle is at ",h,"index")"""

#question 2
"""def ifeven(a,b):
    if a%2==0 and b%2==0:
        return 2
    elif a%2==0 or b%2==0:
        return 1
    else:
        return 0

i,j=input("enter two number to find if its even or odd").split()
score=ifeven(int(i),int(j))
f=open(p,'r')
l=f.read()
if l:
    g=int(l)
    f.close()
    if(score>g):
        print("new high score")
        f=open(p,'w')
        f.write(str(score))
        f.close()
    else:
        print("not a new high score")
else:
    print("new high score")
    f=open(p,'w')
    f.write(str(score))
    f.close()"""

#question 3
"""for i in range(2,21):
    l=[]
    f=open(f"tables/{i}.txt",'w')
    for j in range(10):
        l.append(f"{i}*{j+1}={i*(j+1)}")
    for k in l:
        f.write(k+'\n')
    f.close()"""

#question 4
"""f=open(p,'r')
g=f.read()
f.close()
if g:
    h = g.find("donkey")
    if(h!=-1):
        repl=g.replace("donkey","######")
        f=open(p,'w')
        f.write(repl)
        f.close()
        print("donkey replaced")
    else:
        f.close()
        print("no donkey found")
else:
    print("empty file")
    f.close()"""

#question 5
"""l=["donkey","monkey","hello"]
for i in l:
    f = open(p, 'r')
    g = f.read()
    f.close()
    if g:
        h = g.find(i)
        if(h!=-1):
            repl=g.replace(i,"######")
            f=open(p,'w')
            f.write(repl)
            f.close()
            print(f"{i} replaced")
        else:
            f.close()
            print(f"no {i} found")
    else:
        print("empty file")
        f.close()"""

#question 6
"""f=open(p,'r')
g=f.read()
if g:
    if (g.find("python"))!=-1:
        print("contains word python")
    else:
        print("does not contain word python")
else:
    print("empty file")"""

#question 7
"""f=open(p,'r')
i = 1
while True:
    l=f.readline()
    if not l:
        break
    c=l.find("python")
    if(c!=-1):
        print("python is present at index in line",i)
    i=i+1
f.close()"""

#question 8
"""f=open(p,'r')
g=f.read()
f.close()
f=open('copy.txt','w')
f.write(g)
f.close()
f=open('copy.txt','r')
print(f.read())
f.close()"""

#question 9
"""f=open(p,'r')
g=f.read()
f.close()
f=open('copy.txt','r')
h=f.read()
f.close()
if(g==h):
    print("identical content")
else:
    print("non identical content")"""

#question 10
"""f=open(p,'r')
g=f.read()
f.close()
if g:
    print("file not empty")
    f=open(p,'w')
    f.write('')
    f.close()
else:
    print("file empty")"""

#question 11
import os
"""p="C:\\Users\\NISHANT NAGAR\\PyCharmMiscProject\\practice python\\"
if os.path.isfile(p):
    os.rename("copy.txt", "copy.txt")"""

#question 12 sales.txt-----------------------------------------------
"""class NotEnoughFieldsError(Exception):
    pass

class NegativeSalesError(Exception):
    pass

class SalesRecord:
    def __init__(self,i,n,a):
        self.employee_id=i
        self.employee_name=n
        self.employee_amount=a

    def __str__(self):
        return self.employee_id+","+self.employee_name+","+str(self.employee_amount)

try:
    with open("sales.txt",'r') as f:
        data=f.readlines()
        fdata=list(map(lambda x:list(x.rstrip('\n').split(',')),data))
except FileNotFoundError:
    print("File was Not Found")
except PermissionError:
    print("File not accessible :permission denied")
else:
    Invalid=[]
    Valid=[]
    i=1
    for item in fdata:
        try:
            if len(item)!=3:
                raise NotEnoughFieldsError
            emp_id=item[0]
            name=item[1]
            sales=int(item[2])
            if sales<0:
                raise NegativeSalesError
        except NotEnoughFieldsError:
            Invalid.append([i, data[i-1], "all required fields are not provided"])
        except ValueError:
            Invalid.append([i, data[i-1], "sales amount value provided is invalid"])
        except NegativeSalesError:
            Invalid.append([i, data[i-1], "sales amount value provided is negative"])
        else:
            obj=SalesRecord(emp_id,name,sales)
            Valid.append(obj)
        i=i+1

    try:
        with open("valid_sales.txt",'w') as v:
            v.writelines(list(map(lambda x:str(x)+"\n",Valid)))

        with open("invalid_sales.txt",'w') as iv:
            iv.writelines(list(map(lambda x:str(x)+'\n',Invalid)))
    except PermissionError:
        print("not allowed to write")
    else:
        print("total records processed: ",len(fdata))
        print("total valid records processed: ",len(Valid))
        print("total invalid records processed: ",len(Invalid))
        total=0
        for item in Valid:
            total=total+item.employee_amount
        print("total sales amount: ",total)"""


#question 13 --------------------------------------------------
"""from pathlib import Path
p=Path("test_project_data")
data=[
    "The train arrived at the station earlier than expected.",
    "She decided to learn Python after finishing her college assignment.",
    "The weather became pleasant after the rain stopped.",
    "He forgot to bring his notebook to the study session.",
    "We should check the data carefully before drawing any conclusions."
]
if not p.exists():
    Path("test_project_data").mkdir()
else:
    with open("test_project_data\\log.txt",'w') as t:
        t.writelines(list(map(lambda x:x+'\n',data)))

with open("test_project_data\\log.txt",'r') as u:
    sample=u.read(25)
    print(sample)
    print(u.tell())
    u.seek(0)
    sample1=u.read(55)
    print(sample1)

with open("test_project_data\\data.bin",'wb') as v:
    v.write(b"hello")

with open("test_project_data\\log1.txt",'w') as w:
    pass

q=Path("test_project_data\\log1.txt")
q=q.rename("test_project_data\\log2.txt")
print("if renamed file exists",q.exists())
print("if is it a file",q.is_file())
q.unlink()
if q.exists():
    print('it stil exists')
else:
    print('its deleted')

with open("test_project_data/log.txt", "r+") as f:
    f.seek(20)
    f.truncate()

import os

p = Path("test_project_data/log.txt")

print("Readable:", os.access(p, os.R_OK))
print("Writable:", os.access(p, os.W_OK))
print("Executable:", os.access(p, os.X_OK))
"""