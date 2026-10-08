#question 1

'''n=int(input("enter the number which we want table of "))
i=1
for i in range(1,11):
    if(i==10):
        print(n,'*',i,'=',n*i)
    else:
        print(n,'*',i,'  =',n*i)'''

#question 2

'''l1=['harry','sachin','sohan','rahul']
for i in l1:
    if(i.startswith('s')):
        print(i)'''

#question 3

'''n=int(input("enter the number  have to write multiplication table of "))
i=1
while(i<11):
    if(i==10):
        print(n,'*',i,'=',n*i)
    else:
        print(n,'*',i,'  =',n*i)
    i=i+1'''

#question 4

'''i=int(input("enter the number to be checked"))
n=2
if(i==1):
    print("number is neither prime nor composite")
elif(i==4):
    print("number is not prime")
else:
     for n in range(n,(i//2)):
        if((i%n)==0):
            print("number is not prime")
            break
     else:
         print("number is prime")'''

#question 5

'''n=int(input("enter the number until which i have to find sum till"))
i=1
sum=0
while(i<n+1):
    sum=sum+i
    i=i+1
print(sum)'''

#question 6

'''i=int(input('enter the number to find factorial of'))
f=1
if(i==0):
    print("factorial is 0")
else:
    for j in range(1,i+1):
        f=f*j
print(f)'''

#question 7

'''n=3
for i in range(n):
    j=2
    for j in range(j-i,0,-1):
        print('  ',end='')
    for k in range((2*i)+1):
        print('*',end='')
    print('')'''

#question 8

'''n=3
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print('')'''

#question 9

'''n=10
for i in range(n):
    if(i==0 or i==n-1):
        for j in range(n):
            print('*',end='')
    else:
        print('*',end='')
        for k in range(n-2):
            print('  ',end='')
        print('*',end='')
    print('')'''
            
#question 10

'''n=int(input("enter the number which we want table of "))
i=1
for i in range(1,11):
    if(i==10):
        print(n,'*',(11-i),'=',n*(11-i))
    else:
        print(n,'*',(11-i),'  =',n*(11-i))'''
