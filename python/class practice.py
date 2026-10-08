"""class Details:
    p="abc"
    def __init__(self,n,a): #constructor
        self.name=self.p    #used self in p as when contructor get called
                            #p is no defined so self meaning p is attrubute
                            #of class so it checks in class Details for p,if
                            #we defined p in constructor we wouldn't have to
                            #write self
        self.age=a

    def info(self):
        print(f"{self.name} is my name and {self.age} is my age")

o=Details("Agatha",90)
print(o.name)
o.name="Ron"
print(o.name)
print(o.age)
o.info()"""

#decorator
"""def greet(func):
    def modfunc(*args):
        print("hello")
        func(*args)
        print("world")
    return modfunc

@greet
def add(a,b):
    print(a+b)

print(add(1,2))"""

#decorator when func is not modfied,but replaced
"""def outer(f):
    def modf(x,y):
        print("hello")
        print("world")
    return modf

#then

@outer
def add(a,b):
    print(a+b)

add(1,2)

#or

def add(a,b):
    print(a+b)

add=outer(add)
add(1,3)"""

#decorator which takes a value
"""
def repeat(times): #just to take value for decorator
    def decorator(func): #actual decorator
        def wrapper(*args,**kwargs): #wrapper that replaces orignal function
            for _ in range(times):
                result=func(*args,**kwargs)
            return result
        return wrapper
    return decorator

@repeat(5)
def sayhi():
    print("hi")

sayhi()"""

#getter setter
"""class myclass:
    def __init__(self,v):
        self.value=v

    @property  #this is getter used to get value
    def valueobj(self):
        return self.value

    @valueobj.setter
    def newobj(self,newvalue):
        self.value=newvalue

o=myclass(10)
print(o.valueobj) #taking value fom setter valueobj
o.newobj=20       #setting value of "value" using setter newobj
print(o.valueobj) #taking value fom setter valueobj after updating"""

#getter,setter with multiple arguement in setter
"""class Employee:
    def __init__(self,s,i):
        self.salary=s
        self.inc=i

    @property
    def salaryafterinc(self):
        return int(self.salary)

    @salaryafterinc.setter
    def salarysetter(self,values):
        i,j,k=values
        print(j)
        print(k)
        if(self.inc==i):
            self.salary=self.salary +0.02*self.salary

o=Employee(40000,2)
o.salarysetter=(o.inc,3,5)
print(o.salaryafterinc)"""

"""#making objects in a loop
class Test:
    def __init__(self,n,a):
        self.name=n
        self.age=a

    def showinfo(self):
        print(self.name,self.age)

l=[["ron",24],["ramesh",23],["rajiv",22],["rohit",20],["raj",25]]
o=[]
for i in range(len(l)):
    obj=Test(l[i][0],l[i][1])
    obj.showinfo()
    o.append(obj)
print(o)
o[0].showinfo()"""

#after leaning inheritence
"""class Ceo:
    def __init__(self,n,a):
        self.name=n
        self.age=a
        print("contructor of ceo")

    sal=9999
    name="pl"
    def show(self):
        print(self.name)

class Manager(Ceo):
    def __init__(self,m,l):
        self.nam=m
        self.ae=l
        print("contructor of manger")
    name="op"


o=Ceo("ron",23)
o.show()
o1=Manager("naman",99)
o1.show()
print(o1.sal)"""
###if same variable name in both classes and obj of manager
# uses it the name of manager i.e.derived one is used and will
# be used not the ceo one,and same is for constructor the constructor
# of manager is used over constructor of ceo for the obj of manager class

#private(__itemname) items in class
"""class Details:
    def __init__(self):
        self.__name="rohit"

    def info(self):
        print(self.__name)

obj=Details()
#print(obj.__name) #cant be accessed directly
print(obj._Details__name)
print(obj.info())"""

#acessing and working of class and instance variables
"""class Test:
    compname="tesla"

p1=Test()
p2=Test()
print(p1.compname)
p1.compname="pk"
print(p1.compname)
print(p2.compname)"""

#class methods
"""class Test:
    company="tesla"
    @classmethod
    def changecompany(cls,c):
        cls.company=c

t=Test()
print(t.company)
t.company="samsung"
print(t.company)
print(Test.company)
t.changecompany("apple")
print(Test.company)"""

