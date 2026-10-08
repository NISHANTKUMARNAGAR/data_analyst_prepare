#a={"a","b","c"};
#print(a);

#constructor set()
'''b=set(['$',"a",4,4,4,4,4]);
print(b);'''
#accesssing a element
a={"a","b","c"};
for i in a:
    print(i);

#setoperations
b={"a","b","c","d","e","f"};
c={"e","f"};
#symmeteric difference
g=c^b
print('symmetric difference',g)
#union operator = |
d=b|c;
print(b);
#intersection operator = &
e=b&c;
print(e);
#minus operator = -
f=b-c;
print(f);
#comparision
if(c>b):
    print("true");
else:
    print("false");

#frozen sets
a={2,3,4,5};
a.add(7);
print(a);
#f=frozenset([2,3,4,5]);
#f.add(8);
#print(f);


#set methods
z={2.23,32,34,34};
z.clear();
print(z)
y={213,4,3,4,232,4234};
x=y.copy();
print(x);
w=y.difference(x);
print(w);
t={3,43,4,3,434,3,4,34,34};
u={34,34,34,3,4,3};
#v=t.difference_update(u);
#print(v);
print(t);
t.discard(3);
print(t);
t.remove(4);
print(t);
s=t.intersection(u);
print(s);
print(s.issubset(t));
print(t.issuperset(s));
r={32,3,23,4,3,4,34};
q=r.pop()
print(q);

s20={1,2,3}
s21=set() #declare a empty set
s21.update(s20) #adds items of s20 to s21 and would work as long as s20 is a iterable ex. list,tuple,string etc
#difference between union and update is union creates a new set each time but update changes exting set

#taking input in set(input in a different lines)
n=int(input())
s=set()
for i in range(n):
  p=input()
  s.add(p)
print(len(s))

#taking input in same line
s1=set()
data1=list(map(int,input().split()))
s1.update(data1)

