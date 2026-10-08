def solve(s):
    n=[]
    s=s.capitalize() #to capitaliza first word
    l=list(s)
    for i in range(len(s)): #location of empty space
        if(s[i]==' '):
            n.append(i)
        if(s[i]=='.'):
            n.append(i)

    for i in range(len(n)): #capitalizaing every letter after space
        if((s[(n[i])+1].isalpha())==True):
            l[(n[i])+1]=l[(n[i])+1].upper()
        if((s[(n[i])+1].isalpha())==True):
            l[(n[i])+1]=l[(n[i])+1].upper()

    return "".join(l) #making string from l

a="hello i am Nishant.i am Hungry"
p=solve(a)
print(p)