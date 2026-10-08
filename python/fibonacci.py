#without recursion -------------------
'''cube = lambda x: x*x*x

def fibonacci(n):
    a=0
    b=1
    l=[]
    for i in range(n):
        l.append(a)
        a=b
        b=a+b
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))'''

#with recursion -------------------------
'''cube = lambda x:x*x*x

def origfibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return origfibo(n-1)+origfibo(n-2)

def fibonacci(n):
    l=[]
    for i in range(n):
       l.append(origfibo(i))
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))'''

#memoization using dictionary to give fibonacci hnumber at a given index
#can make this using iterative approach too
"""def fib(n, dp={}):
    if n in dp: #if the index of fibonacci already present in dictionary give it directly
        return dp[n]
    if n <= 1: #if n=0 or 1 give that number directly
        return n
    dp[n] = fib(n-1) + fib(n-2) #if not above cases calculate it recursively and store it
    return dp[n] #just give that fibnacci0_number=dictionary[fibonacci index]
"""