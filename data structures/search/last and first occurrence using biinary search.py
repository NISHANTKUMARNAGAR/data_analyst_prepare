# find last occurrence of target
arr = [1, 3, 3, 3, 5]
t = 3
l=0
r=len(arr)-1

while l<r:
    m=(l+r+1)//2
    if arr[m]<=t:
        l=m
    elif arr[m]>t:
        r=m-1

print(l)
# Normal (l + r) // 2 is always left-biased.
# For finding the last occurrence, we need a right-biased midpoint because
# we keep m by doing l = m. If m stays at the left pointer, the search can
# get stuck. Adding 1 makes the integer division return the right pointer
# when only two pointers remain, so the search continues and converges.
# so m = (l + r + 1) // 2 must be done

# find first occurrence of target
arr = [1, 3, 3, 3, 5]
t = 3
l=0
r=len(arr)-1

while l<r:
    m=(l+r)//2
    if arr[m]>=t:
        r=m
    elif arr[m]<t:
        l=m+1

print(l)
# this time as l+r//2 always converges on left pointer it
# always does not get stuck even when l+1=r like l=2,r=3
# it will converge on left pointer and give result