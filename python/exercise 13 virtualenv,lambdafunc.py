'''question 2
m,n,p=90,'pk',8678786787
print(f"{n} is student has phone number {p} has marks {m}")
print("{} is student has phone number {} has marks {}".format(n,p,m))
print("{2} is student has phone number {1} has marks {0}".format(m,p,n))'''

'''question 3
l=[7,14,21,28,35,42,49,56,63,70]
l1=list(map(str,l))
p='\n'.join(l1)
print(p)
print(type(p))'''

'''question 4
l=[25,3467,2389,250,4232,434,42,5,43]
print(list(filter(lambda x:x%5==0,l)))'''

'''question 5
from functools import reduce
l=[25,3467,2389,250,4232,434,42,5,43]
print(reduce(lambda x,y:x if x>y else y if y>x else x,l))'''

'''question 6
pip freeze > r.txt
python -m venv newenvname
newenvname\Scripts\activate.bat
pip install -r r.txt
pip list
deactivate'''