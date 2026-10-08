import re

#finding one occurence
"""pattern=r"llo"
text="hello, world"
m=re.search(pattern,text)
print(m)
print(m.span())
"""

#finding mutiple using re
"""pattern=r"[a-z]+at"
text="the cat is in the hat"
matches=re.findall(pattern,text)
print(matches)"""

#finditer() return a iterable of matchobjects
"""pattern=r"[a-z]+at"
text="cat in the hat"
matches=re.finditer(pattern,text)
for i in matches:
    print(i.span(),i.group())"""

#can compile patterns
"""text = "ABACADAEAFAGAHAIAJAKALAMANAOAPAQARASATAUAVAWAXAYAZ"
c=r"[B-DF-HJ-NP-TV-Z]"
w=r"[AEIOU]+"
pattern=c+w+c
regex=re.compile(pattern)
print(regex.search(text)) #can search via compiled pattern
print(regex.search(text,4)) #can also seach from a specific position"""

#to replace
"""pattern=r"[a-z]+at" #([a-z] means any one character from a to z),
                        (+ any characters after a to z is allowed),
                        (at is matched after [a-z]+ in text)
text="the cat is in the hat"
new_text=re.sub(pattern,"dog",text)
print(new_text)"""

#to group() returns entire match can print separately using group(n) n bring the  group number
"""text="the email is example@example.com"
pattern=r"\w+@\w+\.\w+" #(\w means any of a-z,A-Z,0-9 and _ ,+ we know),(@\w match @ before \w+),(\. match single dot(.) before again \w+)
match=re.search(pattern,text)
if match:
    email=match.group()
    print(email)"""

#groups() returns tuple containing all matches except group(0) i.e. full match
"""email_address = "contact@example.com"
pattern = r'(\w+)@(\w+)\.(\w+)'
match = re.search(pattern, email_address)
if match:
    print(match.groups())"""

#groupdict() returns a dictionary with groupname as keys
"""pattern=r'(?P<Username>\w+)@(?P<Website>\w+)\.(?P<Domain>\w+)'
text='jon@geekforgeeks.org'
match_object = re.match(pattern,text)
details = match_object.groupdict()
print(details)"""

#split() splits according to pattern
"""text='Words,words,words.'
print(re.split(r'\W+',text))
print(re.split(r'(\W+)',text))
print(re.split(r'\W+',text,maxsplit=1))"""

#start() and end() end points of span()
"""t="i love python"
p=r'python'
m=re.search(p,t)
print(m.start())
print(m.end())"""

#regex flags
import re

# 1. IGNORECASE — capitalization doesn't matter
text1 = "Python PYTHON python"
print(re.findall(r"python", text1, re.IGNORECASE))


# 2. MULTILINE — ^ and $ apply to each line
text2 = """Aman
Riya
Karan"""
print(re.findall(r"^.+$", text2, re.MULTILINE))


# 3. DOTALL — . can match newline
text3 = """Start
middle
end"""
print(re.search(r"Start.*end", text3, re.DOTALL).group())


# 4. VERBOSE — write a complex regex with spaces/comments
pattern = re.compile(r"""
    \d{3}      # area code
    -
    \d{3}      # first part
    -
    \d{4}      # last part
""", re.VERBOSE)

print(pattern.fullmatch("987-654-3210"))

#prog to find consecutive alphanumeric item
"""import re
text = "aB22ccZ7z"
pattern = r'([a-zA-Z0-9])\1' #\1 means that 1st group in () repeats
match = re.search(pattern, text)
if match:
    print("Repeated character:", match.group(1))
    print("Full match:", match.group(0))
else:
    print("No repetition found")"""

#to check for floating number
"""import re
pattern=r'^-?[0-9]*\.[0-9]+$'
n=int(input())
l=[]
for i in range(n):
    text=input()
    m=re.search(pattern,text)
    if(m):
      l.append(True)
    else:
      l.append(False)

for t in l:
    print(t)"""

#to check for id size 10 containing non-repetitive alphanumeric characters
"""import re
n = int(input())
results = []
pattern = r'^' \
          r'(?=[A-Za-z0-9]{10}$)' \ #only has alphanumerric characters
          r'(?!.*(.).*\1)' \ #no repetition allowed
          r'(?=(?:.*[A-Z]){2,})' \ #atleast 2 alphabetic characters
          r'(?=(?:.*[0-9]){3,})' \ #atleast 3 alphabetic characters
          r'.*$' #after above conditions could have anything after that
for _ in range(n):
    text = input()
    if re.match(pattern, text):
        results.append("valid")
    else:
        results.append("invalid")

print(*results, sep="\n")"""

#for validating roman numeral
"""regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))"""

