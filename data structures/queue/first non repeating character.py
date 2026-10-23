from collections import deque
firstnonrep=deque() #to keep tract of first non-repeating character in order of arrival
s = "aabc"
# ["a", "#", "b", "b", "c", "c"]
apponce=set() #to keep track of non-repeating characters
output=[]

for item in s:
    if item not in apponce: #if new unique add to set
        apponce.add(item)
        firstnonrep.append(item)
    else: #if a letter comes again it's no longer unique remove from set
        apponce.remove(item)

    while len(firstnonrep)>=0: #look for item at front of queue if in set add to output
        if len(firstnonrep)==0:
            output.append("#")
            break
        elif firstnonrep[0] in apponce:
            output.append(firstnonrep[0])
            break
        else:
            firstnonrep.popleft()


print(output)