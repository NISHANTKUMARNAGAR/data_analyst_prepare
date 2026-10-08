def finindsub(count, string, sub_string):
    s = string
    s1 = sub_string
    c=count
    '''
    #uses recursion also for cant modify i inside the loop
    for i in range(len(s)):
        if ( ord(s[i]) == ord(s1[0]) ):
            n = s[i:len(s)].find(s1)
            if (n != -1):
                c = c + 1
                return finindsub(c, s[i+n+1:len(s)],s1)'''


    '''#does not use recursion and uses while loop to modify i
    i=0
    while(i<len(s)):
        if ( ord(s[i]) == ord(s1[0]) ):
            n = s[i:len(s)].find(s1)
            if (n != -1):
                c = c + 1
                i=i+n+1
        else:
            i=i+1'''
    return c

def count_substring(string, sub_string):
    count = 0
    return finindsub(count, string, sub_string)


string = 'ooooo'
sub_string = 'oo'
count = count_substring(string, sub_string)
print(count)