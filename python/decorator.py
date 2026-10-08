#basic decorator
"""def decorator(func):
    def wrapper():
        print("hello")
        func()
        print("world")
        return 9
    return wrapper

@decorator
def greet():
    print("hello world")

r=greet()
print(r)
print(greet.__name__) #when wrapped changed to wrapper metadata of func greet is replaced
"""


#if want to preserve metadata of func greet use @wraps(func)
"""from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper():
        print("hello")
        func()
        print("world")
        return 9
    return wrapper

@decorator
def greet():
    print("hello world")

r=greet()
print(r)
print(greet.__name__) #now it keeps metadata of func preserved"""
#work flow
#greet called -> sees its under decorator -> decorator gives wrapper -> greet calls wrapper

#question 1 --------------------------------------------------------------
"""import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(n):
        print("Running",func.__name__)
        a = time.time()
        r=func(n)
        b = time.time()
        print(b-a)
        return r
    return wrapper

@timer
def calculate_sum(n):
    return sum(range(n))

result = calculate_sum(1000000)
print(result)"""

#question 2-----------------------------------------------------------------
#1st using specified arguements
"""from functools import wraps
users = {
    "Aman": "admin",
    "Riya": "user",
    "Karan": "user"}

def require_admin(func):
    @wraps(func)
    def wrapper(username,record_id):
        try:
            if username in users and users[username]=="admin":
                r=func(username,record_id)
                return r
            else:
                print("Access Denied")
                return None
        except KeyError:
            print("Username not Found")
    return wrapper

@require_admin
def delete_record(username, record_id):
    return f"Record {record_id} deleted by {username}"

print(delete_record("Aman",12))
print(delete_record("Karan",13))"""

#2nd using *args,**kwargs and args[0] as username is the 1st args given
"""from functools import wraps
users = {
    "Aman": "admin",
    "Riya": "user",
    "Karan": "user"}

def require_admin(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            if args[0] in users and users[args[0]]=="admin":
                r=func(*args,**kwargs)
                return r
            else:
                print("Access Denied")
                return None
        except KeyError:
            print("Username not Found")
    return wrapper

@require_admin
def delete_record(username, record_id):
    return f"Record {record_id} deleted by {username}"

print(delete_record("Aman",12))
print(delete_record("Karan",13))"""
