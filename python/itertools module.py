import itertools

#-----------------------------for itertools.count
"""for i in itertools.count(1,1):
    if(i>10):
        break
    print(i)"""

#------------------------------for itertools.cycle
#colors=['red','yellow','blue']
"""for i,c in zip(itertools.count(1,1),itertools.cycle(colors)):
    if(i>7):
        break
    print(c)"""
"""for _,c in zip(range(7),itertools.cycle(colors)):
    print(c)"""

#-----------------------------for itertools.repeat
"""for x in itertools.repeat(1,5):
    print(x)"""

#--------------------------for itertools.combination
"""numbers=[1,2,3]
print(list(itertools.combinations(numbers,2)))"""
#to print all length combinations in separate lines
"""s=['3','1','2']
k=3
for i in range(1,int(k)+1):
    print(*map("".join,itertools.combinations(sorted(s),i)),sep="\n")"""

#---------------for itertools.combinations_with_replacement
"""items=[1,2,3]
print(list(itertools.combinations_with_replacement(items,2)))"""

#----------------------------------for itertools.permutation
"""numbers=[1,2,3]
print(list(itertools.permutations(numbers,2)))"""
#to print them in separate lines
"""alpha=["a","b","c"]
print(*map("".join,itertools.permutations(sorted(alpha),2)),sep="\n")"""
#it applies sorted over alpha to get lexicographic order and then join by
#"" i.e. empty space to join permutation tuple's values without any inverted
#comma and this join is applied for each tuple by map method which takes
#iterable and in this iterable is all tuples of permutations function
#and finally the joined by "" permutation tuples are unpacked by *

#-------------------------------for itertools.product
#without repeat
"""n1=[1,2]
n2=[3,4]
n3=[5,6]
print(list(itertools.product(n1,n2,n3)))"""
"""A=[[1,2,3],[3,4,5]]
print(list(itertools.product(*A)))"""
#can also print A one by * unpacking
"""A=[[1,2,3],[3,4,5]]
print(*itertools.product(*A))"""
#or by join
"""A=[[1,2,3],[3,4,5]]
print(" ".join(map(str,itertools.product(*A))))"""
#with repeat
"""n1=[1,2]
n2=[3,4]
print(list(itertools.product(n1,n2,repeat=2)))"""

#----------------------------------for itertools.groupby
"""data="AAAABBBCCDAAPOP"
for key,group in itertools.groupby(data):
    print(key,list(group))"""

#------------------------------for itertools.chain
"""a=[1,2,3]
b=[4,5]
c=[6,7,8]
print(list(itertools.chain(a,b,c)))"""

#-----------------------------for itertools.islice
"""#itertools.islice(iterable, start, stop, step)
for i in itertools.islice(range(100), 10, 20, 2):
    print(i)"""

#------------------------------for zip_longest
"""#runs till longer iterable has value unlike zip
a = [1, 2, 3]
b = ["a", "b"]
#itertools.zip_longest(a, b, fillvalue=None)
for i in list(itertools.zip_longest(a, b, fillvalue="-")):
    print(i)"""

#------------------------------for compress
"""data = ["A", "B", "C", "D"]
selectors = [1, 0, 1, 0]
print(list(itertools.compress(data, selectors)))"""

#------------------------------for filterfalse
#gives values for which filter says false
"""print(list(itertools.filterfalse(lambda x: x > 5, [2, 6, 3, 8, 4])))"""

#------------------------------for takewhile
"""#allows elements into result till condition is true
print(list(itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 7, 2])))
#condition false at 7 so it stops and did not check after 7"""

#------------------------------------for dropwhile
"""#drops while condition is true,opposite to takewhile
print(list(itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 7, 2])))"""

#--------------------------------------for accumulate
"""#calculate running sum
print(list(itertools.accumulate([1, 2, 3, 4])))"""

#------------------------------------for starmap
"""#applies function to every item in iterable
data = [(2, 3), (4, 5), (6, 7)]
def add(a,b):
    return a+b
for i in itertools.starmap(add, data):
    print(i)"""

"""   good hackerrank question 1   """
#find probability of at least one 'a' inside any combination tuple
"""from itertools import combinations
n=9
s=['a','b','c','a','d','b','z','e','o']
k=4
combtup=list(combinations(s,k))
print(combtup)
favout=0
for i in range(len(combtup)):
    if((("".join(combtup[i])).count("a"))>0):
        favout=favout+1
print(favout/len(combtup)) #probability=favorable outcome/total outcome"""

"""   good hackerrank question 2   """
# given few lists,From each list, pick one element such that the sum of their squares
# gives the maximum possible remainder when divided by M.
#noflist=K
#divisor=M
#lenoflist=N
"""noflist,divisor=map(int,input().split())
prodlist=[]
for _ in range(noflist):  #"_" as those variables are not needed
    _,*numblist=map(int,input().split())
    prodlist.append(numblist)

#comblist=list(product(*prodlist)) #avoid building huge list in memory
sumoflist=0
maxrem=0
for currenttuple in (itertools.product(*prodlist)):  #diectly take tuples from product(*prodlist) iterable
    for j in range(len(currenttuple)):
        sumoflist=sumoflist+currenttuple[j]**2
    rem=sumoflist % divisor
    if(rem>maxrem): #check if calculated reminder is larger than previous one
        maxrem=rem
    sumoflist=0

print(maxrem)"""

#question 3 ---------------------------------------------
"""
#Treat all three streams as one continuous transaction stream.
#Consider only transactions whose amount is not negative.
#Process the resulting transactions in their original order.
#From that stream, take only the first 5 transactions.
#Produce the running total of the transaction amounts.
#The final output should therefore be an iterator whose values are:
#120
#200
#250
#450
#520

import itertools
online=[("A", 120),("B", 80),("A", 50),]
store=[("C", 200),("A", 70),("B", 40),]
refunds=[("A", -30),("C", -50),]

cont=itertools.chain(online,store,refunds)
onlypost=itertools.filterfalse(lambda x:x[1]<0,cont)
onlynum=itertools.starmap(lambda x,y:y,onlypost)
n=1
for i in itertools.accumulate(onlynum):
   if n>5:
        break 
   print(i)
   n=n+1
"""

#question 4----------------------------------------------------------
"""import itertools
groups=[[10, 20, 30],[5, 15],[100, 200, 300],]
#Create a lazy iterator that produces every possible
# combination of taking one value from each group, 
# but only keep combinations whose sum is greater than 150.
#For each remaining combination, output its sum.

allcomb=itertools.product(*groups)
sumcomb=itertools.starmap(lambda x,y,z:x+y+z,allcomb)
print(list(itertools.filterfalse(lambda a:a<=150,sumcomb)))"""