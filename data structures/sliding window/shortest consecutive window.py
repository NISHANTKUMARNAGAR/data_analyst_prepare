arr = [2, 3, 1, 2, 4, 3]
target = 7
s=0
e=0
minl=len(arr)
temp=arr[1]

while e<len(arr):
    if temp>=target:
        if e+1-s<minl:
            minl=e+1-s
        temp=temp-arr[s]
        s=s+1
    elif temp<target:
        e=e+1
        if e<len(arr):
            temp=temp+arr[e]

if minl==len(arr):
    print("no subarray exists whole array required")
else:
    print(minl)