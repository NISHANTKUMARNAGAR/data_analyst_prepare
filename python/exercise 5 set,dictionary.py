#question 1
'''translate={}
for i in range(3):
    hindi,english=input().split()
    translate[hindi]=english
print(translate)
n=input("enter the word in hindi to find english transaltion ")
print(translate.get(n))'''

#question 2
'''s=set()
print('enter eight numbers')
for i in range(8):
    s.add(int(input()))
print(s)'''

#question 3
#yes we can as 18 and '18'  are of different types meaning they are different items

#question 4
#length will be 2 as 18 and 18.0 (18.1 or anything other than 0 would be different i.e. float not int) are same but '18' is different
'''s={18,18.00,18.5,'18'}
print(s)'''

#question 6
'''friend={}
for i in range(4):
    name,lang=input().split()
    friend[name]=lang
print(friend)'''
#if names of two people are same then dictionary will update the value given in later name value input and replace previous one
#dictionary will have uniques keys but can have multiple values
'''friend={}
for i in range(4):
    name,*l=input().split()
    lang=list(l)
    friend[name]=lang
print(friend)'''
#values of different key can be same

#quesiton 9
'''#s={8,7,12,'harry',[1,2]}
s={8,7,12,'harry'}
l=list(s)
for i in range(len(l)):
    if l[i]==8:
        l[i]=9
print(l)
#set are mutable meaning operations can be performed but set items are immutable ,cant be chagned if want to change convert to list first
#  and as items in set are stored according to hash so it will give random order when converted to list
# and thats why list in a set throws error as list are mutable hence cant be in a set'''