#for checking hex color code
"""import re
pattern=r"(?!^#.*$)#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})" #first part i.e. lookahead is for checking that only hex code
                                                        matches i.e. #BED AND #CAB wouldn't match
text=
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}
l=[]

for i in range(int(input())):
    text=input()
    m=re.findall(pattern,text)
    if(m):
        for j in range(len(m)):
            l.append(m[j])

for k in l:
    print("#"+k)"""

#phone numbers matching regex
""""import re
pattern=r"^[7-9][0-9]{9}$"
l=[]
for i in range(int(input())):
  text=input()
  m=re.match(pattern,text)
  if(m):
    l.append("YES")
  else:
    l.append("NO")

for j in l:
  print(j)"""

#for email address starting with alphabetical char
"""import re
pattern=r"^[a-zA-Z](\w|\-|\.)*\@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
l=[]
for i in range(int(input())):
  name,text=input().split()
  text=text[1:len(text)-1]
  m=re.match(pattern,text)
  if(m):
    l.append(name+" <"+text+">")

for j in l:
  print(j)"""

#for valid credit card regex
"""import re
valid_char = r"^[4-6]\d{3}(-?\d{4}){3}$"
no_rep = r"(\d)\1{3,}"
l = []
for i in range(int(input())):
    text = input()
    m = re.match(valid_char, text)
    if (m):
        text = text.replace('-', '')
        n = re.search(no_rep, text)
        if (n):
            l.append('Invalid')
        else:
            l.append('Valid')
    else:
        l.append('Invalid')

for j in l:
    print(j)"""

#for substituting " && " and " || " to " and " and " or " repectively
"""
import re
orreg=r" \|\| "
andreg=r" && "
orrepl=" or "
andrepl=" and "

def reploper(text,pattern,replpatt):
    t = re.sub(pattern,replpatt, text)
    while(re.search(pattern,t)):
        t=re.sub(pattern,replpatt,t)
    return t

for i in range(int(input())):
    text = input()
    findand = re.search(andreg, text)
    findor = re.search(orreg, text)
    if (findand):
        m=reploper(text,andreg,andrepl)
        if (findor):
            n=reploper(m,orreg,orrepl)
            print(n)
        else:
            print(m)
    elif (findor):
            n=reploper(text,orreg,orrepl)
            print(n)
    else:
        print(text)"""

#for checking postal codes also checks less than 1 times yxy by special method
"""import re
P = input()
regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(?=(.)\d\1)"
print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)"""

#for validating a regex pattern
"""import re

l = []
n = int(input())
for i in range(n):
    try:
        pattern = input()
        if (re.search(r'(\*|\+|\?){2,}', pattern)):
            l.append(False)
            continue #if above if is satisfied false is added to list
                         continue skips this iteration
        re.compile(pattern)
    except re.error:
        l.append(False)
    else:
        l.append(True)

for j in l:
    print(j)"""
#that r'(\*|\+|\?){2,}' is for some regex engines allow .*+ but some dont so
#if we want to allow proper sysntax of it without repetitive quantifier like
# for example ** or ++ or *+ etc thats why used that if block to flag it as false
#but at the end dpends on the regex engine that what it wants to be ok or not

#matrix script problem Hackrrank -- given a matrix,do -flip it,make a string and
# use regex to replace group of symbol and whitespace with a single whitespace and print this
"""import re
n, m = map(int, (input().strip()).split())  # row,column
matrix = []
for _ in range(n): #to make matrix
    matrix.append(input())

matrix=zip(*matrix) #used zip to flip matrix
middle=""
for i in range(len(matrix)): #using for loop to creatie single string from matrix
        s="".join(matrix[i]) #making sub list to single string
        middle=middle+s #adding each sub list to single final string "middle"

print(re.sub(r"(?<=[A-Za-z0-9])(\s|!|@|#|\$|%|&)+(?=[A-Za-z0-9])"," ",middle))
#also $ means end of line so to check literal $ use \$"""

#istead of zip() above could use below code to form a string from matrix
"""
middle = ""
while (matrix != [""]*n): #to make a printable string from matrix
    for i in range(len(matrix)):
        middle = middle + matrix[i][0]
        matrix[i] = matrix[i][1:len(matrix[i])]

#could also just do newflippedmatrix=zip(*matrix) to get a matrix instead of using loops"""

#overlapping 1 or more vowel btw consonant
"""import re
text = "ABACADAEAFAGAHAIAJAKALAMANAOAPAQARASATAUAVAWAXAYAZ"
c=r"[B-DF-HJ-NP-TV-Z]"
w=r"[AEIOU]+"
pattern=c+w+c
matches=[]
i=0
e=len(text)
while(i<=e-2):
    m=re.search(pattern,text,i)
    matches.append(m.group())
    if i==0:
        i=i+len(m.group())
    else:
        i=i+len(m.group())-1

print(matches)
print(len(matches))"""