#executing on a single thread as per gil(global interpreter lock)
"""The Global Interpreter Lock (GIL) in Python is a mutex (mutual exclusion lock)
 that ensures only one thread can execute Python bytecode at any given time within a single Python process.
"""
import asyncio

async def func1():
    print("func1")
    await asyncio.sleep(2)
async def func2():
    print("func2")
    await asyncio.sleep(2)
async def func3():
    print("func3")
    await asyncio.sleep(2)

async def main():
    """await func1()
    await func2()
    await func3()"""
    #just above was sequential execution code time used 6 sec
    await asyncio.gather(func1(),func2(),func3())
    #just above is concurrent or simultaneous executable version time used 2 sec

asyncio.run(main())