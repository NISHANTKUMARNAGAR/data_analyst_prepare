'''
try:
    #l=[1,2]
    #for i in range(3):
    #    print(l[i])
    p=int(input('enter number'))
except IndexError as e:
    print(e)
except ValueError as v:
    print(v)
except:
    print('any other problem')
print("hello")'''
#------------------------------------------------
'''def f():
    try:
        l=[1,5,6,7]
        i=int(input('enter index'))
        print(l[i])
        return 1
    except:
        print('error')
        return 0
    finally:
        print('always')
x=f()
print(x)'''
#--------------------------------------------
'''n=int(input("enter a integer"))
if(n<5 or n>9):
    raise EOFError('not a valid answer')'''
#-------------------------------------------------
'''try:
    n=int(input('enter index'))
    l=[1,2]
    print(l[n])
except IndexError as i:
    print(i)
else:
    print('correct')'''
#----------------------------------------------------
'''try:
    x=-1
    assert x>0,'x must be +ve'
except AssertionError as e:
    print(e)'''
#-------------------------------------------------------
'''try:
    raise ValueError('Invalid',404)
except ValueError as e:
    print(e.args)
    print(e.args[0])
    print(e.args[1])'''
#--------------------------------------------------------
"""class InvalidEmailError(Exception):
    def __init__(self, email):
        self.email = email
        self.message = f"Invalid email format: '{self.email}'"
        super().__init__(self.message)

def validate_email(email_address):
    if "@" not in email_address:
        raise InvalidEmailError(email_address)
    print(f"Email '{email_address}' is valid.")

# Using the custom exception
try:
    validate_email("user@example.com")
    validate_email("invalid-email")
except InvalidEmailError as e:
    print(f"Caught a custom error: {e}")
except Exception as e:
    print(f"Caught a generic error: {e}")

# Example with a valid email
try:
    validate_email("test@example.com")
except InvalidEmailError as e:
    print(f"Caught a custom error: {e}")
"""

# ============================================================
# IMPORTANT EXCEPTION-HANDLING CONCEPTS
# ============================================================


# ------------------------------------------------------------
# 1. EXCEPTION HIERARCHY
# ------------------------------------------------------------

# Most normal runtime errors inherit from Exception.
# Exception itself inherits from BaseException.

# BaseException
# ├── Exception
# │   ├── ValueError
# │   ├── TypeError
# │   ├── ZeroDivisionError
# │   ├── FileNotFoundError
# │   └── ...
# ├── KeyboardInterrupt
# ├── SystemExit
# └── GeneratorExit

# Normally catch Exception, NOT BaseException.
# BaseException also catches things such as Ctrl+C (KeyboardInterrupt).

try:
    number = int("abc")
except Exception as e:
    print("Normal exception:", e)


# ------------------------------------------------------------
# 2. SPECIFIC EXCEPTION SHOULD BE CAUGHT BEFORE GENERAL ONE
# ------------------------------------------------------------

# Python checks except blocks from TOP to BOTTOM.
# Therefore, put specific exceptions before general exceptions.

try:
    number = int("abc")

except ValueError:
    print("ValueError")

except Exception:
    print("Some other exception")


# This would be WRONG:
#
# except Exception:
#     ...
# except ValueError:
#     ...
#
# ValueError would never reach its own except block because
# Exception already catches it.


# ------------------------------------------------------------
# 3. EXCEPTION PROPAGATION
# ------------------------------------------------------------

# If a function does not handle an exception, the exception
# moves back to the function that called it.
# This continues until some except block handles it.

def divide():
    return 10 / 0


def calculate():
    return divide()


try:
    calculate()

except ZeroDivisionError:
    print("Exception was propagated up to here")


# divide() -> calculate() -> try/except
#
# The exception travels up the call stack until handled.


# ------------------------------------------------------------
# 4. RE-RAISING AN EXCEPTION
# ------------------------------------------------------------

# "raise" without an exception inside an except block
# re-raises the SAME exception.

try:
    number = int("abc")

except ValueError:
    print("Logging the error...")
    raise


# Re-raising is useful when you want to:
# 1. do something locally (logging/cleanup)
# 2. still allow the exception to be handled by a higher level.


# ------------------------------------------------------------
# 5. EXCEPTION CHAINING
# ------------------------------------------------------------

# Sometimes one exception happens because another exception
# happened first.

try:
    number = int("abc")

except ValueError as e:
    raise RuntimeError("Could not process the number") from e


# "from e" explicitly says:
#
# RuntimeError was caused by this ValueError.
#
# This preserves the original cause and makes the traceback
# easier to understand.


# ------------------------------------------------------------
# 6. IMPLICIT EXCEPTION CHAINING (__context__)
# ------------------------------------------------------------

# Python can automatically remember the previous exception
# even without using "from".

try:
    number = int("abc")

except ValueError:
    # A new exception occurs while handling ValueError.
    raise RuntimeError("Another error occurred")


