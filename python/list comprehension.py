#[expression   for item in iterable   if condition]
#[x if x > 5 else 0 for x in nums] #conditional expression
#[x for x in nums if x > 5] #filtering
#[x for x in nums if x > 0 and x % 2 == 0]
#set {x * 2 for x in nums}
#dictionary {key_expression: value_expression for item in iterable}
#dictionary example {x: x**2 for x in range(5)} i.e. {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

x = 2
y = 2
z = 2
n = 2
l1=[]
l1=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
print(l1)

'''when we use range in for loop in python we dont have to write i=i+1 python does it by default
range in for loop by default starts with 0 so dont have to write range(0,5) just range(5) is ok
can also do    l=[]
                        l.append(i)
                        l.append(j)
                        l.append(k)
                        l1.append(l)
                                                as we just have to add new list to output list  we will do
                                                l1.append([i,j,k]) insted of creating new list l and appending
                                                it with i,j,k in 4 lines we will do it  in 1 line'''

'''now to list comprehension we will replace this
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
          if((i+j+k)!=n):
              l1.append([i,j,k])'''

#multiplication table
a=int(input('enter number'))
n=11
l=[a*i for i in range(n) if i>0]
for j in l:
    print(j)

#multiplication table with docstring
a=int(input('enter number'))
n=11
l=[a*i for i in range(n) if i>0]
for j in range(n):
    if(j<n-1):
        print(f"{a} * {j+1} = {l[j]}")

#dictionary comprehension
transactions = [
    ("Alice", "food", 450),
    ("Bob", "travel", 1200),
    ("Alice", "travel", 800),
    ("Charlie", "food", 300),
    ("Bob", "food", 650),
    ("Alice", "food", 250),
    ("Charlie", "travel", 1500),
    ("Bob", "travel", 400),
    ("David", "food", 200),
    ("Charlie", "food", 700),
    ("David", "travel", 900),
    ("Alice", "travel", 300)
]
"""their total spending
their average transaction amount
their highest individual transaction
their transactions that are at least 500
and whether all of their transactions are at least 250"""
from collections import defaultdict
result=defaultdict(list)
{result[item[0]].append(item[2]) for item in transactions}
order=sorted(list(result),key=lambda x:-sum(result[x]))
for item in order:
    print(item)
    print(sum(result[item]))
    print(sum(result[item])/len(result[item]))
    print(max(result[item]))
    print(list(filter(lambda x:x>=500,result[item])))
    print(all(x>=250 for x in result[item]))
    print('\n')