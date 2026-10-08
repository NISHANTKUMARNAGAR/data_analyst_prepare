#lru_cache and cache-----------------------------------------------------------------------------------
"""from functools import lru_cache
import time

@lru_cache(maxsize=None) #lru=last recently used
def func(n):
    time.sleep(2)
    return n*n

l=[1,2,3,4,3,2,1,9]
for i in l:
    print(func(i))

print(func.cache_info()) #gives -hit,miss,currsize,maxsize i.e. data about cache and only for cache_info
func.cache_clear()"""

#caching only works on hashable arguements like integers,tuple not list
#lru_cache is bounded to 128 enteries by default and its slower, when filled clears earliest values
#cache can be used its unlimited by default and its faster, can cause memory leak as it doesn't clear by itself

#partial --------------------------------------------------------------------------------------------------
"""
#creates a function calling handle with fixed parameter
#keep that fixed parameter at the end of arguments
from functools import partial
def multiply(a, b):
    return a * b

double = partial(multiply, 2)
print(double(5))"""


#singledispatch-----------------------------------------------------------------------------------------
#can write diff implementation on type of arguments to the function
"""from functools import singledispatch

@singledispatch
def process(value):
    print("Default")

@process.register
def _(value: int):
    print("Integer")

@process.register
def _(value: str):
    print("String")

process(10)
process("hello")"""