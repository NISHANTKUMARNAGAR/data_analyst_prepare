import threading
import time
#single thread
"""def myfunc():
    print("hello",threading.current_thread().name)

t1=threading.Thread(target=myfunc)
t1.start()
t1.join()"""

#multiple therad
"""def func(s):
    print(f"sleeping for {s} seconds")
    time.sleep(s)
    return s

def main():
    time1=time.perf_counter()
    t1 = threading.Thread(target=func,args=[4])
    t2 = threading.Thread(target=func, args=[3])
    t3 = threading.Thread(target=func, args=[1])
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    time2=time.perf_counter()
    print(time2-time1)

main()"""

#using lock btw multiple threads
# Define the global counter and lock at the module level.
# This makes them accessible to all threads.
"""counter = 0
lock = threading.Lock()


def increment():
    # Use the 'global' keyword to modify the global variable 'counter'.
    global counter

    # Each thread will run this loop 10,000 times.
    for _ in range(10000):
        # The 'with' statement ensures the lock is automatically
        # acquired before the block and released after the block,
        # even if an error occurs.
        with lock:
            counter += 1


if __name__ == '__main__':
    threads = []
    # Create and start two threads.
    for _ in range(2):
        # No arguments are needed for the target function since it accesses
        # the global 'counter' and 'lock'.
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    # Wait for both threads to complete their execution.
    for thread in threads:
        thread.join()

    # The final value will be 20,000 (2 threads * 10,000 increments).
    print("Counter value:", counter)
"""