def dashout(outstr):
    l = []
    d = len(outstr)
    final=''
    for i in range(len(outstr)):
        l.append(outstr[i])
        if (i <d-1):
            l.append('-')
    for t in range(len(l)):
        final =final + l[t]
    return final


def print_rangoli(size):
    s = "abcdefghijklmnopqrstuvwxyz"
    spa = 1 + (size - 1) * 4
    if(size==1):
        print(s[size - 1].center(spa, '-'))
    else:
        for j in range(size, 0, -1):
            #print("1st for")
            startstring = s[j:size]
            outstr = startstring[::-1] + s[(j - 1):size]
            finstr = dashout(outstr)
            prioutstr = finstr.center(spa, '-')
            print(prioutstr)

        for k in range(1, size):
            #print("2nd for")
            startstring = s[k+1:size]
            outstr = startstring[::-1] + s[k:size]
            finstr = dashout(outstr)
            prioutstr = finstr.center(spa, '-')
            print(prioutstr)

n=8
print_rangoli(n)