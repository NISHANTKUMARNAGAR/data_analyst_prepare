s = "{[}"
stack=[]
opening=['{','[','(']
closing=['}',']',')']
flag=0

if len(s)!=0:
    for item in s:
        if item in opening:
            stack.append(item)
        elif item in closing:
            if len(stack) != 0:
                c = stack.pop()
                if closing.index(item) == opening.index(c):
                    continue
            #if only one closing/bracket not matched
            flag=1
            break #only exec

    if flag==0 and len(stack)==0:
        print(True)
    else:
        print(False)
else:
    print('empty sequence')