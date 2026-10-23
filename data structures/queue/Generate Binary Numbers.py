#Input:  n = 8
#Output: ["1", "10", "11", "100", "101", "110", "111", "1000"]

from collections import deque
q=deque(["1"])
l=["1"]
n=8

#process
#so we start from 1 add 0 or 1 then we get 10,11 so we take 10 add 0 and 1 so we get 100,101 and so on
if n==1:
    print(l)
else:
    rem=n-1
    while rem>0:
        if rem!=1:
            temp=q.popleft()
            q.append(temp+"0")
            q.append(temp+"1")
            l.append(temp+"0")
            l.append(temp+"1")
            rem=rem-2
        else:
            temp=q.popleft()
            q.append(temp+"0")
            l.append(temp+"0")
            rem=rem-1

    print(l)