#-----------------------counter--------------------
"""from collections import Counter
#iteration order of counter is how elements appear in orignal input of counter()
print(Counter(['b','b','a','c','c','c']))
print(Counter({'a':3,'b':9}))
print(Counter(a=2,b=5))
c=Counter("abcdd")
print(c.most_common(2)) #top 2 most common
print(c.most_common()) #all char count in decreasing"""

#hackerrank question company logo "tough question" IMPORTANT
"""from collections import Counter

s = input().strip() #to get company name in s
c = Counter(s) # to get counts of aphabetical characters in c

sorted_items = sorted(c.items(), key=lambda x: (-x[1], x[0]))
#here basically c would be a dictionary as counter(s) would return a dictionary and
#in c.items would be containing tuples of like ('a',3),('b',4) etc so now here in lamda
#function for a tuple ('a',3) will be x,here x[0]='a' and x[1]=3 so when we write
#(-x[1],x[0]) it will be (-counter,character) we have done this because now, normally,
#what would happen is if we have different counts, like 4 and 5 but we would want in
#our actual output to have the bigger count come before than the smaller one. And
#but this sorted function will sort them by 4 and then 5. And we want the opposite.
#That is why we adding a minus to it,i.e minus to the counter, so that we would have the 5 first.
#And then 4 which and then sorted will work by sorting those actual, bigger count first,
#because they have minus. And then if some have the similar count, it will absolutely look
#to the next value of the tuple Sort the alphabets alphabetically, which would have the similar counts.
#so So sorted does actually first applies the key function and then sorts it. thats why it would first
#create (-count,character) pairs of all then sort accoring to these pairs

for char, count in sorted_items[:3]:
    print(char, count)
"""

#counter also works on list
"""words = ["apple", "banana", "apple", "orange",
         "banana", "apple", "grape", "orange",
         "banana", "grape", "grape" ]

from collections import Counter
print(Counter(words).most_common(2))"""

#----------------ordered dictionary(OrderedDict)----------
"""from collections import OrderedDict
print("This is a ordered dict")
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=6
od['e']=9

for key,value in od.items():
    print(key,value)

od.pop('a') #deleting
od['a']=1 #re-insertion ,will appear at last

print("\nafter insertion")
for k,v in od.items():
    print(k,v)

#to move particular key to end
od.move_to_end('c')
print(od)
#pop items from left or right ends
od.popitem(last=False) #pops first item
od.popitem(last=True)  #pops last item
print(od)
#also orderedDict like([('a',2),('b',1)]) is not same as
#orderedDict like([('b',1),('a',2)]) if we check them by
#== will give false as ordereddict ensures insertion order"""

#------------------default dictionary(defaultdict)-------
"""from collections import defaultdict
#for a default dictionary with factory function int
intd=defaultdict(int)
L=[1,2,3,4,2,3,1,5]

for i in L:
    intd[i]=intd[i]+1
    #here we dont have to check if that key is in
    #dict or not as defaultdict creates that key
    #gives it a value 0 as value of int() is 0
    #hence first time we acess it its default value is 0
    #thats why it did not give error

print(intd)
print(dict(intd))

print("\n")
#for a default dictionary with factory function list
listd=defaultdict(list)
for i in range(5):
    listd[i].append(i)
    #here same as above create empty list for every
    #key and appending i value to it

print(listd)
print(dict(listd))"""

#------------------------------NamedTuple----------------
"""from collections import namedtuple

#declaring namedtuple
firstnamedtuple=namedtuple("student",['name','age'])

#adding values
s=firstnamedtuple("nishant",'19')

print(s)
print(s[0],"using index")
print(s.name,"using feild name")

#_make() function make namedtuple from iterable
l=["naman","20"]
print("\nusing iterable ",firstnamedtuple._make(l))

#_asdict() creating ordereddict from namedtuple
print("\nusing namedtuple ",s._asdict())"""

#-------------------------deque-----------------------
"""from collections import deque
d=deque([1,2,3])
print(d)
d.append(4)
d.appendleft(0)
print(d)
e=d.pop()
f=d.popleft()
print(d)
print(e)
print(f)
print("\nprinting elements of deque")
for i in d:
    print(i)"""

# hackerrank question piling up
"""from collections import deque
t=int(input())
final=[]
for _ in range(t): # loop for each testcase
    n=int(input())
    d=deque(map(int,input().split()))
    if(len(d)==1): #the is only 1 element in the deque
        final.append("Yes")
        continue
    else:  #if more than 1 element in deque
        ini=(2**31)+1 #maximum possible value in hackerrank +1 to check less than
        while(True): #loop for checking in given list in single testcase
            if(len(d)==1): #if initially more than 1 but after operations last one 1 remains
                if((remain:=d.pop())<=ini):
                    final.append("Yes")
                    break
                else:
                    final.append("No")
                    break
            else: #initially more than 1 case whole loop
                right=d.pop()
                left=d.popleft()
                if(left>=right): #left bigger
                    d.append(right) #giving back the unused value to deque
                    if(left<=ini):
                        ini=left
                    else:
                        final.append("No")
                        break
                else: #right bigger
                    d.appendleft(left) #giving back the unused value to deque
                    if(right<=ini):
                        ini=right
                    else:
                        final.append("No")
                        break

for item in final:
    print(item)"""

#------------------------------chainmap--------------------
"""from collections import ChainMap
d1={2:4,3:9}
d2={2:8,3:27}
c=ChainMap(d1,d2)

#acessing key,values of new ChainMap
print(c)
print(c.keys())
print(c.values())

print("printing keys")
for i in c.keys():
    print(i)
print("printing values")
for j in c.values():
    print(j)
#values of first dictionary is printed if the keys overlap
#if not
print("\n")
d3={4:16,5:25}
d4={6:216,7:343}
c2=ChainMap(d3,d4)

print(c2)
print("printing keys")
for k in c2.keys():
    print(k)
print("printing values")
for k in c2.values():
    print(k)

#adding new dictionary to ChainMap
d5={"a":"b","e":"f"}
c3=c2.new_child(d5)
print("new ChainMap",c3)
print(c3[4])"""