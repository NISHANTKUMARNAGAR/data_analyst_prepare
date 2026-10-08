#map
"""l=list(map(int,input().split()))
print(l)
ones=[1,2,3]
tens=[11,12,13]
print(list(map(lambda x,y:(x+y),ones,tens)))
"""

#filter
"""n=[1,2,3,4,5,6]
print(list(filter(lambda x:x%2==0,n)))"""

#zip
"""iter1=[1,2,3,4,5]
iter2=['a','b','c','d','e']
print(list(zip(iter1,iter2)))
t=[iter1]+[iter2] #making nested list in iter1,iter2 each containing 1 element ,if put in t by adding it makes 1 list
print(list(zip(*t))) #unpacking list t by * which contains multiple list that will be input to zip()
#if any iterable is smaller then zip truncates i.e. removes elemtents ffrom bigger list to match smaller ones size
names = ["A", "B", "C"]
marks = [80, 90, 70]
print(dict(zip(names, marks)))
"""
#zip usage in transpose
"""matrix = [
    [3, 7, 2, 9],
    [5, 1, 8, 4],
    [6, 3, 7, 2],
    [9, 5, 1, 6]]
rev_sort=[sorted(item,key=lambda x:-x) for item in matrix]
rem_lar=[item[1:] for item in rev_sort]
final=[]
for i in list(zip(*rem_lar)):
    final.extend(i)
print(final)"""

#enumerate
"""fruits=["apple","banana","mango"]
for i,val in enumerate(fruits,start=1):
    print(i,val)"""

#any
"""test=[-3,-1,4,5]
print(any(test))
any([])   # False #nothing is true
"""

#all
"""test1=[0,-1,2]
print(all(test1))
all([])   # True #nothing can be false as its empty
"""

#------hackerrank built in any/all challange---**
#without any,all and with loops
"""n = int(input())
l = list(input().split())
print(l)
p = 0
pos = 0

def chkpalin(num):
    # checking palindrome
    if (''.join(reversed(num)) == num):
        return True

for item in l:  # for +ve and palindrome check
    if (int(item) == abs(int(item))):  # item is +ve
        pos = pos + 1
    else:  # item is negative
        break
    if (chkpalin(item)):  # if item is palindrome
        p = 1

if (pos == n):  # check if all are +ve
    if (p == 1):
        print(True)
    else:
        print(False)
else:
    print(False)"""
#with any all and genreator function to save time,space
"""n=int(input())
l=list(input().split())
pos=0

def chkpalin(num):
  #checking palindrome
  if(''.join(reversed(num))==num): #using reversed() works for any iterator
    return True

#if(all([int(item)>0 for item in l])): #list comprehenion more time,space consumed
if(all(int(item)>0 for item in l)): #generator function less time and space used
  # check if all positive
  pos=1
  #if(any([chkpalin(item) for item in l])): ##list comprehenion more time,space consumed
  if(any(chkpalin(item) for item in l)): #generator function less time and space used
    #if any palindrome
    print(True)
  else:
    print(False)
else:
  print(False)"""

#sorted
"""t=[('a',1),('a',2),('a',3),('a',4)]
print(sorted(t))
t=[('a',1),('c',2),('d',3),('b',4)]
print(sorted(t))
t={2:"b",1:"a"}
print(sorted(t))
print(sorted(["orange","kiwi","apple"],key=len,reverse=False))"""

#-------hackrrank athelete sort challange-------
# by using key in a nested list i.e. list in list then sorting all these sublists using key to get 1
# specific index value from every sublist then arranging or sorting them based on this index and to get
# this index we used a function to get this index value which sorted() applied on every sublist and
# after getting these values sorted() function  did sorting of these values and it also handles similar
# values and ensures insertion order .(for more information check athelete sort challange on hackerrank
# in python's "built-in" section
"""n,m = map(int,input().split()) #no. of athelete,attributes
athedata = []
for _ in range(n): #to take athelete data
  #done rstrip to remove nextline character
  athedata.append(list(map(int, input().rstrip().split())))
k = int(input()) #attribute to be arranged by(0 indexed)

def findattr(item): #to get that specific attr. value
    global k
    return item[k]

#key finds that specific attr. value for every player then that's sorted by this function
 #sorted() then it returns list i.e. players data based on that sorting plus it retains
  #input order so if two players have same value on that attribute we dont have to worry about that 
sorted_data=sorted(athedata,key=findattr) #sorted() takes a func in 2nd arguement thats why func. findattr is used
for item in sorted_data: #printing sorted by that attribute
  print(" ".join(map(str,item)))"""

