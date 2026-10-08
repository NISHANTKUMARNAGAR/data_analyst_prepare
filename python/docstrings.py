def cube(n):
    '''this takes single integer and returns cube of it'''
    return n*n*n

c=cube(3)
print(c)

#there just after decleration line of function a string within triple quotes is written and its
#called a "docstring" they are used to document a code and to make clear what does that
#function or class or method or module do as in this always should be written just after the
#decleration line or otherwise it would not be considered as docstring.

#interpretor does not ignore docstring like it ignores comment

print(cube.__doc__)
#function/class/method/module name.__doc__
#can be used to print that docstring it will only be printed if docstring is written just after
#decleration

def square(o):
    p=o
    '''this will not be considered a docstring as not written after decleration line'''
    return p*p

s=square(4)
print(s)
print(square.__doc__) #shows none as interpretor understood it as comment

#can be used my any proggrammer to explain what that function/class/module/method
#does and any other person can just print it by
#print(function/class/module/method name.__doc__) no need to read all comment in that
#function to read and understood 
