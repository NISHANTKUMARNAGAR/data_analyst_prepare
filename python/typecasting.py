#EXPLICIT TYPECASTING-THE ONE WHICH WE DO OURSELVES

a="1234"
b="2323"

c=int(a)
d=int(b)

print(c+d)
print(a+b)

#e=int(input("enter a number"))
#print(e+c)
#print(int(e)+c)

x="nishant"
y=1

#y=str(1)
#print(x+y)

print(x+str(y))


"""IMPLICIT TYPECASTING-THE ONE WHICH PYTHON DOES THE TYPECASTING
INTERNALLY INTO BIGGER DATA TYPE"""

q=1.9
p=4
print(p+q)

#as p was type casted into a bigger data type i.e. float