#if dont want to sort by sorted() in above data use bubble sort()
"""for i in range(n):
    for j in range(n - i - 1): #as i increases one element gets sorted each time , n-i and -1 for indexing as j from 0
        if athedata[j][k] > athedata[j + 1][k]: #only exchange if current greater than next one(doesnt swap for equal)
            athedata[j], athedata[j + 1] = athedata[j + 1], athedata[j]
"""
#can also put labda function in place to findattr() i.e.sorted(athedata,key=lambda sublist: sublist[k])

#sum
"""print(sum([1,2,3],start=0))
print(sum([1,2,3],start=10))"""

#min
"""print(min([1,2,3]))
print(min(['a','b','c']))
p=[]
print(min(p,default=0)) #if iterable empty
"""

#max
"""print(max([1,2,3]))
print(max(['a','b','c']))
p=[]
print(max(p,default=0)) #if iterable empty
"""

#eval
"""p="x**3 + x**2 + x + 1"
x=1
print(eval(p))"""

#--------------hackerrank input challange-------
#handle a polynomial if p(x)==k print True else False
"""p="x**3 + x**2 + x + 1"
x, k = map(int, input().split())  # variable,final value
print("x:",x)
print("k:",k)
pitems = list(map(str.strip, p.split(" ")))  # polynomial
print(pitems)
value = 0

for i in range(len(pitems)):  # calculate value of polynomial
    if (pitems[i]!="-") and (pitems[i]!="+"): #for not signs
        if ("x**" in pitems[i]): #cases if coeff 1 or not 1 with power
            if (pitems[i].startswith("x**")): # if item in p is having coeff not written i.e. by default 1 ex. x**4
                part = x ** int((pitems[i])[3:len(pitems[i])]) #indexing item to get raising value
                print("raisedpowernot1:",part)
            else: #if coeff from 1 to limit of int in python ,it also takes when written 1 as above if does not handle that ex. 1*x**4 or 5*x**1
                coeff=""
                for j in pitems[i]: # to get integer coeff by taking j till we encounter *
                    if (j=="*"):
                        break
                    coeff = coeff+j
                # now to calculate value of item with coeff other than 1 and with raised power
                # raising power is calculated by indexing item from after ** to end of pitem[i]
                part =int(coeff) * x ** int((pitems[i])[((pitems[i]).find("x"))+3:len(pitems[i])])
        elif (pitems[i].endswith("x")):
            # if item in p is having coefficeint 1 to limit of int in python and no power raising ex. 5x,1x,x
            if(pitems[i]=="x"): # for sepcifically x
                part=x
            else: # for if item ends in x but has a coeff like ex 1x,2x etc
                part = int((pitems[i])[0:len(pitems[i])-1])*x
            print("coeff1:",part)
        else:
            # if item is just a number ex. 3
            print(pitems[i])
            part = int(pitems[i])
            print("normal:",part)

        #below if and elif for 1st item in pitems
        if(i==1): #if for 1st item there is -sign then enter cuurent if and enounter this if
            value = value - part
        elif(i==0): #if for 1st item there is +sign then enter cuurent if and enounter this if
            value = value + part
        else: #for other items
            if(pitems[i-1]=="+"): #if + before current item
                value = value + part
            else: #if - before current item
                value = value - part

print(value)
if (value == k):
    print(True)
else:
    print(False)"""

#len
"""print(len([1, 2, 3]))
print(len("hello"))
print(len({"a": 1, "b": 2})) #for dict it counts keys"""

#isinstance()
# -- diff then type(x) becoz it will give true if we have class animal and class horse inherits from it
# then if we do isinstance(object_of_horse,class animal) --> true as i will see does horse belong to animal
# or not but type(object_of_horse,class animal) --> False as it checks immediate class
"""x=4
print(isinstance(x, int))"""

#id()
"""x=4
print(id(x))"""

#divmod()
"""print(divmod(17, 5)) #returns (quotient,remainder)"""

#reduce()
"""from functools import reduce
nums=[1,2,3,4,5,6]
print(reduce(lambda x, y: x + y, nums))"""