arr = [4, 3, 7, 3, 2, 8, 4, 9, 2, 5, 8]
# Elements occurring exactly once → all go first, in any order.
# Elements occurring more than once → all go afterward, with all of their occurrences included.
# answer can be like -> [7, 9, 5, 4, 3, 3, 2, 8, 4, 2, 8]
countarr={}
for item in arr:
    if item in countarr:
        countarr[item]=countarr[item]+1
    else:
        countarr[item]=1

dup=0 #finds values with duplicates
dis=len(arr)-1 #finds distinct values
while dup<dis:
    if countarr[arr[dis]]>1:
        dis=dis-1
    elif countarr[arr[dup]]==1:
        dup=dup+1
    else:
        arr[dis],arr[dup]=arr[dup],arr[dis]
        dis=dis-1
        dup=dup+1

print(arr)