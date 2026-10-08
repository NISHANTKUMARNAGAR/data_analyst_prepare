# required arguement( that must be provided with function call)/also called positional arguement

'''def p(n):
    for i in n:
        print(i)

n=input('enter the word to be printed')
p(n)'''

# default arguement(that can be prvided in function definition and
    #work as default when no arguement provided in function call

'''def p(n='seema'):
    for i in n:
        print(i)
p()'''

# keyword arguement (order can be random while calling the function because
                                    #we use the parameters name in function call)

'''def avg(a,b):
    print((a+b)/2)

avg(b=2,a=8)'''

#variable length argaument(* for takes parameter as tuple,** for dictionary)

'''def pr(*t1):
    for i in t1:
        print(i)

pr(7,3,5,4,9)'''
