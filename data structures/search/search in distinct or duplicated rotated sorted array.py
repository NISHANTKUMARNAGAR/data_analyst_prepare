x = [6,6,6,1,2,6,6]
t = 1
l=0
r=len(x)-1
result=-1
m=(l+r)//2

def bs(xl,xr): #apply binary search on where it belongs
    while xl<=xr:
        xm=(xl+xr)//2
        if x[xm]==t:
            return xm
        elif x[xm]>t:
            xr = xm - 1
        elif x[xm]<t:
            xl = xm + 1

def searchinrotatedsortedarray(l,r):
    while l<=r:
        m=(l+r)//2
        if x[m]==t:
            return m

        if x[m]-x[l]>0: #if left part is sorted
            if t<=x[m] and t>=x[l]: #item belongs in left part
                return bs(l,m-1)
            else:
                l=m+1
                continue
        if x[r]-x[m]>0: #if right part is sorted
            if t<=x[r] and t>=x[m]: #item belongs in right part
                return bs(m+1,r)
            else:
                r=m-1
                continue

if x[l] == x[r] == x[m]:  # if an array like [6,6,6,6,6,6,4,5,6,6],[6,6,6,6,6,6,6,6,6,6,6,6]
    if x[l] == t:
        print(l)
    else: #normal rotated sorted array with or without duplicates like [7,8,9,1,2,3,4,5,6],[7,7,1,2,3,3,4,4,5]
        l = m + 1
        r = r - 1
        result=searchinrotatedsortedarray(l, r) #call normal search with updated l and r
else: #normal rotated sorted array with or without duplicates like [7,8,9,1,2,3,4,5,6],[7,7,1,2,3,3,4,4,5]
    result=searchinrotatedsortedarray(l, r) #call normal search with normal l and r

if result==None:
    print(-1)
else:
    print(result)