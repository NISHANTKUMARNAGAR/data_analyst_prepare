operations = [
    ("enqueue", 10),
    ("enqueue", 20),
    ("enqueue", 30),
    ("peek", None),
    ("dequeue", None),
    ("enqueue", 40),
    ("size", None),
    ("front", None),
    ("dequeue", None),
    ("enqueue", 50),
    ("is_empty", None),
    ("dequeue", None),
    ("dequeue", None),
    ("dequeue", None),
    ("peek", None),
    ("size", None),
    ("is_empty", None)
]
from collections import deque
q=deque()
output=[]

for item in operations:
    if item[0]=="enqueue": #add to left
        q.appendleft(item[1])
    elif item[0]=="dequeue": #remove from right
        if len(q)!=0:
            output.append(q.pop())
        else:
            output.append(None)
    elif item[0]=="is_empty": #retun True if q empty else false
        output.append(len(q)==0)
    elif item[0]=="peek" or item[0]=="front": #return first in queue
        if len(q)!=0:
            output.append(q[-1])
        else:
            output.append(None)
    else:
        output.append(len(q))

print(output)