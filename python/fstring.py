fname="nishant"
lname="nagar"

line="hello my first name is {} and my last name is {}"
print(line.format(fname,lname))

line="hello my first name is {1} and my last name is {0}"
print(line.format(lname,fname)) #as order of arguement is changed we have to mannually
                                                    #assign in brackets so if we had 10 arguments to assign it
                                                   #will be a hassale to remember their order and write in that
                                                    #string properly every time there is a new string

#so we use "F - string" makes interpolation (data insertion easier)
#format to use is to put f in front of every string

#example if we want to use fname and lname in a string initialise them above (already done)
print(f"hello my first name is {fname} and my last name is {lname}")
print(f"hello my name is {fname} {lname}")
#to print that string with curved brackets itself just put double curved brackets
print(f"hello my name is {{fname}} {{lname}}")

price=49.09999
print(f"final price is {price}")
print(f"final price is {price:.2f}")#we forced it to take only upto 2 decimal number thats why
                                                #it rounds of to 49.10
print(f"{2*60}")#we can also put arithmetic calucation in it

