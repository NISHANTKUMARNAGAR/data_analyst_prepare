#question 1
"""class progmic:
    def __init__(self,n,s):
        self.name=n
        self.sal=s

    def data(self):
        print(f"my name is {self.name} and my salary is {self.sal}")

p1=progmic("ron",23232)
p2=progmic("rohit",4545454)
p1.data()
p2.data()"""

#question 2
"""class Mathprog:
    def __init__(self,n):
        self.number=n

    @staticmethod
    def greet():
        print("hello)
    
    @property
    def sqrn(self):
        return self.number*self.number

    @property
    def cuben(self):
        return self.number*self.number*self.number

    @property
    def sqrtn(self):
        for i in range(1,self.number):
            if(self.number/i==i):
                return i

o=Mathprog(58920976)
print("square of number is ",o.sqrn)
print("cube of number is",o.cuben)
print("square root of number is",o.sqrtn)"""

"""#question 3
class Myclass:
    def __init__(self,p):
        self.a=p

o=Myclass(4)
o.a=0
print(o.a)
#o.a does change the attribute"""

#question 4
"""added in question 2"""

#question 5
"""#l = [[12331, 30, 200], [45454, 14, 400]]
class Indtrain:
    def __init__(self,n,a,tr,ti):
        self.name=n
        self.age=a
        self.trno=tr
        self.tick=ti

    l = [[12331, 30, 200], [45454, 14, 400]] #train data(train no.,no. of tick,price)

    def bookticket(self):
        #global l
        for i in range(len(Indtrain.l)):
            if (Indtrain.l[i][0] == self.trno):
                if (Indtrain.l[i][1] >= self.tick):
                    print(self.tick, "tickets booked")
                    Indtrain.l[i][1] = Indtrain.l[i][1] - self.tick
                else:
                    print("req number of seats not available")

    def status(self):
        #global l
        for j in range(len(Indtrain.l)):
            print(f"train {Indtrain.l[j][0]} has {Indtrain.l[j][1]} seats available")

    def fareinfo(self):
        #global l
        for k in range(len(Indtrain.l)):
            if(Indtrain.l[k][0]==self.trno):
                print(f"train {self.trno} has {Indtrain.l[k][2]} charge for 1 ticket")


n,a,tr,ti=input("enter name,age,train number,number of seats to be booked sep by space").split()
o=Indtrain(n,int(a),int(tr),int(ti))
o.bookticket()
o.status()
o.fareinfo()
#using classname.variablename in Indtrain.l is good to avoid using declaring l as global"""

#question 6 changing the "self" reference to object
"""class Test:
    def __init__(nishu):
        nishu.n="nishant"
        nishu.a=24

    def info(nishu):
        print(nishu.n,nishu.a)

o=Test()
o.info()
#can use anything as long as we use it consistently "self" is just a standard thing used in python"""