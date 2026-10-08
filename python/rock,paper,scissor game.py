import random as r
l=['rock','paper','scissor']
lc=r.choice(l)
u=input("give one from rock paper scissor ")
print('computer chooses',lc)
if(lc==u):
    print('tie')
elif((lc=="rock" and u=="scissor") or (lc=="paper" and u=="rock") or (lc=="scissor" and u=="paper")):
    print("computer wins")
else:
    print("user wins")