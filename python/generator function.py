#basic functionality of generator
"""def func():
    for i in range(5):
        yield i
    print('after loop')

p=func()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
try:
    print(next(p)) #stopiteration exception is raised when generator function ends
except StopIteration:
    print("stop iteration is raised")"""


#example without loop in generator  function
"""def func():
    print('hello')
    yield 1
    yield 2
    yield 3

itera=func()
print('after getting generator object')
for i in itera:
    print('before printing number')
    print(i)
    print("after printing number")"""

#generator with loop
"""def func(n):
    c=1
    while c<=n:
        print('before yield')
        yield c
        print("after yield")
        c=c+1

itera=func(5)
print('after getting generator object')
for i in itera:
    print('before printing number')
    print(i)
    print("after printing number")"""

#multiple generators
"""def numbers():
    yield from [1, 2, 3]
    yield from [4, 5, 6]
    
g=numbers()
for i in g:
    print(i)"""

#chaining generators
"""def numbers():
    for i in range(10):
        yield i

def squares(values):
    for value in values:
        yield value * value

for i in squares(numbers()):
    print(i)"""

#close() tells the generator to terminate.
#throw() injects an exception into the generator.

#communication with generator
#value = yield something #take a value in value variable
#g.send(value) #send value variable's value to g generator object

#a question to demonstrate exception handling for generators
"""numbers = [3, 7, 10, 14, 19, 22, 25, 30]
def op(l):
    for n in l:
        if n%2==0 and n>10:
            yield n

g=op(numbers)
print(next(g))
print(next(g))
for item in g:
    print(item)

try:
    print(next(g))
except StopIteration:
    print("no more values available")"""