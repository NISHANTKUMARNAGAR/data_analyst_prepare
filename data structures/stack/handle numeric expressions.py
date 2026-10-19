s = "18-4*3+24/5*2-7+6*4/3-10/4"
op_stack=[]
num_stack=[]
i=len(s)-1

while i>=0: #handle all *,/ coming and put all +,- on top of stack
    if s[i].isdigit(): #if digit just put in number stack
        flag=i
        while i>=0 and s[i].isdigit():
            i=i-1
        num_stack.append(int(s[i+1:flag+1]))
    elif s[i] in {'+','-','/','*'}: #if digit check
        if len(op_stack)!=0 and (s[i]=='-' or s[i]=='+') and (op_stack[-1]=='*' or op_stack[-1]=='/'): #if +,- came when *,/ are on top of stack
            while len(op_stack)!=0 and (op_stack[-1]=='*' or op_stack[-1]=="/"): #solve all *,/ that are on top
                if op_stack[-1]=="*":
                    op_stack.pop()
                    temp = num_stack.pop() * num_stack.pop()
                elif op_stack[-1]=="/":
                    op_stack.pop()
                    temp = num_stack.pop() // num_stack.pop()
                num_stack.append(temp)
            op_stack.append(s[i]) #then add that +,- on top of stack
        else: #all other cases when *,/ come and +,- on top or empty op_stack just add that operator
            op_stack.append(s[i])
        i=i-1

#now when all *,/ have been solved we solve -,+
while len(op_stack)!=0:
    if op_stack[-1]=='+':
        op_stack.pop()
        temp=num_stack.pop()+num_stack.pop()
    elif op_stack[-1]=='-':
        op_stack.pop()
        temp=num_stack.pop()-num_stack.pop()
    num_stack.append(temp)

#return top of num_stack
print(num_stack[-1])