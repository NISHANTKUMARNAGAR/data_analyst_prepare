#question 1
"""class Vector3d:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i +{self.j}j +{self.k}k"

class Vector2d:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def __str__(self):
        return f"{self.i}i +{self.j}j"

    def create3d(self,k):
        return Vector3d(self.i,self.j,k)

o=Vector2d(3,5)
print(o)
p=o.create3d(9)
print(p)"""

#question 2
"""class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    def __init__(self,n):
        self.name=n

    def bark(self):
        print(f"{self.name} barks")

o=Dog("spike")
o.bark()
print(Dog.mro())"""

#question 3
"""class Employee:
    def __init__(self,s,i):
        self.salary=s
        self.inc=i

    @property
    def salaryafterinc(self):
        return int(self.salary)

    @salaryafterinc.setter
    def salarysetter(self,l):
        if(self.inc==l):
            self.salary=self.salary +0.02*self.salary

o=Employee(40000,2)
o.salarysetter=o.inc
print(o.salaryafterinc)"""

#question 4
"""class Complex:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"{self.x}+{self.y}i"

    def __add__(self,obj):
        return Complex(self.x+obj.x,self.y+obj.y)

    def __mul__(self,obj):
        return Complex((self.x*obj.x)-(self.y*obj.y),(self.x*obj.y)+(self.y*obj.x))

c1=Complex(3,5)
print(c1)
c2=Complex(5,6)
print(c2)
print("addition:",c1+c2)
print("multiplication:",c1*c2)"""

#for a case where its told to take input from user
"""string="25j"
x,y=string.split('+')
a=int(x)
b=int(y[:len(y)-1])
print(a)
print(b)
#if(string.endswith('j'))
if((string.find('+'))!=-1):
    print('normal')
elif(string.isdigit()):
    print('only real number')
elif(string.isalnum()):
    print('only imaginary part')
    a=string[:len(string)-1]
    print(a)"""

#question 5
"""class Vector:
    def __init__(self,values):
        self.l=values

    def __add__(self,obj):
        newl = []
        for i in range(len(self.l)):
            newl.append(self.l[i]+obj.l[i])
        return Vector(newl)

    def dotpro(self,obj):
        dp=0
        for j in range(len(self.l)):
            dp=dp+(self.l[j]*obj.l[j])
        return dp

o1=Vector([4,5,6,345,45,8])
o2=Vector([4,5,3,4,3,5345])
print("added vector dimension are:",(o1+o2).l)
print("dot product of two vector has dimensions:",o1.dotpro(o2))"""