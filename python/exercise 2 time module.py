import time
h=int(time.strftime('%H'))
m=int(time.strftime('%M'))
s=int(time.strftime('%S'))

if(h>=00 and h<12):
    print("it is am")
    if(h>=6 and h<8):
        print("good morning")
    elif(h>=8 and h<12):
        print("you got up late and good morning")
elif(h>=12 and h<=23):
    print("then its pm")
    if(h>=12 and h<18):
        print("good afternoon")
    elif(h>=18 and h<21):
        print("good evening")
    elif(h>=21 and h<23):
        print("good night")
    elif(h==23):
        if(m>=00 and m<=59):
            print("good night")

print("time is :",time.strftime('%H:%M:%S')) 
