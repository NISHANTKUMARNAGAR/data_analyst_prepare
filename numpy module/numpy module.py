import numpy as np
import sys
import time

#speed comparison
#python list is fast for small list but for larger numpy array is faster
"""l=range(10000000)
x=time.time()
double=[item*2 for item in l]
y=time.time()
print(y-x) #takes way more time in python list
arr=np.array(l)
a=time.time()
doublearr=arr*2 
b=time.time()
print(b-a) #takes very less time in python list
"""

#size comparision
"""print("calulating difference in size of numpy array and normal python list")
lst=range(1000)
size=sys.getsizeof(1)*len(lst)
print("size of python list")
print(sys.getsizeof(1))
print(size)
print("size of numpy list")
nplst=np.arange(1000)
size1= nplst.size * nplst.itemsize
print(nplst.itemsize)
print(size1)"""

#creating nd array from python list
"""a=np.array([1,2,3])
b=np.array([[1,2,3],[4,5,6]])
print(type(b))
print(b.shape) #row,col
print(b.size) #total number of elements
print(b.ndim) #number of dimensions
print(b.dtype) #datatype of elements in array
c=np.array([[[1,2],[1,2]],[[2,3],[2,3]]])
print(c) #array containing 2 , 2d arrays
arr = np.array([
    [
        [[1,2],[3,4]],
        [[5,6],[7,8]]
    ],
    [
        [[9,10],[11,12]],
        [[13,14],[15,16]]
    ]
])
print(arr) #its a shape 2,2,2,2 i.e. 2 groups each having 2 matrices having 2 row and 2 column
"""

#creating other types of numpy array
#every ine of these give float64 values until int mentioned
'''print(np.zeros(2,int))
print(np.ones(2,int)*5)
print(np.zeros((2,3),int))
print(np.ones((2,3),int))
print(np.ones((3,3,3))) #three 3by3 array's having 1's type=float64
print(np.ones((4,3,2,2)))
#2by2 array 3 times then that 4 times containing 1's
#it works by making 4 blocks of 3 blocks of 2 row of 2 col
#last two values will always be row then col before that
#take blocks then blocks
print(np.full((2,3),7,int))
print(np.eye(3,3,0,int))
#.eye has row,col,default 0 for diagonal,datatype
print(np.eye(3,3,1,int)) #1 upper or start from 1 upper column digonal
print(np.eye(4,4,-2,int)) #2 lower or start from 2 lower row diagonal
print(np.identity(3,int)) #identity matrix of size 3 having int values
print(np.arange(5))
print(np.arange(1,9))
print(np.arange(1,10,2))
print(np.linspace(0,10,5,dtype=int))'''

#indexing and slicing
"""q=np.array([10,20,30,40])
print(q[0])
print(q[1:3])
p=np.array([[1,2,3],[4,5,6]])
print(p[0,0])
print(p[1,2])
print(p[:,1])
print(p[1,:])
r=np.array([10,20,30,40,50])
mask=r>20 #Boolean Indexing
print(mask)
print(r[mask])
print(r[r>20])
r[r>20]=100
print(r)"""

#vectorized operation
"""a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(b-a)
print(a*b)
print(b%a)
print(a**2)
print(a/b) #division
print(a//b) #floor_divide i.e. divide then floor OR integer divide
"""

#different array working together
"""a=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20,30])
print(a+b)
c=[20]
print(a+c)
d=20
print(a+d)"""

#aggregation functions
"""a=np.array([[1,2,3],[4,5,6]])
print(a.min())
print(a.min(axis=0))
print(a.max())
print(a.max(axis=1))s
print(a.sum())
print(a.sum(axis=1))
print(a.sum(axis=0))
print(a.mean())
print(a.var()) #variance of whole array
print(a.var(axis=0)) #variance per column
print(a.var(axis=1)) #variance per row
print(a.std()) #standard deviation
std_dev=a.std()
#std=sqrt(var)"""

#reshape and transpose
"""a=np.arange(6)
b=a.reshape(2,3) #reshape is called on numpy array
print(b)
e=np.array([[1,2,3],[4,5,6]])
e.shape=(3,2)
print(e)
c=b.flatten() #.ravel()/.flatten() works similarly
print(c)
d=b.T #.T or .transpose() works similarly
print(d)"""

