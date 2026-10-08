import time
#print(time.time())

#testing time elapsed
"""a=time.time()
def greet(func):
    def modfunc(*args):
        print("hello")
        func(*args)
        print("world")
    return modfunc

@greet
def add(a,b):
    print(a+b)

print(add(1,2))
b=time.time()
timeused=b-a
print(f"{timeused:.9f}")"""

#testing sleep
"""x=time.time()
time.sleep(10)
y=time.time()
print(y-x)"""

#printing local time
"""t=time.localtime()
print(t)
formattedtime=time.strftime('%Y-%m-%d %H:%M:%S',t)
print(formattedtime)
print(type(formattedtime))"""