"""#creating object using class method
class ABC:
    a=2
    @classmethod
    def create(cls,temp):
        cls.a=temp
        d=cls()
        return d

o1=ABC()
print(ABC.a)
o2=ABC.create(10)
print(ABC.a)"""

#dir() method
"""x=[1,2]
print(dir(x))"""

#__dict__ attribute,help() method
"""class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

p=Person("pk",26)
print(p.__dict__)
print(Person.__dict__)
print("trying help()")
print(help(p))
print(help(Person))"""

"""#super method
#used to acess attr. of parent class in child class
# as we cannot use them directly
class P1:
    p1att=9
    def p1m(self):
        print("this is 1st parent class method")
    def l(self):
        print("this is same method from p1")

class P2:
    p2att=4
    def p2m(self):
        print("this is 2nd parent class method")
    def l(self):
        print("this is same method from p2")

class Child(P1,P2):
    ch1=P1.p1att
    def ch(self):
        print("child method")
        super().l()
        super().p1m()
        super().p2m()

o=Child()
print(o.ch1)
o.ch()"""

#magic/dunder method
"""class Test:
    def __init__(self,n):
        self.name=n
#    def __str__(self):
#        return f"my name is {self.name} in str"
    def __repr__(self):
        return f"Test({self.name!r})"
    def __call__(self,sr):
        return self.name+' '+sr

t=Test("nishant")
print(t)
print(str(t))
t1=eval(repr(t))
print(t1.__dict__)
print(len(t1.name))
print(t('nagar'))
print(dir(t))"""
#if we dont use !r then python will not give '' around Nishant then eval will think we passed a variable name in
#creation of new object instead of a string for 'name' instance variable thats why !r is required there

#method overriding
"""class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x * self.y

s=Shape(4,3)
s.__init__(5,6)
print(s.area())

class Derived(Shape):
    def __init__(self,r):
        self.r=r
        super().__init__(r,r)

    #def area(self):
    #    return 3.14 * self.r * self.r   #completely overriding area

    def area(self):
        return 3.14 * super().area()     #entending area's behaviour

d=Derived(9)
print(d.area())"""

#operator overloadinng
"""class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i +{self.j}j +{self.k}k"

    def __add__(self,obj2):
        return Vector(self.i+obj2.i ,self.j+obj2.j ,self.k+obj2.k)

v1=Vector(3,5,6)
print(v1)

v2=Vector(1,2,9)
print(v2)

print(v1+v2)
print(type(v1+v2))"""

#multilevel inheritence
"""class A:
    def f(self):
        print("this is a")

class B(A):
    pass

class C(B):
    pass

o=C()
o.f()
print(C.mro())"""

#hybrid inhertence
"""class ultrabase:
    pass

class ulti1(ultrabase):
    pass

class ulti2(ultrabase):
    pass

class ulti3(ultrabase):
    pass

class ulti4(ultrabase):
    pass

class bas1(ulti1,ulti2):
    pass

class bas2(ulti3,ulti4):
    pass

class ch(bas1,bas2):
    pass

o=ch()
print(ch.mro())"""

#heirarchial inhertence
"""class base:
    pass

class der1(base):
    pass

class der2(base):
    pass

class der3(base):
    pass

class der4(base):
    pass 
#here all der clasess are child classes of 1 base class"""


#library question----------------------------------------
"""books = [("1984", "George Orwell", 3),("Dune", "Frank Herbert", 2),("The Hobbit", "J.R.R. Tolkien", 4)]

class Book:

    library_name="City Library"

    def __init__(self,t,a,c):
        self.title=t
        self.author=a
        if c>0:
            self._copies=c
        else:
            print("you put wrong number of copies make book again")

    def borrow(self):
        if self._copies>=1:
            self._copies=self._copies-1
            return True
        else:
            return False

    def return_book(self):
        self._copies=self._copies+1

    @property
    def copy_check(self):
        return self._copies

    @copy_check.setter
    def copy_check(self,c):
        if c>=0:
            self._copies=c

    def __eq__(self,obj2):
        if (self.title==obj2.title) and (self.author==obj2.author):
            return True
        else:
            return False

    def __len__(self):
        return self._copies

    def __call__(self):
        return self.borrow()

book_lib=[]
for item in books:
    obj=Book(item[0],item[1],item[2])
    book_lib.append(obj)

#demonstration
print(book_lib[2].borrow())
print(book_lib[2].borrow())
book_lib[2].return_book()
print(book_lib[1].borrow())
print(book_lib[1].borrow())
print(book_lib[1].borrow())
Book.library_name="New_Library"
print(book_lib[0]==book_lib[2])
print(len(book_lib[1]))
print(book_lib[2]())"""

