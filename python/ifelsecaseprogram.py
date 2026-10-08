a=int(input("enter your age: "))

if(a>=18):
    print("you can vote")
else:
    print("you cant vote")

#------------------------------------------------------------------

a=int(input("enter your percentage"))

if(a>=90 and a<=100):
    print("grade A")
elif(a>=80 and a<90):
    print("grade B")
else:
    print("grade C")

print("i gave the exam")

#----------------------------------------------------------------


if(input("did you give the exam enter yes or no : ")=="yes"):  #enter yes or no
    a=int(input("enter your percentage"))
    if(a>=90 and a<=100):
        print("grade A")
    elif(a>=80 and a<90):
        print("grade B")
    else:
        print("grade C")
else:
    print("you fail")
