#insertion sort - pick an element one by one and put it at its
#                 correct location in sorted elements
arr = [9, 4, 7, 3, 1, 8, 2, 6, 5]
#let's say 1st element is at its correct location
#so start from 2nd element
for i in range(1,len(arr)): #for every unsorted item
    s=0
    while s<i: #find its proper place
        if arr[i]<=arr[s]:
            insertpos=s
            break
        elif arr[i]>arr[s]:
            s=s+1

    poppeditem=arr.pop(i) #remove item from arr
    arr.insert(insertpos,poppeditem) #insert at correct location

print(arr)