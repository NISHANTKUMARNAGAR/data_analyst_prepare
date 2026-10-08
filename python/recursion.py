#sum of first n numbers
'''def sumofn(a):
    if(a==1):
        return 1
    elif(a==0):
        return 0
    else:
        return a+ sumofn(a-1)

sum=sumofn(50)
print(sum)'''

#factorial of number n
'''def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

factorial=fact(5)
print(factorial)'''

#fibonacci series without any loop with recursion in n>=4
'''def fibo(n):
    if(n<=0):
        return []
    elif(n==1):
        return [0]
    elif(n==2):
        return [0,1]
    else:
        s=fibo(n-1) #creates a list with fibo(n-1)
        s.append(s[-1]+s[-2])   #adds a new number with addition of last 2 number of list
        return s

print(fibo(3))'''
#fibnacci series using for loop with recursion
'''def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input('enter how many number of series to be printed'))
if(n<0):
    print('enter positive number')
elif(n==0):
    print('entered zero thats why no output')
else:
    for i in range(n):
        print(fibo(i))'''




