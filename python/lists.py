#list always in square brackets
#list are always changable after creation
l1=[1,2,5,3,5]
print(l1)
l2=["naman","gadha","donkey"]
print(l2)
print(l1[2])
'''print(l1[4]) #out of range'''

#range always starts from zero and goes to length of list if only : mentioned
# ie [0:len(listname)] is executed
l3=["nishant",63,"nagar",True,3,7,9,5]
print(l3)   
print(l3[1]) #positive indexing
print(l3[-3]) #negative indexing which subtracts from length of l3 and works as [0:1]
print(l3[-3:3]) #before colon also subtracts from length of string
print(l3[5:3])  #return nothing as wrong order of index same in -3:3
print(l3[0:7:2]) #last 2 means every 2nd one from 0th item
                        #ie index 0 then 2 then 4 then 6 as there is no 8 index available it stops

#check if present (testing l3)
if "naman" in l3:
    print("gadha present")
elif 63 in l3:
    print("number present")

# check can be done with strings
n="hello"
if 'hel' in n:
    print('h present')
if 'ho' in n:
    print('ho presents')

#list comprehension ie creating list from another list,array,string,tuple,dictionary,set etc
#only work for list this same way cannot be used for tuple creation 
l4=[i*i for i in l1]
print(l4)
print(l1)
l5=[j+j for j in range(6)]
print(l5)
l6=[k for k in l2 if 'do' in k]
print(l6)
l7=[k for k in l2 if (len(k))<6]
print(l7)


#list methods

l1.sort() #sort in increasing order
print(l1)
l1.sort(reverse=True) #just reverses the list for which this function is called
print(l1)
l1.append(9) #just adds to last doesn't care about any order
print(l1)
l1.reverse() #reverse in itself is also a function just reverses the last updated list
print(l1)
print(l1.index(5)) #index return first occurence of that item
print(l1.count(5)) #count return how many times that item has occured
'''l8=l1'''  #this should never be done as this just creates the reference l8 of l1 in memory
             #only list l1 is present so any change to l8 changes that orignal l1 as l8 is just
            #another name or reference to l1 it does not copy l1 to l8
l8=l1.copy() #copy function creates copy of l1 and stores in l8 so now l1 and l8 are different
print(l8)
l8.insert(3,9) #adds 9 at index 3 and shifts other items 1 step back
print(l8)
l8.extend(l1) #extend just adds another list or set or tuple or dictionary at end of l8
print(l8)
print(l8+l2) # this '+' concatenates or joins two lists
l3.remove(True)
print(l3)

#list questions

#question 1
'''l9=[]
for i in range(7):
    f=input('enter the name of the fruit')
    l9.append(f)
print(l9)'''

#question 2
'''l10=[]
for l in range(6):
    m=int(input('enter the marks of the student'))
    l10.append(m)
l10.sort()
print(l10)'''

#question 4
'''l11=[3,6,2,4]
sum=0
for b in l11:
    sum=sum+b
print(sum)'''
