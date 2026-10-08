#used string literal
"""for i in range(1,int(input())):
    ele=int('1'*i)
    print(ele*i)
"""

#more than 2 lines of code
"""n=int(input())
for i in range(0,n-1):
    if(i==0):
        final=10**i
        temp=1
    else:
        temp=10**i+temp
        final=temp*(i+1)
    print(final)"""

#more than 2 lines of code
"""for i in range((int(input()))-1):
    if(i==0): final=10**i; temp=1
    else: temp=10**i+temp; final=temp*(i+1)
    print(final)"""

#multiple print
"""for i in range((int(input()))-1):
    if(i==0): print(10**i); temp=1
    else: temp=10**i+temp; print(temp*(i+1))"""

#two line,1 print,no string ,1 for loop code
"""temp = 1
for i in range((int(input())) - 1): final = 10**i if i == 0 else (temp := 10**i + temp) * (i + 1); print(final)
"""
#used walrus operator and if-else in 1 line and removed temp=1 to before for loop

##using previous 1,11,111 to generate 1,121,12321
"""for i in range(1,int(input())+1):
    print(pow(((pow(10,i)-1)//9),2))"""