# Python internally records that the RuntimeError happened
# while handling the ValueError.
#
# This relationship is available through:
#
# exception.__context__


# ------------------------------------------------------------
# 7. SUPPRESSING EXCEPTION CONTEXT: "from None"
# ------------------------------------------------------------

try:
    number = int("abc")

except ValueError:
    # Hide the original exception from the displayed traceback.
    raise RuntimeError("Invalid input") from None


# "from None" means:
# Do not display the previous exception as the cause/context.


# ------------------------------------------------------------
# 8. FINALLY ALWAYS RUNS
# ------------------------------------------------------------

# finally is normally used for cleanup.
# It runs whether an exception occurs or not.

try:
    number = int("10")

except ValueError:
    print("Invalid value")

finally:
    print("This always runs")


# finally runs when:
# - no exception occurs
# - an exception is handled
# - an exception is not handled
# - return is used
# - break/continue is used


# ------------------------------------------------------------
# 9. FINALLY WITH RETURN
# ------------------------------------------------------------

def example():
    try:
        return 10

    finally:
        print("finally runs before the function returns")


print(example())


# Output:
# finally runs before the function returns
# 10


# IMPORTANT:
# A return inside finally can OVERRIDE a previous return.


def example():
    try:
        return 10

    finally:
        return 20


print(example())     # 20


# This is generally bad practice because it can hide
# exceptions or overwrite return values.


# ------------------------------------------------------------
# 10. FINALLY CAN OVERRIDE AN EXCEPTION
# ------------------------------------------------------------

def example():
    try:
        raise ValueError("Original error")

    finally:
        return "Exception was suppressed"


print(example())


# The ValueError disappears because the return in finally
# overrides the exception.
#
# Therefore, avoid return/break/continue inside finally
# unless you specifically need that behavior.


# ------------------------------------------------------------
# 11. EXCEPTION OBJECT: as e
# ------------------------------------------------------------

try:
    number = int("abc")

except ValueError as e:
    print(e)             # human-readable error
    print(str(e))        # string representation
    print(e.args)        # arguments used to create exception


# e is simply the exception object.
# You can inspect it or use its attributes.


# ------------------------------------------------------------
# 12. CUSTOM EXCEPTION WITH CUSTOM DATA
# ------------------------------------------------------------

class AgeError(Exception):

    def __init__(self, age, message):
        self.age = age
        self.message = message

        # Call Exception's constructor so the message is
        # also stored normally.
        super().__init__(message)


try:
    age = 15

    if age < 18:
        raise AgeError(age, "Age must be at least 18")

except AgeError as e:
    print(e)
    print(e.age)


# Custom exceptions can contain their own attributes/data.


# ------------------------------------------------------------
# 13. ASSERT vs RAISE
# ------------------------------------------------------------

# assert is mainly used to check assumptions during development.

age = 20

assert age >= 18


# If the condition is False:
#
# AssertionError is raised.


# raise is used when YOU intentionally want to raise
# an exception as part of program logic.

age = 15

if age < 18:
    raise ValueError("Age must be at least 18")


# Simple rule:
#
# assert -> "This condition should always be true."
# raise  -> "This is an actual error condition I want to handle."


# ------------------------------------------------------------
# 14. NESTED TRY/EXCEPT
# ------------------------------------------------------------

# try/except blocks can be placed inside other try/except blocks.

try:

    try:
        number = int("abc")

    except ValueError:
        print("Inner handler")

        # Re-raise the exception so the outer handler
        # can also deal with it.
        raise

except ValueError:
    print("Outer handler")


# The inner block gets the first opportunity to handle it.
# If it re-raises, the exception continues outward.


# ------------------------------------------------------------
# 15. RETURN vs RAISE
# ------------------------------------------------------------

def check_number(number):

    if number < 0:
        raise ValueError("Number cannot be negative")

    return number


# return -> gives a value back to the caller.
# raise  -> signals that something went wrong.


try:
    result = check_number(-5)

except ValueError as e:
    print(e)


# ------------------------------------------------------------
# 16. MULTIPLE EXCEPTIONS IN ONE BLOCK
# ------------------------------------------------------------

try:
    number = int("abc")

except (ValueError, TypeError):
    print("Either ValueError or TypeError occurred")


# Use a tuple when different exception types should
# receive the same handling.


# ------------------------------------------------------------
# 17. BARE except vs except Exception
# ------------------------------------------------------------

# Bare except catches virtually everything, including
# exceptions such as KeyboardInterrupt.

try:
    number = int("abc")

except:
    print("Something went wrong")


# Prefer:
#
# except Exception:
#
# because it catches normal program exceptions without
# also catching things such as Ctrl+C.


# ------------------------------------------------------------
# 18. ELSE + EXCEPTION HANDLING
# ------------------------------------------------------------

# else runs ONLY when the try block completed successfully.

try:
    number = int("100")

except ValueError:
    print("Invalid number")

