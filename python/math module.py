import math
print('1:',math.sqrt(16))
print('2:',math.ceil(9.43))
print('3:',math.floor(9.43))
print('4:',math.factorial(25))
print('5:',math.pow(3,4))
print('6:',math.pow(1.0,9))
print('7:',math.pow(9,0.0))
print('8:',math.pow(1.0,3.0))
print('9:',math.pow(-3,3)) #cant use float as arguements
print('10:',math.pow(0.0,float('-inf')))
print('11:',math.pow(-0.0,float('-inf')))
print('12:',math.log10(2))
print('13:',math.log(2,10))
print('14:',math.pi)
print('15:',math.e)
print('16:',math.acos(2/math.sqrt(5)))
r=math.acos(2/math.sqrt(5))
print('17:',math.degrees(r))

import cmath
print('18:',cmath.phase(complex(-1.0,0.0)))
z=1+5j
print('19:',cmath.polar(z))

print('20:',abs(complex(-1.0,0.0)))
d=math.degrees(r)
print('21:',round(d))
print('22:',divmod(177,10))
print('23:',pow(2,5,3))
