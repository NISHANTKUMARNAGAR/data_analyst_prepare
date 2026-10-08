from math import sqrt,pow,acos,degrees
AB=int(input())
BC=int(input())
AC=sqrt(pow(AB,2)+pow(BC,2)) #pythagoras theorom
MC=BM=AC/2
MBC=round(degrees(acos((pow(BM,2)+pow(BC,2)-pow(MC,2))/(2*BM*BC)))) #law of cosine
print(str(MBC)+"\u00B0")