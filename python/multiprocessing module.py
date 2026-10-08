#for creating and handling multiple processes manually
"""
import multiprocessing
import requests
def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"images/{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

url = "https://picsum.photos/2000/3000"
pros = []
for i in range(20):
    p = multiprocessing.Process(target=downloadFile, args=[url, i])
    p.start()
    pros.append(p)
for p in pros:
    p.join()"""

#using pool to handle processes
"""from multiprocessing import Pool
def process_task(task):
    print("task:",task)

if __name__=="__main__":
    task=[1,2,3,4,5,6,7,8,9,10]
    with Pool(4) as pool:
        results=pool.map(process_task,task)"""

#using queue to communicate between processes
"""import multiprocessing
def producer(queue):
    for i in range(10):
        queue.put(i)
    queue.put(None)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        else:
            print(item)

queue = multiprocessing.Queue()
p1 = multiprocessing.Process(target=producer, args=(queue,))
p2 = multiprocessing.Process(target=consumer, args=(queue,))
p1.start()
p2.start()"""

#using lock to allow only 1 process to use critical section
"""import multiprocessing
def increment(counter, lock):
    for i in range(10000):
        lock.acquire()
        counter.value += 1
        lock.release()

if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=increment, args=(counter, lock))
    p2 = multiprocessing.Process(target=increment, args=(counter, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Counter value:", counter.value)"""