def mergesort(x):
    if len(x)<=1:
        return x

    x1=mergesort(x[:int(len(x)/2)])
    x2=mergesort(x[int(len(x)/2):])

    p1=0
    p2=0
    templ=[]
    while True:
        if p1<len(x1) and p2<len(x2):
            if x1[p1]<=x2[p2]:
                templ.append(x1[p1])
                p1=p1+1
            elif x2[p2]<x1[p1]:
                templ.append(x2[p2])
                p2=p2+1
        else:
            if p1==len(x1):
                templ.extend(x2[p2:])
                break
            elif p2==len(x2):
                templ.extend(x1[p1:])
                break

    return templ

arr = [5, 2, 8, 1, 3]
newarr=mergesort(arr)
print(newarr)