#stacking and concatenating
"""a=np.array([[1,2],[3,4]])
b=np.array([[5,6]])
print(np.vstack([a,b]))
c=np.array([[5],[6]])
print(np.hstack([a,a]))
print(np.hstack([a,c]))
print(np.concatenate([a,b],axis=0)) 
print(np.concatenate((a,b)))
#concatenate axis=0 is like vstack and 1 is like hstack
#by default concatenate takes 0 as axis value"""

#utiity functions
"""a=np.array([1,1,2,3,4,5])
print(np.unique(a))
print(np.unique(a,return_counts=True)) #gives unique elemnts
a3 = np.array([[20, 20, 20, 0],
               [0, 20, 20, 20],
               [0, 20, 20, 20],
               [20, 20, 20, 0],
               [10, 20, 20, 20]])
print(a3.shape)
print(np.unique(a3,axis=0)) #if mention axis=0 gives unique row
print(np.unique(a3,axis=1)) #if mention axis=1 gives unique column
b=np.array([14,11,12,3,4,5])
print(np.sort(b))
print(np.argsort(b)) #gives indices of sorted values
                    # with respect to original array
c=np.array([10,20,30,40,50])
print(np.where(c>25))
print(np.where(c>25,1,0)) #if false give 0 ,true give 1
d=np.array([-5,0,10,20])
print(np.clip(d,0,15)) #clips or binds items to 0 to 15
"""

#math functions
"""a=np.array([1.22323,1.5,1.8])
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a)) #(round to nearest int)
print(np.round(a, 2))  #(round to N decimal places)"""

#basic linear algebra
"""a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print(a @ b) #dot product
print(np.dot(a,b))
print(np.linalg.det(a)) #determinant
print(np.linalg.inv(a)) #inverse
print(np.linalg.eig(a)) #eigrnvalue and eigenvector"""

#special function to trim large decimal values
#num = number to be trimmed
#n = the no. of digits after places we want just replace 11
"""def trim(num, n=11):
    s = ('{0:.%df}' % n).format(num)  # round to n decimals
    if '.' in s:
        s = s.rstrip('0').rstrip('.')  # remove extra zeros if less numbers than 11 after .
    if s == '0':                      # special case of 0
        return '0.0'
    return s"""