#things to remember
"""
LIBRARY QUESTION — MISTAKES / THINGS TO REMEMBER
================================================

1. __len__() MUST RETURN AN INTEGER
------------------------------------
I initially wrote:

    def __len__(self):
        print("number of copies =", self.copies)

The problem is that len(obj) expects __len__() to RETURN an integer.

Remember:

    len(obj)
        ↓
    obj.__len__()
        ↓
    must return an integer

So it should be:

    def __len__(self):
        return self._copies

If I want to display it as well, I can print the result outside:

    print(len(book))


2. __eq__() MUST RETURN True/False
-----------------------------------
I initially printed the result inside __eq__():

    def __eq__(self, obj2):
        if ...:
            print("equal")
        else:
            print("not equal")

But __eq__() is used by:

    book1 == book2

Therefore it should RETURN a Boolean:

    def __eq__(self, obj2):
        return self.title == obj2.title and self.author == obj2.author

Remember:
Special methods that implement an operation normally need to return
the result of that operation.

Examples:

    __eq__   → return True/False
    __len__  → return integer
    __add__  → return resulting object/value
    __call__ → return whatever the callable operation is supposed to return


3. USE "and" FOR BOOLEAN LOGICAL CONDITIONS
-------------------------------------------
I initially used:

    (self.title == obj2.title) & (self.author == obj2.author)

This happens to work here because the operands are Booleans, but "&"
is the bitwise AND operator.

For logical Boolean conditions, remember:

    and
    or
    not

So:

    self.title == obj2.title and self.author == obj2.author

is the appropriate expression.


4. __call__() SHOULD RETURN THE RESULT WHEN THE REQUIREMENT SAYS
   THE CALL SHOULD RETURN SOMETHING
---------------------------------------------------------------
I initially wrote:

    def __call__(self):
        print(self.borrow())

But the requirement was that:

    book()

should RETURN True/False.

Therefore:

    def __call__(self):
        return self.borrow()

Remember the difference:

    print(...)
        → displays something

    return ...
        → gives a value back to the caller

If the question says "return", don't replace that with print.


5. PROPERTY MUST ACTUALLY CONTROL THE ATTRIBUTE BEING PROTECTED
---------------------------------------------------------------
I initially had:

    self.copies = c

and later created:

    @property
    def copy_check(self):
        return self.copies

    @copy_check.setter
    def copy_check_setter(self, c):
        if c >= 0:
            self.copies = c

The problem is that this property does NOT control:

    book.copies = -5

because "copies" is still a normal public attribute.

The setter is attached to:

    copy_check

Therefore the controlled assignment would be:

    book.copy_check = 5

If the actual requirement is:

    book.copies = new_value

and that assignment must be validated, then the property itself
should represent "copies", while the real internal storage should
be something like:

    self._copies

For example:

    @property
    def copies(self):
        return self._copies

    @copies.setter
    def copies(self, value):
        if value >= 0:
            self._copies = value

This way:

    book.copies = -5

goes through the setter instead of directly modifying the internal
value.


6. UNDERSTAND WHY _copies IS USED WITH A PROPERTY
--------------------------------------------------
A common pattern is:

    self._copies

for the internal storage and:

    @property
    def copies(...)

for controlled public access.

The idea is:

    book.copies
        ↓
    property getter
        ↓
    self._copies

and:

    book.copies = value
        ↓
    property setter
        ↓
    validate value
        ↓
    self._copies = value

This prevents the setter from recursively calling itself.

For example, don't do:

    @copies.setter
    def copies(self, value):
        self.copies = value

because that would call the setter again.


7. DO NOT CONFUSE "PRIVATE/INTERNAL" STORAGE WITH A PROPERTY
-------------------------------------------------------------
Using:

    self._copies

is a convention indicating that the attribute is intended for
internal/protected use.

The property is what gives controlled access.

So these are two separate ideas:

    _copies
        → internal storage/convention

    @property
        → controlled interface for accessing/modifying it


8. __call__ IS FOR MAKING AN OBJECT CALLABLE
---------------------------------------------
I used:

    def __call__(self):
        return self.borrow()

This is valid.

It means:

    book()

is equivalent in concept to:

    book.__call__()

and in this particular program it performs a borrow.

Remember that __call__ is not required just because a class has
methods. It is specifically used when you want the OBJECT ITSELF
to behave like a callable.


9. SPECIAL METHODS SHOULD MATCH THE OPERATION THEY IMPLEMENT
-------------------------------------------------------------
When implementing a dunder method, think about what Python expects
that operation to produce.

Examples:

    obj == other
        → __eq__()
        → Boolean

    len(obj)
        → __len__()
        → integer

    obj + other
        → __add__()
        → resulting value/object

    str(obj)
        → __str__()
        → string

    repr(obj)
        → __repr__()
        → string

    obj()
        → __call__()
        → whatever result the callable is designed to return

Don't just make the method print something unless printing is
actually the requirement.


10. SEPARATE INTERNAL LOGIC FROM DISPLAY
----------------------------------------
A useful general rule from this question:

    return a value
and
    print a value

are different things.

For example:

    def borrow(self):
        ...
        return True

Then outside:

    print(book.borrow())

This is generally more reusable than:

    def borrow(self):
        ...
        print(True)

Because the returned Boolean can be used by other code:

    if book.borrow():
        print("Borrowed successfully")


11. WHEN A QUESTION SAYS AN ATTRIBUTE "MUST NEVER" HAVE A BAD VALUE,
    THINK ABOUT ALL WAYS THE VALUE CAN CHANGE
---------------------------------------------------------------
The constructor check:

    if c >= 0:
        ...

only protects the value during object creation.

It does NOT automatically protect later assignments.

For example:

    book = Book(...)
    book.copies = -10

can bypass the constructor check.

So whenever a requirement says something like:

    "must never be negative"

ask myself:

    "Can the value be changed after construction?"

If yes, the validation must also cover later updates.


12. READ THE REQUIREMENT LITERALLY
----------------------------------
If the question says:

    book()

should return True/False

then make it return True/False.

If it says:

    len(book)

should return the number of copies

then __len__ must return that number.

If it says:

    book1 == book2

should compare title and author

then __eq__ should return the comparison result.

Don't substitute a visually similar behaviour such as printing the
result.


13. WHEN USING A PROPERTY, THE PROPERTY NAME SHOULD USUALLY MATCH
    THE PUBLIC ATTRIBUTE YOU WANT TO CONTROL
---------------------------------------------------------------
Instead of something like:

    copy_check
    copy_check_setter

a cleaner design is:

    @property
    def copies(self):
        ...

    @copies.setter
    def copies(self, value):
        ...

Then the outside interface naturally becomes:

    book.copies
    book.copies = 5

while the internal implementation can use:

    self._copies


14. OVERALL LESSON FROM THIS QUESTION
-------------------------------------
The main mistakes were not about understanding classes themselves.

They were mostly about understanding the CONTRACT of Python's
special methods and properties:

    __len__  → must return integer
    __eq__   → should return Boolean
    __call__ → return the required result
    @property → getter
    @property.setter → controls assignment to the property
    _copies → internal storage
    print → display
    return → give value back

When writing a program, always ask:

    "What exactly is Python expecting this method/attribute
     interface to provide?"

That prevents most of the mistakes I made in this question.
"""

