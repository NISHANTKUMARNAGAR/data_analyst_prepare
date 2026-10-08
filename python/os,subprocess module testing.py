#---------------------------------------os
import os
n='o.txt'

"""f=os.open(n,os.O_RDONLY)
print((os.read(f,1024)).decode("utf-8")) #1024 are number of bytes & are converted to utf for reading
os.close(f)
print((os.read(f,1024)).decode("utf-8"))"""

"""if not os.path.exists('one'):
    os.mkdir("one")
for i in range(5):
    os.mkdir(f"one/d{i+1}")
    os.rename(f"one/d{i+1}",f"one/p{i+1}")

print(os.listdir("one"))

print(os.getcwd())
print(os.listdir(os.getcwd()))
print(os.environ)
print(os.getenv(os.getcwd()))"""


#-----------------------------------------------subprocess
import subprocess

result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print(result.stdout)