#other important functions ----------------------------------------------------------------------------------------
"""
print(np.__version__)

arr=np.array([1,3,7,11])
print('1',arr.size*arr.itemsize)

print('2',np.zeros(10)) #10 zeros
print('3',np.ones(10)) #10 ones
print('4',np.ones(10)*5) #10 fives
print('5',np.arange(30,70,2)) #even values from 30 to 70

print('6',np.identity(3)) #identity matrix of size 3
print('7',np.random.normal(0,1,15))
p=np.arange(12)
p.shape=(3,4)
print('8',p)
for item in np.nditer(p):
    print(item,end=" ")

print("\n")
for item in np.nditer(p,op_flags=['readwrite']):
    item[...]=item*2
    print(item,end=" ")

print('\n')
a=np.arange(21)
for item in np.nditer(a,op_flags=['readwrite']):
    if 8<item and item<16:
        item[...]=item*-1

a[(a >= 9) & (a <= 15)] *= -1
print('9',a)

b=np.random.randint(1,10,5)
print('10',b)

c=np.array([1,2,3])
d=np.array([4,6,5])
e=c*d
print('11',e)

f=np.arange(10,22).reshape(3,4)
print('12',f)
print('13',f.shape)

g=np.identity(3,int)
print('14')
print('14',g)

h=np.ones((10,10),int)
h[1:-1,1:-1]=0
print('15',h)

i=np.identity(5,int)
i[1,1]=2
i[2,2]=3
i[3,3]=4
i[4,4]=5
print('16')
print(i)

j=np.arange(27).reshape((3,3,3))
print('17')
print(j)

print('18',np.random.uniform(0,1))

k=np.array([[1,2],[3,4]])
print('19',(k.sum(axis=0))[0]) # 1st column sum
print('20',(k.sum(axis=0))[1]) # 2nd column sum
print('21',(k.sum(axis=1))[0]) # 1st row sum
print('22',(k.sum(axis=1))[1]) # 2nd row sum

l=np.array([1,345,32,52])
m=np.array([1,12,64,12])
print('23',np.dot(l,m))

n=np.array([1,2,3])
o=np.array([1,2,3,4,5,6]).reshape(2,3)
print('24',n+o)

p=np.array([1,2,3,4,5])
p_bytes=p.tobytes()
print(p_bytes)
p2=np.frombuffer(p_bytes,dtype=p.dtype)
print(p2)
print(np.array_equal(p,p2))

l=[1,2,3]
q=np.array(l)
l1=q.tolist()
print(l==l1)

m=np.float32(0)
print(type(m))
n=m.item()
print(type(n))

add=0
o = np.array([[1, 1, 0, 2],[0, 3, 0, 3],[1, 0, 4, 4]])
for i in range((o.shape)[0]): #every row
    for j in range((o.shape)[1]): #every column
        if 0<=i-1<(o.shape)[0] and o[i-1,j]==0:
            continue
        add=add+o[i,j]

print(add)

onedigit=np.arange(0,10)
twodigit=np.arange(10,100)
threedigit=np.arange(100,1000)
p=np.concatenate((onedigit,twodigit,threedigit))
print(p)

q=np.random.uniform(0,1,40)
print(q)

r=np.random.normal(200,7,40)
r.reshape(8,5)
print(r)

s=np.array([[1,2],[3,4]])
s[[0,-1],:]=s[[-1,0],:]
print(s)

t=np.zeros((5,6),int)
print(t)

u=np.array([[5,3],[4,1]])
print(np.sort(u)) #row wise sort
print(np.sort(u,axis=0)) #col wise sort

v = np.array([[5.54, 3.38, 7.99],
              [3.54, 8.32, 6.99],
              [1.54, 2.39, 9.29]])
print("Original array:")
print(v)
print("\nNew array of equal shape and data type of the said array filled by 0:")
print(np.empty_like(v))

w=np.arange(27).reshape(3,3,3)
print(w)

x=np.array([1,2,3,4]).reshape(1,4)
#other way
x[:,[0,3]]=x[:,[3,0]]
x[:,[1,2]]=x[:,[2,1]]
#other way
x=x[:,::-1] #swapping 1st and last,2nd and 3rd col
print(x)

y=np.array([[1,2],[3,4]])
y=y[::-1,::-1]
print(y)

z=np.array([1,2])
z1=np.array([3,4])
print(z*z1)

a1=np.random.randint(2,10,27).reshape(3,3,3)
print(a1)

b1=np.zeros(10)
b1[6]=np.float32(11)
print(b1)

c1=np.arange(12,20)
print(c1)
c1[[-1,0]]=c1[[0,-1]]
print(c1)
c1=c1[::-1]
print(c1)

d1=np.arange(1,6)
d2=np.float32(d1)
print(d2)

e1=np.ones((4,4),int)
print(e1)
e1[1:-1,1:-1]=0 #border 1,inside 0
print(e1)

f1=np.ones((2,2),int)
f1=np.pad(f1,pad_width=1,mode='constant',constant_values=0)
print(f1)

g1=np.zeros((8,8),int)
g1[1::2,::2]=1
g1[::2,1::2]=1
print(g1)

h1=np.array((1,2,3,4,5,6)).reshape(2,3)
print(h1) #tuple into array

il=[[1,2,3],[4,5,6]]
il=np.append(il,np.array([7,8,9]))
print('appending a array to array:',il)

j1=np.empty((3,3),dtype=int)
j2=np.full((3,3),6)
print(j1)
print(j2)

k1=np.array([1+2j,2+0.40j])
print(k1.real)
print(k1.imag)

l1=np.array([1,2,3])
print('total number of ele: ',l1.size)
print('size of 1 item: ',l1.itemsize)
print('total size: ',l1.size*l1.itemsize)

m1=np.array([[1,2],[4,3]])
n1=np.array([1,3])
print(np.isin(m1,n1))
print(m1[np.isin(m1,n1)]) #common

o1=np.array([10,20,30,10,60,30])
print(np.unique(o1))

p1=np.array([10,20,30])
p2=np.array([10,40])
print(np.setdiff1d(p1,p2))
print(np.setxor1d(p1,p2))
print(np.union1d(p1,p2))

q1=np.array([10,20,np.nan,np.float32('inf'),0])
print(any(q1))

r1=np.array([1,2,3])
x=np.tile(r1,2)
print(x)

s1=np.repeat(3,4)
print(s1)
s2=np.repeat([1,2,3,4],2)
print(s2)

t1=np.array([[3,1],[3,7]])
print(np.argmax(t1,axis=0))
print(np.argmax(t1,axis=1))
print(np.argmin(t1,axis=0))
print(np.argmin(t1,axis=1))
print(np.sort(t1,axis=0))
print(np.sort(t1,axis=1))
t2=np.array([2,2,51,24])
print(np.argmax(t2))
print(np.argmin(t1))

u1=np.array([1,2,3])
u2=np.array([3,4,3])
print(np.greater(u1,u2))
print(np.greater_equal(u1,u2))
print(np.less(u1,u2))
print(np.less_equal(u1,u2))
print(np.equal(u1,u2))
print(np.array_equal(u1,u2))

print('\nhere v1')
v1=[[ 0,10,20],[20,30,40]]
#v1=[0,10,20,20,30,40]
v1=np.array(v1)
print(np.where(v1>10))

print(np.zeros((3,3),dtype=int))
print(np.ones((3,3)))

w1=np.array([1,2,3,4,5,6,7,8,9])
w1.shape=(3,3)
print(w1)
w2=np.array([[1,2,3],[4,5,6]])
print(w2.shape)
print(w2.dtype)
print(w2.ravel())
w2=np.float64(w2)
print(w2.dtype)
print(w2)

x1=(np.ones((3,5),dtype=int))*2
shape=x1.shape
x2=np.ones((15))*10
x2.shape=shape
print(x2)

print(np.identity(3))
print(np.diag([4,5,6,8]))
print(np.linspace(2.5,6.5,30))

y1=np.arange(2,14).reshape(4,3)
y2=np.triu(y1,-1)
print(y2)
print(y2.flatten())

print(np.tril([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], -1))

z1=np.array([[1,2],[4,5]])
print(z1.flat[3])
print(z1)

a2=np.array([[1,2,3]]).reshape(3,1)
print(a2)

b2=np.zeros((2,3,4))
print(np.moveaxis(b2,0,1).shape)
print(np.swapaxes(b2,0,-1).shape)

c2=[[1,2,3],[4,5,6]]
print(np.atleast_1d(c2))

d2=np.arange(12).reshape(3,4)
print(d2)
print(np.expand_dims(d2,axis=2))

e2=np.array([[1,2],[3,4]])
f2=np.array([[5,6],[7,8]])
print(np.concatenate((e2,f2)))

g2=np.array([10,20,30])
h2=np.array([40,50,60])
print(np.column_stack((g2,h2)))
g2.shape=(3,1)
h2.shape=(3,1)
print(np.hstack([g2,h2]))

i2=np.array([1,2,3])
j2=np.array([4,5,6])
result=np.dstack((i2,j2))
print(result)
print(result.shape)

k2=np.arange(1,15)
print(np.split(k2,[7])) #divide at 7 index i.e. 2 parts
print(np.split(k2,7)) #divide in 7 equal parts

l2=np.arange(16).reshape(4,4)
print(np.split(l2,2,axis=1))
print(np.hsplit(l2,2))
print(np.vsplit(l2,[3]))

m2=np.array([0.,1.,2.,3.,4.])
m2=np.tile(m2,5)
print(m2.reshape(5,5))
print(2. in m2)
print(10 in m2)

n2=np.random.random(10)
n2.flags.writeable=False
n2[1]=1

o2=np.arange(1,100)
final = o2[(o2 % 3 == 0) | (o2 % 5 == 0)]
print(np.sum(final))
#other method
divby3=o2[o2%3==0]
divby5=o2[o2%5==0]
final=np.unique(np.append(divby3,divby5))
print(np.sum(final))

p2=np.array([1,2,3,4])
print(p2.reshape(2,2,order='F'))
q2=np.array([[1,2],[3,4]])
print(q2.flatten(order='F'))
print(q2.ravel(order='F'))

r2=np.ones((5,5,5),dtype=int)
print(r2)

s2=np.arange(12).reshape(3,4)
print(s2*3)

t2=np.arange(4).reshape(1,4)
t22=np.arange(8).reshape(2,4)
for a,b in np.nditer([t2,t22]):
    print(a,b)

u2=np.array([1,2,3])
u22=np.array([1.,2.,3.])
u222=np.array(['a','b','c'])
#print(np.column_stack((u2,u22,u222)))
x = np.zeros((3), dtype=[('id', 'i4'),('score', 'f4'),('name', 'U40')])
new_data = [(1, 2., "Albert Einstein"), (2, 2., "Edmond Halley"), (3, 3., "Gertrude B. Elion")]
x[:] = new_data
print(x)
print(x['name'])

x2=np.array([1,2,3])
x22=np.array([1.,2.,3.])
x222=np.array(['a','b','c'])
result=np.core.records.fromarrays([x2,x22,x222],names='a,b,c')
print(result[0])
print(result[1])
print(result['b'])

y2=np.array([1.23232,4.23232323])
print(np.array2string(y2, formatter={'float_kind': lambda x: f"{x:.2f}"}))
print(y2.dtype)

z2=np.array([123456789.60000000e-10])
np.set_printoptions(precision=3)
print(z2)

a3=np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(np.delete(a3,0))
print(np.delete(a3,[8,9]))
b3=np.array([[1,2],[3,4]])
print(np.delete(b3,(0,0)))
print(np.delete(b3,[(0,0),(1,1)]))
print(np.delete(b3,0,axis=0)) #delete row 0
print(np.delete(b3,0,axis=1)) #delete column 1

print('removing row and column with nan')
c3=np.array([[1,3],[2,np.nan]])
print(~np.isnan(c3))
print(~np.isnan(c3).any(axis=1))
print(c3[~np.isnan(c3)])
print(c3[~np.isnan(c3).any(axis=1)]) #remove row
print(c3[:,~np.isnan(c3).any(axis=0)]) #remove col
print(c3)

d3 = np.array([97, 101, 105, 111, 117])
e3 = np.array(['a','e','i','o','u'])
print(e3[(d3>100)&(d3<110)])

f3=np.array([10,10,20,10,20,20,20,30,30,50,40,40])
print(np.unique(f3,return_counts=True)[1])

g3=np.array([[20,20,20],[30,30,30],[40,40,40]])
h3=np.array([20,30,40])
#i=0
#for row in g3:
#    print(row/h3[i])
#    i=i+1
print(g3/h3[:,None])

i3=np.arange(25000).reshape(500,50)
print(i3)
np.set_printoptions(threshold=sys.maxsize)
print(i3)

j3=np.array([10,20,30])
print(j3.sum())
print(j3.prod())

k3=np.array([10,20,20,20,20,0,20,30,30,30,0,0,20,20,0])
#for item in np.unique(k3,return_counts=True)[1]:
#    print(item)
print(np.count_nonzero(k3==10))

l3=np.array([200.,300.,np.nan,np.nan,np.nan,700.])
print(l3[~np.isnan(l3)])

x=np.array([1,2,3])
y=np.array([4,5])
z=np.array([9,8])
#print([np.tile(x, len(y)), np.repeat(y, len(x))])
print(np.array(np.meshgrid(x,y,z)).T.reshape(-1,3))

m3=np.array([1,0,2,0,3,0,4,5,6,7,8])
print(np.where(m3==0)[0])

n3=np.array([])
o3=np.array([10,20,30])
print(np.append(n3,o3))

p3=np.array([[1,2,3],[4,3,1]])
print(np.max(p3.flatten()))

q3=np.array([1,2,3])
r3=np.array([2,3,4])
print(np.vstack((q3,r3)))

s3=np.arange(16).reshape(4,4)
print(s3)
#[0,5,11]
print(np.array(np.where(s3==5)).T)
#with np.array made it 2,1 array then .T into 1,2
print(np.where(s3==11))

t3=np.arange(16).reshape(4,4)
print(np.resize(t3,(2,2)))
print(np.resize(t3,(5,5)))
print(np.resize(t3,5))

u3=np.arange(9).reshape(3,3)
v3=np.array([10,11,12]) #shape(1d)
print(u3+v3)
w3=np.array([[0],[10],[20]]) #shape(3,1)
print(v3+w3)

x3=np.arange(4).reshape(2,2)
y3=np.arange(4,8).reshape(2,2)
print(np.row_stack((x3,y3)))

z3=np.arange(16).reshape(4,4)
print(np.vsplit(z3,4))

a4 = np.arange(16).reshape(2, 2, 4)
print(a4)
print('at 1 and 3 position along 3rd axis')
print(np.dsplit(a4,[1,3]))
print('into two equal parts along 3rd axis')
print(np.dsplit(a4,2)

b4=np.array([24,27,30,29,18,14])
argsort=b4.argsort()
rank=np.empty_like(argsort)
rank[argsort]=np.arange(len(b4))
print(rank)

c4=np.array([1,3,7,9,10,13,14,17,29])
print(np.where(c4[(c4>5) & (c4<20)]))

d4=np.arange(12).reshape(3,4)
d4[:,[0,1]]=d4[:,[1,0]]
print(d4)

e4=np.arange(36).reshape(4,9)
print(np.where(np.any(e4>10,axis=1)))

f4=np.arange(36).reshape(4,9)
print(np.sum(f4,axis=0))

g4=np.arange(1,13).reshape(4,3)
print(np.triu(g4,0))

h4=np.arange(16).reshape(4,4)
for item in np.nditer(h4,flags=['external_loop'],order='F'):
    if np.array_equal(item,np.array([0,4,8,12])):
        print(True)
        break

for item in h4.T:
    if np.array_equal(item,np.array([0,4,8,12])):
        print(True)
        break

h4=np.array([[10.,20.,30.],
[40.,50.,np.nan],
[np.nan,6.,np.nan],
[np.nan,np.nan,np.nan]])
print(np.nanmean(h4,axis=1))
#masked array approach
temp=np.ma.masked_array(h4,np.isnan(h4))
result=np.mean(temp,axis=1)
print(result.filled(np.nan))

i4=np.array([1,2,3,2,4,6,1,2,12,0,-12,6]).reshape(-1,3)
print(np.average(i4,axis=1))

j4=np.array([[11,22,33,44,55],[66,77,88,99,100]])
j4[:,[0,1,2,3,4]]=j4[:,[1,3,0,4,2]]
print(j4)

k4=np.array([1.,7.,8.,2.,0.1,3.,15.,2.5])
for _ in range(4):
    temp=np.argmin(k4)
    print(np.min(k4))
    k4=np.delete(k4,temp)

k4=np.array([1.,7.,8.,2.,0.1,3.,15.,2.5])
n=4
result=np.argpartition(k4,n)#4 smallest elements
print(k4[result[:n]])
result2=np.argpartition(k4,-2)
print(k4[result2[-2:]])

l4=np.arange(96).reshape(3,4,8)
idx=np.array([0,2,2,2]) #make a 4 by 8 array
#means at index 0 is 0 so take 0th row from 0th group's 0row of l4
#means at index 1 is 2 so take 1st row from 2nd group's 1row of l4
#means at index 2 is 2 so take 2nd row from 2nd group's 2row of l4
#means at index 3 is 2 so take 3rd row from 2nd group's 3row of l4
final=np.empty_like(np.arange(32).reshape(4,8),dtype=int)
#i=0
#for item in np.nditer(idx):
#    final[i,:]=l4[item,i,:]
#    i=i+1
final=l4[idx,np.arange(4),:]
print(l4)
print(final)

m4=np.array([[1, 0, 'aaa'],[0, 1, 'bbb'],[0, 1, 'ccc']])
np.savetxt('matrix.txt',m4,delimiter='\t',fmt='%s')

x = np.array([10, -10, 10, -10, -10, 10])
y = np.array([.85, .45, .9, .8, .12, .6])
print(np.sum((x == 10) & (y > 0.5)))

d={'a':1,'b':2,'c':3}
n4=np.array([n for a,n in d.items()])
print(n4)

o4=np.arange(3 * 4 * 5).reshape(3, 4, 5)
print(np.array([np.diag(o4[i,:,:]) for i in range(3)]))
print("\n")
print(np.diagonal(o4,axis1=1,axis2=2))

p4=np.array([[1,2,3],[2,1,2]],np.int32)
print(repr(p4).count("1, 2"))

q4=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
seq=np.array([4,5,6])
print(np.where((q4==seq).all(axis=1)))

r4 = np.array([[1, 1, 0],
                 [0, 0, 0],
                 [0, 2, 3],
                 [0, 0, 0],
                 [0, -1, 1],
                 [0, 0, 0]])

print(r4[np.where((r4>0).any(axis=1))[0]])


s4=np.arange(12).reshape(3,4)
print(s4.size)
print(s4.shape)
print(s4.ndim)
print(s4.itemsize)

t4=np.arange(20)
m=np.mean(t4)
u4=np.array([[1,np.nan],[np.nan,5]])
u4[np.where(np.isnan(u4))]=m
print(u4)

v4=np.arange(20)
print(np.where((v4>6) & (v4%3==0))[0])

w4=np.arange(15).reshape(3,5)
x4=np.arange(15).reshape(3,5)
print(w4.shape==x4.shape)

y4=np.zeros((4,4),int)
y4[np.random.randint(0,4,7),np.random.randint(0,4,7)]=10
print(y4)

z4=np.arange(20).reshape(5,4)
print(z4-z4.mean(axis=1, keepdims=True))

a5=np.random.randint(0,3,(4, 10))
print((a5==0).all(axis=0).any())

iterator=(n for n in range(5))
b5=np.fromiter(iterator,int)
print(b5)

c5=np.arange(1,9)
d5=np.zeros(c5.size+((c5.size)-1)*2)
d5[::3]=c5
print(d5)

e5=np.arange(12).reshape(2,2,3)
f5=np.arange(4).reshape(2,2)
print(e5)
print(f5.reshape(2,2,1))
print(e5*f5.reshape(2,2,1))

g5=np.array([1,2,3,4,5,20],dtype=np.uint8)
print(np.unpackbits(g5[:,None],axis=1))

h5=np.random.randint(0,4,(6, 3))
comp=h5[:,0].reshape(-1,1)
print(h5)
print(h5[np.where((h5==comp).all(axis=1))])

i5=np.array([('Yasemin Rayner','88.5','90'),
             ('Ayaana Mcnamara','87','99'),
             ('Jody Preece','85.5','91')],dtype=[('name','U40'),('age','float64'),('marks','int32')])
print(i5)
print(i5['name'])
print(i5['age'])
print(i5['marks'])

j5=np.random.randint(0,5,(25,25))
#using list comprehension
blocksum=np.zeros((5,5),int)
index=[(0,5),(5,10),(10,15),(15,20),(20,25)]
blocksum=np.array([[np.sum(j5[i:j,a:b]) for i,j in index] for a,b in index])
print(blocksum)
#using reshape and sum using axis
print(j5.reshape(5,5,5,5).sum(axis=(1,3)))
#using reduceat
temp=np.add.reduceat(j5,[0,5,10,15,20],axis=1)
print(np.add.reduceat(temp,[0,5,10,15,20],axis=0))

k5=np.random.randint(0,5,(12,12))
print(k5)
print(np.array([[k5[i:i+4,j:j+4] for j in range(9)] for i in range(9)]))

l5=np.array(np.random.randint(0,4,(1,3,4)))
print(l5.shape)
print(np.squeeze(l5).shape)

m5=np.array(np.random.randint(0,4,(12,12,4)))
print(np.resize(m5,(6,6,3)))

n5=np.arange(4).reshape(2,2)
o5=np.arange(2).reshape(2,1)
print(np.concatenate([n5,o5],axis=1))

p5=np.array(np.random.random(12))
np.set_printoptions(precision=2)
print(p5)

q5=np.array([1.2e-07,1.5e-06,1.7e-05])
np.set_printoptions(suppress=True,precision=10)
print(q5)

r5=np.array([[1,2,3],[4,5,6]])
print(r5)
print(np.delete(r5,0,axis=1))

s5=np.array([[2, 5, 2],
             [1, 5, 5]])
t5=np.array([[5, 3, 4],
             [3, 2, 5]])
#print(np.array([[(s5[i,j]+t5[i,j])/2 for i in range(2)] for j in range(3)]))
print(np.divide((np.add(s5,t5)),2))

u5=np.array([1,2,3,4,5,5,5])
np.random.shuffle(u5[2:5])
print(u5)

v5=np.array([['Yasemin Rayner','88.5','90'],
             ['Ayana McNamara','87','79'],
             ['Jody Preece','85.5','91']])
print(v5[np.char.startswith(v5[:,0],'Y')])
print(v5[np.char.startswith(v5[:,2],'9')])

w5=np.array([
    ['01', 'V', 'Debby Pramod', 30.21],
    ['02', 'V', 'Artemiy Ellie', 29.32],
    ['03', 'V', 'Baptist Kamal', 31.00],
    ['04', 'V', 'Lavanya Davide', 30.22],
    ['05', 'V', 'Fulton Antwan', 30.21],
    ['06', 'V', 'Euanthe Sandeep', 31.00],
    ['07', 'V', 'Endzela Sanda', 32.00],
    ['08', 'V', 'Victoire Waman', 29.21],
    ['09', 'V', 'Briar Nur', 30.00],
    ['10', 'V', 'Rose Lykos', 32.00]
])
temp=w5[np.char.startswith(w5[:,2],'E')]
print(np.sum(np.float64(temp[:,3])))

x5=np.array([[10,40],[30,20]])
print(np.sort(x5,axis=0)) #column wise
print(np.sort(x5,axis=1)) #row wise
print(np.sort(x5.flatten()))

students=[('James',5,48.5),('Nail',6,52.5),('Paul',5,42.10),('Pit',5,40.11)]
datatype=[('name','U40'),('height','float64'),('class','float64')]
y5=np.array(students,datatype)
print(np.sort(y5,order=["height","name"]))

id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
height = np.array([40., 42., 45., 41., 38., 40., 42.0])
sortedorder=np.lexsort((id,height))
for n in sortedorder:
    print(id[n],height[n])

z5=np.array([1023,5202,6230,1671,1682,5241,4532])
print(np.argsort(z5))

a6=np.array([(1+2j),(3-1j),(3-2j),(4-3j),(3+5j)])
reala6=a6.real
imaga6=a6.imag
order=np.lexsort((imaga6,reala6))
for n in order:
    print(a6[n])

b6=np.array([70,50,20,30,-11,60,50,40])
print(np.partition(b6,4))
temp=np.argpartition(b6,4)
print(b6[temp[:4]])
print(b6[temp])

c6=[0.395,0.117,0.326,0.163,0.988,0.255,0.013,0.151,0.120,0.672]
temp=np.partition(c6,4)
print(np.concatenate((np.sort(temp[:4]),temp[4:])))

d6=np.array([[1,5,0],[3,2,5],[8,7,6]])
#sort by 2nd column
print(d6[d6[:,1].argsort()])

e6=np.array([[0,1],[2,3]])
print(np.max(e6,axis=1))
print(np.min(e6,axis=0))

f6=np.arange(12).reshape(2,6)
print(np.max(f6,axis=1)-np.min(f6,axis=1))

g6=np.arange(12).reshape(2,6)
print(np.percentile(g6,80,axis=1))

h6=np.arange(12).reshape(2,6)
print(np.median(h6))

i6=np.arange(5)
weightarr=np.array([1,2,3,4,5])
print(np.average(i6,weights=weightarr))

x=np.array([0,1,3])
y=np.array([2,4,5])
print(np.cov(x,y)) #co-variance
print(np.corrcoef(x,y))

j6=np.array([1,np.nan,np.inf,-np.inf,True])
print(np.isnan(j6))
print(np.isinf(j6))
print(np.isneginf(j6))
print(np.isfinite(j6))

k6=np.arange(9).reshape(3,3)
weightarr=np.arange(9,18).reshape(3,3)
print(np.average(k6,weights=weightarr,axis=0))

l6=[0,1,6,1,4,1,2,2,7]
print(np.bincount(l6))"""