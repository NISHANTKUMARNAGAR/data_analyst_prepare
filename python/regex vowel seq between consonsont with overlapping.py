import re
pattern1=r'[aeiouAEIOU]+'
pattern2=r'[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]'
pattern=pattern2+pattern1+pattern2
text="match a single character not present in the list below MaaM hiip"
flag=0

m=re.search(pattern,text)
if(m):
    first_match=(m.group())[1:-1] #did this because we only want to print vowel part in question
    if(len(first_match)>=2):
        print(first_match)
        flag = 1
    search_start=m.start()+len(m.group())-1
    while(search_start<len(text)):
        p=re.search(pattern,text[search_start:len(text)])
        if(p):
            other_matches=(p.group())[1:-1]
            if (len(other_matches) >= 2):
                print(other_matches)
                flag = 1
            search_start=p.start()+search_start+len(p.group())-1
            #p.start is for getting to this match in sliced string
            #Search_Start is to get to this sliced string from start of orignal text (i.e. offset from orignal text)
            #len(p.group) is for finding out length of this match
            #-1 from len(p.group) is for going back to last vowel
            #           in match like in baeb to get to e so we can start
            #           checking from next char to account for overlapping
        else:
            break

if(flag==0):
    print(-1)