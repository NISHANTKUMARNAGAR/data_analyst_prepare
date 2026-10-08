p="x**3 + x**2 + x + 1"
x, k = 1,4  # variable,final value
print("x:",x)
print("k:",k)
pitems = list(map(str.strip, p.split(" ")))  # polynomial
print(pitems)
value = 0

for i in range(len(pitems)):  # calculate value of polynomial
    if (pitems[i]!="-") and (pitems[i]!="+"): #for not signs
        if ("x**" in pitems[i]): #cases if coeff 1 or not 1 with power
            if (pitems[i].startswith("x**")): # if item in p is having coeff not written i.e. by default 1 ex. x**4
                part = x ** int((pitems[i])[3:len(pitems[i])]) #indexing item to get raising value
                print("raisedpowernot1:",part)
            else: #if coeff from 1 to limit of int in python ,it also takes when written 1 as above if does not handle that ex. 1*x**4 or 5*x**1
                coeff=""
                for j in pitems[i]: # to get integer coeff by taking j till we encounter *
                    if (j=="*"):
                        break
                    coeff = coeff+j
                # now to calculate value of item with coeff other than 1 and with raised power
                # raising power is calculated by indexing item from after ** to end of pitem[i]
                part =int(coeff) * x ** int((pitems[i])[((pitems[i]).find("x"))+3:len(pitems[i])])
        elif (pitems[i].endswith("x")):
            # if item in p is having coefficeint 1 to limit of int in python and no power raising ex. 5x,1x,x
            if(pitems[i]=="x"): # for sepcifically x
                part=x
            else: # for if item ends in x but has a coeff like ex 1x,2x etc
                part = int((pitems[i])[0:len(pitems[i])-1])*x
            print("coeff1:",part)
        else:
            # if item is just a number ex. 3
            print(pitems[i])
            part = int(pitems[i])
            print("normal:",part)

        #below if and elif for 1st item in pitems
        if(i==1): #if for 1st item there is -sign then enter cuurent if and enounter this if
            value = value - part
        elif(i==0): #if for 1st item there is +sign then enter cuurent if and enounter this if
            value = value + part
        else: #for other items
            if(pitems[i-1]=="+"): #if + before current item
                value = value + part
            else: #if - before current item
                value = value - part

print(value)
if (value == k):
    print(True)
else:
    print(False)