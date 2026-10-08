#FOR normal process request io bound
"""import requests
from concurrent.futures import ProcessPoolExecutor

def downf(u,n):
    print(f"start {n}")
    response=requests.get(u)
    open(f"images/{n}.jpg","wb").write(response.content)
    print(f"end {n}")

url="https://picsum.photos/2000/3000"
with ProcessPoolExecutor() as p:
    l1=[url for i in range(20)]
    l2=[j for j in range(20)]
    results=p.map(downf,l1,l2)

"""

#for cpu bound
"""from multiprocessing import Pool
import time

def square(n):
    print(f"Processing {n}")
    s = sum(i * i for i in range(100000000))  # heavy computation
    return s

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    start = time.perf_counter()
    with Pool(processes=4) as pool:
        results = pool.map(square, nums)
    end = time.perf_counter()
    print(f"Results: {results}")
    print(f"Total time: {end - start:.2f}s")"""