#banking question--------------------------
"""accounts = [("Aman", 10000),("Rahul", 15000),("Priya", 20000)]

class Account:
    def __init__(self,n,b):
        self.name=n
        self.__balance=b

    @property
    def meth_balance(self):
        return self.__balance

    @meth_balance.setter
    def meth_balance(self,b):
        if b>=0:
            self.__balance=b

    bank_name = "National Bank"

    @classmethod
    def change_bank_name(cls, bn):
        cls.bank_name = bn

    @staticmethod
    def give_bank_name():
        return Account.bank_name

    def __str__(self):
        return f"{self.name}-Balance:{self.__balance}"

    def __repr__(self):
        return f"for developer {self.name},{self.__balance}"

    def __add__(self,obj2):
        return Account(self.name+obj2.name,self.__balance+obj2.__balance)

    def __len__(self):
        return self.__balance

    def __call__(self):
        return self.name

class SavingsAccount(Account):
    def __init__(self,n,b,i):
        super().__init__(n,b)
        self.intrest_rate=i

    def __str__(self):
        return f'{self.name}-Balance:{self.meth_balance}-Intrest:{self.intrest_rate}%'

    def __add__(self,obj2):
        return SavingsAccount(self.name+obj2.name,self.meth_balance+obj2.meth_balance,self.intrest_rate)

class PremiumAccount(Account):

    intrest_rate=15

    def __init__(self,n,b):
        super().__init__(n,b)

    def __str__(self):
        return f'{self.name}-Balance:{self.meth_balance}-Intrest:{self.intrest_rate}%'

    def __add__(self,obj2):
        return PremiumAccount(self.name+obj2.name,self.meth_balance+obj2.meth_balance)

Accounts_list=[]
for item in accounts:
    obj=Account(item[0],item[1])
    Accounts_list.append(obj)

so=SavingsAccount('pk',1000000,9)
so1=SavingsAccount('lk',2000000,9)
print(so)
print(so+so1)
po=PremiumAccount('qa',3000000)
po1=PremiumAccount('qo',4000000)
print(po)
print(po+po1)
print(Account.give_bank_name())
Account.change_bank_name("New Bank")
print(Account.give_bank_name())
so.meth_balance=90000
#above shown inherited and overridden behaviour
print(len(Accounts_list[0]))
print(str(Accounts_list[0]))
print(repr(Accounts_list[0]))
print(Accounts_list[0]())
print(po())
print(PremiumAccount.mro())"""

