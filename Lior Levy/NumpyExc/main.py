#1
import numpy as np

#2
np.__version__
np.show_config()

#3
arr = np.zeros(10)

#4
arr.itemsize

#5
np.info(np.add)

#6
arr[4] = 1

#7
arr2 = np.arange(start=10, stop=49, step=1)

#8
arr2[::-1]

#9
np.matrix([[1, 2 , 3], [3, 4 , 5],[6 , 7, 8]])

#10
arr3 = np.array([1, 2, 0, 0, 4, 0])
np.where(arr3 != 0)

#11
np.identity(3, dtype = float)

#12
np.random.randint(100, size=(3, 3 ,3))

#13
arr4 = np.random.randint(100, size=(10, 10))
arr4.max()
arr4.min()

#14
arr5 = np.random.randint(100, size=(30))
np.mean(arr5)

#15
x = np.ones((5, 5))
x[1:-1, 1:-1] = 0

#16
full_array = np.full((5, 5), 0)
full_array =np.pad(full_array, pad_width=1, mode='constant',constant_values=1)

#17
print(0*np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)

#18
matrix = np.zeros((5, 5), float)
np.fill_diagonal(matrix[:-1, 1:], [1,2,3,4])
np.fill_diagonal(matrix[1:, :-1], [1,2,3,4])

#19
y = np.zeros((8, 8), dtype=int)
y[1::2, ::2] = 1
y[::2, 1::2] = 1

#20
np.unravel_index(100, (6 , 7 , 8))

#21
print(np.tile([[0,1] , [1,0]], (4, 8)))

#22
z = np.random.random((5, 5))
zmax = z.max()
zmin = z.min()
z = (z - zmin) / (zmax - zmin)

#23
dt = np.dtype([('r', np.ubyte ), ('g', np.ubyte ), ('b', np.ubyte )])

#24
np.matmul(a, b)

#25
a = np.random.random(size=10)
a[2:8] = np.negative(a[2:8])

#26
print(sum(range(5),-1))

#29
np.ceil(x)

#30
np.intersect1d([1, 3, 4, 3], [3, 1, 2, 1])

#31
#np.seterr(all='ignore')

#32
np.sqrt(-1) == np.emath.sqrt(-1)

#33
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')

#34
np.arange('2016-07', '2016-08', dtype='datetime64[D]')

#35
np.add(A,B)
np.divide(A,2)
np.negative(A)
np.multiply(A,B)

#36
Z - Z%1
Z // 1
np.floor(Z)
np.trunc(Z)

#37
np.arange(5).reshape(5,5)

#38
def generate():
    iterable = (x for x in range(10))
    print(np.fromiter(iterable, np.int))

#39
np.random.uniform(low=0.01, high=1, size=(10,))

#40
np.sort(x)

#41
np.add.reduce([2,3,5])

#42
np.array_equal(A,B)

#43
a.flags.writeable = False

#44
z = np.random.random((10, 2))
x, y = z[:, 0], z[:, 1]
r = np.sqrt(x**2 + y**2)
t = np.arctan2(y, x)

#45
nums = np.random.rand(5, 5)
max_value = np.max(nums)
nums[nums == max_value] = 0

#46
c= 1.0 / (x.reshape((-1,1)) - y)

#47
for dtype in [np.int8, np.int32, np.int64]:
   print(np.iinfo(dtype).min)
   print(np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
   print(np.finfo(dtype).min)
   print(np.finfo(dtype).max)
   print(np.finfo(dtype).eps)

#4
np.set_printoptions(threshold=float("inf"))
Z = np.zeros((40,40))

#49
Z = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(Z-v)).argmin()