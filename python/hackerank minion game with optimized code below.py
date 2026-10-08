#unoptimized code
"""
def finapp(c,s,s1):
    for i in range(len(s)):
        if ( ord(s[i]) == ord(s1[0]) ):
            n = s[i:len(s)].find(s1)
            if (n != -1):
                c = c + 1
                return finapp(c, s[i+n+1:len(s)],s1)

    return c

def minion_game(string):
    cons='BCDFGHJKLMNPQRSTVWXYZ'
    vow='AEIOU'
    kevin=0
    stuart=0
    ks=set()
    ss=set()
    c=0
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            if string[i:j][0] in cons:
                if string[i:j] not in ss:
                    stuart=stuart+finapp(c,string,string[i:j])
                ss.add(string[i:j])
            elif string[i:j][0] in vow:
                if string[i:j] not in ks:
                    kevin=kevin+finapp(c,string,string[i:j])
                ks.add(string[i:j])

    if(kevin>stuart):
        print('Kevin',kevin)
    elif(kevin<stuart):
        print('Stuart',stuart)
    elif(kevin==stuart):
        print('Draw')

s ='BANANA'
minion_game(s)"""

#optimized code

"""so above Program problem is that the function of the minion game Generate all possible substrings
of a given string for example banana My using nested for loops meaning it goes up to a complexity 
of order of n square Generated substring another Now we check every little substring for the whole 
string that how many times it occurs in the original that adds the complexity of order n of a game 
because another for loop is executed for that so now the problem in worst case it would go upto oerder 
of n cube which is not much for word like banana a 6 letter word but in some real life scenario this 
complexity would go to trillioss of calucation which would take years

so now wwe would not generate all substring we would just count number of sub-string that would be
generated meaning for banana all substring from b are points for stuart because b is consonant meaning 
b,ba,ban,bana,banan,banana 6 points for stuart likewise a(1st a) substring will be a,an,ana,anan,anana
will be 5 points for kevin so we can just check if 1st letter is vowel or not and add points accordingly
to kevin or stuart for overalapping of ana in this a(1st a)gernerates ana and a(2nd a)generates ana again 
so ana counted 2 times i.e. all its occurences including the overlapping one is counted also,for

b -- b,ba,ban,bana,banan,banana
a -- a,an,ana,anan,anana
n -- n,na,nana,nana
a -- a,an,ana
n -- n,na
a -- a

so as index increases the numberof string decreses by one for
i=1 5 subsrting + itself(b) so 6 substring for stuart b is consonant
i=2 4 substring + itself(a) so 5 substring for stuart a is vowel
i=3 3 substring + itself(n) so 4 substring for stuart b is consonant
i=4 2 substring + itself(a) so 3 substring for stuart a is vowel
i=5 1 substring + itself(n) so 2 substring for stuart n is consonant
i=6 0 substring + itself(a) so 1 substring for stuart a is vowel

we can conlude that "n-i" is formula that works and as i will increase 
from 1 to 6 all possible substring will be counted just add itself 
(meaning that letter to as its also a substring)

#remove the sets too as we are just counting the substring not creating
 #them so no storing in sets and no counting of them
"""
def minion_game(string):
    vow='AEIOU'
    kevin=0
    stuart=0
    c=0
    n=len(string)
    for i in range(len(string)):
        c=n-i
        if s[i] in vow:
            kevin=kevin+c
        else:
            stuart=stuart+c

    if(kevin>stuart):
        print('Kevin',kevin)
    elif(kevin<stuart):
        print('Stuart',stuart)
    elif(kevin==stuart):
        print('Draw')

s ='BANANA'
minion_game(s)