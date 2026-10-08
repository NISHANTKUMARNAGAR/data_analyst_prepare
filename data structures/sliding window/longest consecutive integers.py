arr = [2, 7, 11, 15, 3, 6]
arr.sort()
consec=[]
l=0

for i in range(len(arr)):
    if len(consec)==0 or arr[i]==consec[-1]+1:
        consec.append(arr[i])
    else:
        if len(consec)>l: #if in between you found max length
            l=len(consec)
        consec.clear()

if len(consec)>l: #if last group is of max length
    print(len(consec))
else:
    print(l)