#things to remember
"""
BANKING QUESTION — MISTAKES / THINGS TO REMEMBER
================================================

1. A CLASS METHOD MUST MODIFY THE CLASS THROUGH "cls"
------------------------------------------------------
I initially wrote:

    @classmethod
    def change_bank_name(cls, bn):
        bank_name = bn

The problem is that:

    bank_name = bn

only creates a local variable inside the method.

It does NOT change the class attribute.

Remember:

    @classmethod
    def change_bank_name(cls, bn):
        cls.bank_name = bn

"cls" refers to the class that the class method is operating on.

So:

    cls.bank_name = bn

actually changes the class attribute.


2. UNDERSTAND WHAT A CLASS METHOD RECEIVES
-------------------------------------------
A class method automatically receives the class as its first
argument:

    @classmethod
    def method(cls, ...):

For example:

    Account.change_bank_name("New Bank")

is conceptually passing Account as cls.

So:

    cls.bank_name

means:

    Account.bank_name

in this case.

Remember:

    instance method → self
    class method    → cls
    static method   → neither automatically


3. A STATIC METHOD DOES NOT RECEIVE "self" OR "cls"
---------------------------------------------------
I initially wrote:

    @staticmethod
    def give_bank_name(cls):
        return cls.bank_name

That is not how a static method works.

A static method receives no automatically supplied instance or class.

So:

    @staticmethod
    def give_bank_name():
        return Account.bank_name

is valid.

Remember:

    @staticmethod
    def func(...):

does NOT automatically receive:

    self
or
    cls


4. IF I NEED "cls", I PROBABLY WANT A CLASS METHOD
---------------------------------------------------
Compare:

    @classmethod
    def method(cls):
        return cls.bank_name

with:

    @staticmethod
    def method():
        return Account.bank_name

The first receives the class automatically.

The second doesn't.

So remember:

    Need instance → instance method → self

    Need class → class method → cls

    Need neither → static method


5. DON'T DIRECTLY ACCESS A PRIVATE ATTRIBUTE FROM A SUBCLASS
-------------------------------------------------------------
I initially used things like:

    self._Account__balance

inside SavingsAccount and PremiumAccount.

This technically works because __balance is name-mangled to:

    _Account__balance

But I had already created a property:

    @property
    def meth_balance(self):
        return self.__balance

Therefore the cleaner interface is:

    self.meth_balance

and:

    obj.meth_balance

The property exists specifically to provide controlled access to
the private/internal value.

Remember:

    __balance
        → private/name-mangled internal storage

    property
        → controlled public interface


6. NAME MANGLING IS NOT TRUE PRIVATE ACCESS CONTROL
---------------------------------------------------
I should remember that:

    self.__balance

doesn't make the value completely inaccessible.

Python name-mangles it approximately to:

    _Account__balance

That is why:

    self._Account__balance

can technically access it.

But normally I should use the intended interface/property instead
of deliberately bypassing it.


7. PROPERTY + PRIVATE STORAGE IS A COMMON PATTERN
--------------------------------------------------
The Banking question used:

    self.__balance

and:

    @property

The general idea is:

    internal value
        ↓
    controlled property
        ↓
    outside code

For example:

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value

Then the outside code can use:

    account.balance

without directly manipulating:

    account.__balance


8. __str__ SHOULD RETURN A STRING
---------------------------------
I correctly used:

    def __str__(self):
        return f"..."

Remember that:

    str(account)

and:

    print(account)

expect __str__() to return a string.

Do not use:

    print(...)

inside __str__ as the actual result.

The method should return the representation.


9. __repr__ SHOULD ALSO RETURN A STRING
----------------------------------------
I correctly used:

    def __repr__(self):
        return f"..."

Remember:

    __str__
        → human-friendly representation

    __repr__
        → developer/debugging representation

Both return strings.


10. __add__ SHOULD RETURN THE RESULTING OBJECT
-----------------------------------------------
I used:

    def __add__(self, obj2):
        return Account(...)

This is the correct general pattern.

When Python evaluates:

    account1 + account2

it calls:

    account1.__add__(account2)

The method should return the result of the operation.

Remember:

    __add__ → return the resulting value/object

not simply print the result.


11. SUBCLASSES CAN OVERRIDE __add__, JUST LIKE OTHER METHODS
-------------------------------------------------------------
SavingsAccount and PremiumAccount had their own:

    __add__()

This means the subclasses can define what "+" means for their
objects.

This is another example of method overriding/polymorphism.

Remember:

    Parent implementation
          ↓
    child can override it
          ↓
    child's implementation is used for child objects


12. super() IS USED TO REUSE PARENT INITIALIZATION
---------------------------------------------------
I correctly used:

    super().__init__(n, b)

inside:

    SavingsAccount
    PremiumAccount

This means the parent Account initialization handles the common
parts:

    name
    balance

while the subclass handles its additional information.

Remember the useful pattern:

    class Child(Parent):

        def __init__(...):
            super().__init__(...)
            # initialize child-specific attributes


13. DON'T DUPLICATE COMMON PARENT INITIALIZATION
------------------------------------------------
If Account already knows how to initialize:

    name
    balance

then SavingsAccount should not rewrite all of that.

Instead:

    super().__init__(...)

and then add:

    self.interest_rate = ...

This keeps shared behaviour in the parent.


14. INHERITANCE SHOULD REPRESENT THE "IS-A" RELATIONSHIP
--------------------------------------------------------
The Banking question used:

    SavingsAccount(Account)

    PremiumAccount(Account)

This makes sense because:

    SavingsAccount IS AN Account

    PremiumAccount IS AN Account

Therefore they inherit common Account behaviour and can add or
override their own behaviour.


15. OVERRIDING DOES NOT MEAN EVERYTHING MUST BE REWRITTEN
----------------------------------------------------------
For example, SavingsAccount overrides:

    __str__()

because it needs additional information.

But it can still inherit:

    __len__()
    __call__()
    properties
    other Account methods

unless it needs different behaviour.

Remember:

    inherit what is already appropriate
    override only what needs different behaviour


16. CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE
-----------------------------------------
I correctly used:

    bank_name = "National Bank"

as a class attribute.

This means it belongs to the class rather than being separately
stored in every account.

So:

    Account.bank_name

accesses the class-level value.

Instances can also access it through inheritance/lookup:

    account.bank_name

Remember the distinction:

    class attribute
        → shared class-level data

    self.something
        → instance-specific data


17. MRO DETERMINES WHERE INHERITED METHODS ARE FOUND
----------------------------------------------------
I used:

    PremiumAccount.mro()

This is important.

For:

    class PremiumAccount(Account):

the basic MRO is:

    PremiumAccount
    Account
    object

Python searches according to that order.

Remember:

    MRO = Method Resolution Order

It becomes especially important when multiple inheritance is
involved.


18. __len__ MUST RETURN AN INTEGER
----------------------------------
I correctly used:

    def __len__(self):
        return self.__balance

So:

    len(account)

returns the balance.

Remember the same rule from the Library question:

    __len__ → integer

It should not merely print the length/value.


19. __call__ MAKES AN OBJECT CALLABLE
-------------------------------------
I used:

    def __call__(self):
        return self.name

Therefore:

    account()

works.

Remember:

    account()

means Python invokes:

    account.__call__()

when __call__ is defined.

The behaviour of __call__ should be deliberately chosen; it isn't
something every class needs.


20. A STATIC METHOD SHOULD BE USED ONLY WHEN INSTANCE/CLASS STATE
    IS NOT NEEDED
---------------------------------------------------------------
In this question:

    give_bank_name()

doesn't need an individual account object.

That's why a static method can make sense.

But if the method needs:

    self
or
    cls

then it shouldn't be a static method.

Remember:

    staticmethod → independent utility associated with the class

    classmethod → operates on class-level state

    instance method → operates on object-level state


21. USE THE PUBLIC INTERFACE YOU CREATED
----------------------------------------
If I create:

    @property
    def meth_balance(self):
        return self.__balance

then later code should generally use:

    self.meth_balance

rather than:

    self._Account__balance

The property is the interface I intentionally created.

This makes the code easier to change later because the internal
storage can change without changing the outside interface.


22. CHECK WHETHER I ACTUALLY DEMONSTRATED EVERY REQUIRED FEATURE
----------------------------------------------------------------
In a programming question containing many requirements, I should
make a checklist before finishing.

For this Banking question:

    class attribute              ✓
    class method                 ✓
    static method                ✓
    private attribute            ✓
    property/setter              ✓
    inheritance                  ✓
    super()                      ✓
    overriding                   ✓
    polymorphism                 ✓
    __str__                      ✓
    __repr__                     ✓
    __add__                      ✓
    __len__                      ✓
    __call__                     ✓
    MRO                          ✓

The important lesson is:

    Don't only implement a feature.
    Also demonstrate that it actually works if the question asks
    for a demonstration.


23. WHEN DEBUGGING, SEPARATE "LOGIC ERROR" FROM "DESIGN CHOICE"
---------------------------------------------------------------
Not every unusual implementation is necessarily incorrect.

For example:

    self._Account__balance

is technically valid.

The important question is whether it violates the intended design
or requirement.

So when reviewing my own code, ask:

    "Does this actually produce the wrong result?"

and separately:

    "Is there a cleaner/more appropriate way to implement it?"

Don't confuse a style/design improvement with an actual bug.


24. MAIN LESSON FROM THE BANKING QUESTION
-----------------------------------------
The biggest things I need to remember for future OOP programs are:

    self
        → current object

    cls
        → current class

    @classmethod
        → automatically receives cls

    @staticmethod
        → automatically receives neither self nor cls

    @property
        → controlled attribute access

    __private
        → name-mangled internal attribute

    super()
        → continue through the inheritance hierarchy

    overriding
        → subclass provides its own implementation

    __str__
        → human-readable string

    __repr__
        → developer-oriented representation

    __add__
        → behaviour for +

    __len__
        → behaviour for len()

    __call__
        → makes an object callable

    MRO
        → determines inheritance lookup order


25. GENERAL PROGRAMMING HABIT TO REMEMBER
-----------------------------------------
Before considering an OOP program finished, check:

    1. What data belongs to each object?
    2. What data belongs to the class?
    3. Which things should be internal/private?
    4. Which attributes need validation?
    5. Which behaviour belongs to the parent?
    6. Which behaviour needs overriding?
    7. Am I correctly using self vs cls?
    8. Does every dunder method return the type Python expects?
    9. Am I using the interface/property I created instead of
       bypassing it?
    10. Did I actually test every requirement?

These checks will prevent most of the mistakes I made in this
question.
"""