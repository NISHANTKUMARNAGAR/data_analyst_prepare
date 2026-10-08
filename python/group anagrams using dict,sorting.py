s=["eat","tea","tan","ate","nat","bat"]
d={}
for i in range(len(s)):
    temp="".join(sorted(s[i]))
    if temp not in d:
        d[temp]=[s[i]]
    elif temp in d:
        d[temp].append(s[i])

final=[]
for j in d:
    final.append(d[j])
print(final)