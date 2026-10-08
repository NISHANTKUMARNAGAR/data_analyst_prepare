v=5
def w():
    i=9
    print('function being called from mymodule')
    print(locals())
print("always")
print(__name__)
if __name__=='__main__':
    print('inside if')
    w()