s="MCMXCIV"
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
v=0
i=0
while(i<len(s)):
    if i==len(s)-1 or d[s[i]]>=d[s[i+1]]: #for (last index) or (like MM or MC)
        v=v+d[s[i]] #just add their value
        i=i+1
    else:     # only for fixed subtraction pairs like "XC"
        v=v+d[s[i]+s[i+1]]  #just concatenate both and add
        i=i+2

print(v)