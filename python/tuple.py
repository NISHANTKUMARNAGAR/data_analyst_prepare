#tuples are always enclosed in curved brackets
#tuples are not changable they are permanent creations
t3=() #empty tuple
t4=(7,) #we have to add comma otherwise if only t4=(7) it will consider it as integer
t5=(9)
print(type(t5))
t1=(3,5,2,43,5,13,23)
print(t1)
'''t1[0]=9''' #tuples are non changable so item assignment is not allowed
print(t1[0:2])
print(t1[-2])

if 3 in t1:
    print('3 present')
if 'name' in t1:
    print('name present')

#tuple operations

print(t1.index(5))    #gives first occurence
'''print(t1.index(99))'''  #index gives valueerror if not found
print(t1.count(0))    #gives number of appearences of that item in that tuple
print(len(t1))

t2=[3,6,3,5,6,2,64,6,43]
l2=list(t2) #we can convert tuple to list to do any list operations that tuple cant do like
                #append,extend,sort etc as tuple is not changable ,then
                #we change that list back into tuple
l2.append(99)
l2.sort()
l2.reverse()
l2.insert(0,'naman')
print(l2)
t2=tuple(l2)

#hashing a tuple
n=5
s=input()
l=[]
for i in range(0,2*n,2):
    l.append(int(s[i]))

print(l)
'''t=tuple(l)
print(t)
print(hash(t))'''
