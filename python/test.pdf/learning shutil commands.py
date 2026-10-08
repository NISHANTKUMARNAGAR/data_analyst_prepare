import shutil
import os

p=os.getcwd()
print(p)
#shutil.copy("copy.txt",p+'\shutil module practice\copy2.txt')
#shutil.copy2("copy.txt",p+'\shutil module practice\copy2.txt')
#os.remove(p+'\shutil module practice\copy2.txt')
#shutil.copytree("shutil test dir",p+"\\shutil module practice\\test dest dir")

shutil.move(p,"C:\\Users\\NISHANT NAGAR\\PyCharmMiscProject\\practice python\\test.pdf")
#shutil.rmtree(p+"\\shutil module practice - Copy")
