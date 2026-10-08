def nonrepstr(listofsub,lengthofsub):
    s=''
    for m in range(k):
        if(s.find(listofsub[m])==-1):
            s=s+str(listofsub[m])
    print(s)

def merge_the_tools(string, k):
    l=[]
    for i in range(0,len(string),k):
        l.clear()
        for j in range(i,i+k):
            l.append(string[j])
        nonrepstr(l,k)

string='AABCAAADA'
k=3
merge_the_tools(string, k)