else:
    print("Conversion successful:", number)

finally:
    print("Finished")


# Order:
#
# try
#   ↓
# exception? → except
#   ↓
# no exception → else
#   ↓
# finally → always runs


# ============================================================
# QUICK REVISION
# ============================================================

# try       -> code that might cause an exception
# except    -> handles the exception
# else      -> runs when NO exception occurred
# finally   -> runs regardless of what happened
# raise     -> manually raises an exception
# raise     -> inside except = re-raise the same exception
# raise X from e -> explicit exception chaining
# from None -> suppress displayed exception context
# assert    -> checks an assumption
#
# Exception hierarchy matters because:
# specific exceptions should be caught before general ones.
#
# Exception propagation means:
# an unhandled exception moves upward through the call stack.
#
# Custom exceptions:
# class MyError(Exception): ...
#
# "as e":
# gives access to the actual exception object.
#
# finally + return:
# can override both a previous return and an exception.
#
# ============================================================


#employee data validation question-------------------------------------------
"""records = [
    ["Aman", "25", "55000"],
    ["Riya", "twenty", "62000"],
    ["Karan", "31", "-5000"],
    ["Neha", "28", "70000"],
    ["Raj", "27"],
    ["Vikas", "35", "abc"],
    ["Vic1", "39", "900"]
]

class Wrongname(Exception):
    pass

class Employee:
    def __init__(self, n, a, s):
        self.name=n
        self.age=a
        self.salary=s

    def __str__(self):
        return str(self.name)+" "+str(self.age)+" "+str(self.salary)

Employees=[]
Invalid=[]
i = 1
for item in records:
    try:
        name = item[0]
        age = item[1]
        salary = item[2]
        if not str.isalpha(name):
            raise Wrongname("name is not purely alphabetical")
        if int(age)<=0:
            raise ValueError
        if int(salary)<0:
            raise ValueError
    except (TypeError,IndexError):
        e='wrong number of fields entered for employee:'+str(i)
        Invalid.append(e)
    except Wrongname as w:
        e = str(w) + " for employee:" + str(i)
        Invalid.append(e)
    except ValueError:
        e = "wrong age or salary entered" + " for employee:" + str(i)
        Invalid.append(e)
    else:
        obj = Employee(item[0], int(item[1]), int(item[2]))
        Employees.append(obj)
    i=i+1

for valid in Employees:
    print(valid)
print("Number of Valid Employees:",len(Employees))
print("Number of Invalid Employees:",len(Invalid))
for item in Invalid:
    print(item)"""

#banking class-exception  question------------------------------------------
"""transactions = [
    ["A101", "deposit", "5000"],
    ["A102", "withdraw", "2000"],
    ["A101", "withdraw", "7000"],
    ["A103", "transfer", "1000"],
    ["A102", "withdraw", "abc"],
    ["A999", "deposit", "500"],
    ["A101", "deposit", "-200"],
]

class InvalidDepositValue(Exception):
    pass

class AccountNotFound(Exception):
    pass

class TransactionNotSupportedError(Exception):
    pass

class InsufficientBalance(Exception):
    pass

class NegativeWithdrawalValue(Exception):
    pass

class Account:
    def __init__(self,ano,n,b):
        self.number=ano
        self.name=n
        self.balance=b

    def __str__(self):
        return str(self.number)+" "+str(self.name)+" "+str(self.balance)


a1=Account("A101","Aman",10000)
a2=Account("A102","Riya",5000)
a3=Account("A103","Karan",8000)
accounts={a1.number:a1,a2.number:a2,a3.number:a3}

Invalid=[]
i=1

for item in transactions:
    try:
        a=accounts[item[0]]

        if item[1]=="deposit":
            amount = int(item[2])

            if amount<=0:
                raise InvalidDepositValue

            a.balance = a.balance + amount

        elif item[1]=="withdraw":
            amount = int(item[2])

            if amount<=0:
                raise NegativeWithdrawalValue

            if amount>a.balance:
                raise InsufficientBalance

            a.balance = a.balance - amount

        else:
            raise TransactionNotSupportedError

    except KeyError:
        Invalid.append("account for transaction number " + str(i) + " not found")

    except ValueError:
        Invalid.append("transaction number "+ str(i) + " not possible because of invalid transaction value type")

    except InvalidDepositValue:
        Invalid.append("transaction number " + str(i) + " not possible because of negative deposit value")

    except TransactionNotSupportedError:
        Invalid.append("transaction number " + str(i) + " not supported")

    except InsufficientBalance:
        Invalid.append("transaction number " + str(i) + " not supported due to insufficient balance")

    except NegativeWithdrawalValue:
        Invalid.append("transaction number " + str(i) + " not supported due to negative withdrawal value")

    i=i+1


for item in accounts:
    print(accounts[item])

print("successful transactions:",len(transactions)-len(Invalid))
print("failed transactions:",len(Invalid))

for item in Invalid:
    print(item)"""

