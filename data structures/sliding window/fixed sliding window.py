arr = [2, 1, 5, 1, 3, 2]
k = 3
#temp to maintain sum of consecutive items
#maxsize to keep track of maxsum
temp=maxsum=0

if len(arr)==3:
    maxsum=sum(arr)
else:
    s=0
    e=2
    temp=maxsum=sum(arr[s:e+1])
    while e<len(arr)-1:
        temp=temp+arr[e+1]-arr[s]
        if temp>maxsum:
            maxsum=temp

        s=s+1
        e=e+1

print(maxsum)