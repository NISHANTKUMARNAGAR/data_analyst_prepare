import random
arr = [7, 2, 9, 2, 5, 7, 1, 5]

#first sorting
def quick_sort(x):
    if len(x)<=1:
        return x
    n = random.randint(0, len(x) - 1) #taking random pivot
    pivot = x[n]
    x[n], x[-1] = x[-1], x[n] #moving pivot to end
    b = 0

    for i in range(len(x) - 1): #using loop to move all less/equal to pivot to left
        if x[i] <= pivot:
            x[b], x[i] = x[i], x[b]
            b += 1

    x[b], x[-1] = x[-1], x[b] #move pivot to left partition boundary at b

    left=quick_sort(x[:b])
    left.append(pivot)

    return left+quick_sort(x[b+1:])


sorted_arr=quick_sort(arr)
#removing duplicates second
s=1 #place distinct,distinct boundary
e=2 #find distinct,scan whole
while e<len(sorted_arr):
    if sorted_arr[s]!=sorted_arr[e]:
        s=s+1
        sorted_arr[s]=sorted_arr[e]
    elif sorted_arr[s]==sorted_arr[e]:
        e=e+1

for i in range(e-1,s,-1):
    sorted_arr.pop(i)

print(sorted_arr)

