import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(s):
    print(f"Sleeping for {s} seconds")
    time.sleep(s)
    return s

def poolingDemo():
    with ThreadPoolExecutor() as e:
        l = [3, 5, 1, 2]
        results = e.map(func, l)
        #this map function preserves starting order
        #thats why you will see 3,5,1,2 when printing result
        #regardless of 1 fuinishing first
        for result in results:
            print(result)

poolingDemo()