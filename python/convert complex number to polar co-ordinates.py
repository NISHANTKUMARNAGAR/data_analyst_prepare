from math import sqrt,pow
from cmath import phase,complex
z=input()

def polar(real,img): #to prfloat polar coordinates
    r=sqrt(pow(real,2)+pow(img,2))
    ph=phase(complex(real,img))
    print("modulus:",r)
    print("phase:",ph)

#optimized version and include j,-j,all complex number containing e
#for only j or -j
if z == "j":
    z = "1j"
elif z == "-j":
    z = "-1j"
#for all 1,-1,5j,-5j,1+5j,1-5j,-1+5j,-1-5j
# if scientific notation present, use complex()
if "e" in z or "E" in z:
    z = complex(z) #not handling scientific notation by ourselves
    polar(z.real, z.imag)
else:
    if(z[0]!="-"): #real part is +ve
        startindex=0
    else: #real part is -ve
        startindex=1
    c=0
    for i in range(startindex,len(z)): #joined for loop for both +ve and -ve img part
        if (z[i] == "+" or z[i] == "-"):
            c = i #for finding if img part exists
            break
    if(c!=0): #if there is 2nd sign ,case with both img and real part
        polar(float(z[0:c]), float(z[c:].rstrip('j')))
    else: #no 2nd sign so only real(-5/5) or img part(-5j/5j)
        if (z[len(z) - 1] == "j"): #to check if its img
            polar(0, float(z[0:len(z) - 1]))
        else: # no j so only real part
            polar(float(z), 0)