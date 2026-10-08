'''string are immutable hence whenever we perform a function on string it always makes
a copy of it and then performs the function on it and not on the orignal string ie once
created it is immutable but as we cant change it string we can overrde it with another
ie by declaring it again as python always takes the latest decleration of the any variable if
declared more than one time'''

# STRING BASIC

name="nishant"
srname=" nagar"

print(name+srname)
print("hello "+name+srname)
print("hello "+name+srname+" i am 23 years old")

"""a="my name is nishant
 and i said \"my cousion is dumber than all people\""""#this is commented

a='''my name is nishant
 and i said \"my cousion is dumber than all people\" '''

print(a)

print(a[0])
print(srname[1])

'''for character in a:
    print(character)'''

#STRING SLICING AND OPERATIONS IN STRING


a="my name is nishant and i said \"my cousion is dumber than all people\""

print(len(a))
print(a[0:67])
print(a[67])

print('printing slice')
print(a[:4])
print(a[:]) #it automatically puts 0 at left and string length at left of colon(:)
print(a[15:25])
print(a[-20:-5]) #it always subtracts from string length ie here 68 so a[48:63]
print(a[-5:-20]) #will give no result as a[63:48] does not make sense

#STRING METHODS

a="my name is nishant and i said \"my cousion is dumber than all people\""
print("hello")
print(a.upper())
print(a.lower())

b="      ram    "
print(b)
print(b.strip()) # removes any white spaces before and after the string
#if want to use in map() use str.strip because strip is not a global function

c="ram$$$$$$$$$$"
print(c.rstrip("$")) # remove any trailing character

d="raam"
print("printing d")
print(d.replace("a","o"))
print(d.replace("a","o",1))

e="nishant nagar"

print(e.split(" "))
print(e.split("h"))    #split() splits at specific character and also removes that character

print("1st letter capital")
print(e.capitalize()) #only capitalize 1st character of string

print(e.center(50)) #it centers the string between given number of spaces
print(e.center(50,"-")) #it can also do the filling of any other character

print(e.count("a")) #can count the times a character has appeared

print(e.endswith("r"))
print(e.endswith("e"))
print(e.startswith("nishant"))

print(e.find("nagar"))
print(e.find("hello"))
print(e.rfind("hello"))

print(e.index("nagar"))
#print(e.index("hello"))

# so there both index() and find() gives the index value if it can find the character
#but if it cant find only gives -1 but index gives raises exception

print(e.isalnum()) #only alphabets and numbers present
print(e.isalpha()) #only alphabets present gives false as there is a space(" ") in string
print(e.islower()) #only lowercase present
print(e.isupper()) #only uppercase
print(e.isprintable()) 

f="nishant\n"
print(f.isprintable())  #if  printable characters are present its false because "\n" not a printable

g="     "
print(g.isspace()) #true only if it contains only spaces given by spacebar or tab

print('is e a title:',e.istitle())

g="Hello World"
print(g.istitle()) #onyl true if first letter of each word is capital

print(e.swapcase()) #swapcase returns a new string with swapped characters so if not printed
                    # directly you have to assign new string to a variable then print that new variable

h="8eema gothwal"
print(h.title())

s='ABCDE'
#print(s.rjust(11,' '))
#print(' '.join(s))