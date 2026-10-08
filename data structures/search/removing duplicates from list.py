arr = [1, 1, 2, 2, 3, 4, 4, 5]
f=1 #to check every new and find genuine
s=0 #to swap genuine with current
seen=set()

while f<len(arr):
    if arr[s] not in seen: #if new at s
        seen.add(arr[s])
        s=s+1
    else: #if not new at s
        if arr[f] not in seen: #if new at f
            arr[s],arr[f]=arr[f],arr[s]
            f=f+1
        else: #if not new at f
            f=f+1

#removing duplicates
for i in range(len(arr)-1,s,-1):
    arr.pop(i)

print(arr)

#without set--------------------------------------------------------
arr = [1, 1, 2, 2, 3, 4, 4, 5]
f=1
s=0

while f<len(arr):
    if arr[s]==arr[f]:
        f=f+1
    else:
        s=s+1
        arr[s]=arr[f]
        f=f+1

print(arr)
for i in range(len(arr)-1,s,-1):
    arr.pop(arr[i])

print(arr)