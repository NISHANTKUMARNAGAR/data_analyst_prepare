x=int(input("enter a number "))

match x:
    case _ if x*2==10:
        print("number is 5")
    case 9:
        print("number is 9")
    case 4:
        print("number is 4")
    case _:
        print("number does not match")

#----------------------------------------------------------------------------------------------


n=input("give me your name")

match n:
    case "naman":
        print("he is oversmart")
    case "nishant":
        print("he is smart")
    case "seema":
        print("she is dumb")
    case _ if n.find("pradeep")==0:
        print("he is father")
    case _:
        print("does not matter")
