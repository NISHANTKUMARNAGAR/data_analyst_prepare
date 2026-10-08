#question 1 -------------------------------------------------------------------------------------------------------------

a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
d=int(input("enter 4th number"))

if(a>b):
    if(a>c):
        if(a>d):
            print(a," is greatest")
        else:
            print(d," is greatest")
    elif(c>d):
        print(c," is greatest")
    else:
        print(d,"is greatest")
else:
    if(b>c):
        if(b>d):
            print(b," is greatest")
        else:
            print(d," is greatest")
    elif(c>d):
        print(c," is greatest")
    else:
        print(d,"is greatest")

#question 2 --------------------------------------------------------------------------------------------------------------

m1=int(input("enter 1st subject marks"))
m2=int(input("enter 2nd subject marks"))
m3=int(input("enter 3rd subject marks"))

total=((m1+m2+m3)/300)*100
#as each marks is out of 100 they are in itself a percentage

if(total>=40 and m1>=33 and m2>=33 and m3>=33):
    print("pass")
else:
    print("fail")

#question 3 ---------------------------------------------------------------------------------------------------------------

s=input("enter the text")

if(((s.find("make a lot of money"))!=-1) and ((s.find("click this"))!=-1) and ((s.find("buy now"))!=-1) and ((s.find("subscribe this"))!=-1)):
    print("it is not a spam")
else:
    print("its a spam")

#question 4 ---------------------------------------------------------------------------------------------------------------

n=input("enter your name")

if(len(n)<10):
    print("has less than 10 char")
else:
    print("not less than 10")

#question 5 ---------------------------------------------------------------------------------------------------------------

l1=["nishant","naman","seema"]
na=input("enter a name to check in list")

for i in range(0,3,1):
    if(l1[i]==na):
        print("yes in the list")
        break
    else:
        continue



