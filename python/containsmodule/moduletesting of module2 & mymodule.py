#import mymodule as m
import math
import sys
print('printing path')
print(sys.path)
from module2 import w as p
from mymodule import w as q
def w():
   print('function in test')
w()
#p()
q()
p()
#print(v)
print(dir(math))
x=5
print(globals())