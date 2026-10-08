#question 1

'''def max(a,b,c):
    if(a>b):
        if(a>c):
            print('a is max')
        else:
            print('c is max')
    else:
        if(b>c):
            print('b is max')
        else:
            print('c is max')

max(3,6,4)'''

#question 2

'''def celtofar(a):
    f=(a*(9/5))+32
    return f
    
far=celtofar(0)
print(far,end=' is the temp in fahrenheit')'''

#question 3 => by using end=''         example print('hi',end='')

#question 4

'''def sumofn(a):
    if(a==1):
        return 1
    elif(a==0):
        return 0
    else:
        return a+ sumofn(a-1)

sum=sumofn(50)
print(sum)'''

#question 5

'''def star(n):
    for i in range(n):
        for j in range(n-i):
            print('*',end='')
        print('')
        
star(3)'''

#questopn 6

'''def inchtocm(n):
    cm=n*2.54
    print(cm)
    
inchtocm(6)'''

#question 7

'''l=['  mango  ','banana','apple']
print(l)
p=(l.pop(0)).strip()
print(p)
print(l)'''

#question 8

'''def table(n):
    for i in range(10):
        if(i==9):
            print(n,'*',i+1,'=',(n*(i+1)))
        else:
            print(n,'*',i+1,'  =',(n*(i+1)))

table(5)'''
