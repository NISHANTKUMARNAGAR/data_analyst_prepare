import re
text='ddaadaaa'
pattern=r'aa'
flag=0 #to check if matched even once
s=re.search(pattern,text)
if (s):
    print((s.start(),((s.end()) - 1)))
    i=s.start()+1
    flag=1
    while (i < len(text)):
        p=re.search(pattern,text[i:len(text)])
        if(p):
            print((i+p.start(),i+((p.end())-1)))
            i=p.start()+i+1 #to get to new checking index
        else:
            break

if(flag==0):
    print((-1,-1))

# In my earlier string-based version of "find substring with overlapping.py", I used a variable 'n'
# to store the index of where the substring was found inside the sliced string/new string created
# by slicing (s[i:]). That was necessary because the str.find() method only returns the index relative
# to the portion of the string being searched because str.find() was being used in sliced string — not
# the original full string. So, to move my main index 'i' correctly through the original string, I had
# to add n to it using 'i = i + n + 1', where '+1' ensured overlapping matches were also counted by
# searching next from 1 character to right and n added the offset from main string.i for current position
# in sliced string n for position or offset from original string +1 for going 1 position to right to not
# skip any overlapping matches
#
# However, in this regular expression version, I didn’t need to explicitly use any variable
# like 'n' because re.search() returns a MatchObject that already provides the exact positions
# of the match using its start() and end() methods. These give the indices (relative to the
# substring being searched/i.e. whether it was original or sliced one) where the match begins
# and ends. So instead of storing a separate 'n', I directly accessed p.start() to know where
# the next match occurs and used it inline as 'i = p.start() + i + 1' to shift my search position
# forward by one for overlapping checks.Essentially, start() served the same purpose that 'n' did
# earlier — they told me where the match occurred and end() was just for printing end point of
# matched string — but since re.search() gives that information directly through
# the MatchObject, I didn’t need to manually store or calculate it as a separate variable.
