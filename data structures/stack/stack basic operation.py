operations = [
    ("push", 10),
    ("push", 20),
    ("push", 30),
    ("peek", None),
    ("pop", None),
    ("peek", None),
    ("push", 40),
    ("size", None),
    ("pop", None),
    ("pop", None),
    ("pop", None),
    ("is_empty", None)
]
stack=[]
def push(x):
    stack.append(x)

def peek():
    return stack[-1]

def pop():
    return stack.pop()

def size():
    return len(stack)

def is_empty():
    return len(stack)==0

for item in operations:
    if item[0]=="push":
        push(item[1])
    elif item[0]=="pop":
        if size()!=0:
            n=pop()
            print(n)
        else:
            print(None)
    elif item[0]=="peek":
        if size()!=0:
            n=peek()
            print(n)
        else:
            print(None)
    elif item[0]=="size":
        l=size()
        print(l)
    elif item[0]=="is_empty":
        print(is_empty())