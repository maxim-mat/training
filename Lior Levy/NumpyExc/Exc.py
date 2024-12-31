import random
import numpy as np

# 51
a = np.array([],
             dtype=[('color', [('r', np.int32), ('g', np.int32), ('b', np.int32)]),
                    ('position', [('x', np.int32), ('y', np.int32)])])

# 52
pos_arr = np.random.randint(0, 1000, (100, 2))
X = np.atleast_2d(pos_arr[:, 0])
Y = np.atleast_2d(pos_arr[:, 1])

dist = np.sqrt((X - X.T) ** 2 + (Y - Y.T) ** 2)

# 53
float_arr = np.array([1, 2, 3, 4], dtype=np.float64)
int_arr = float_arr.astype(np.int64)

# 54
file_data = np.genfromtxt("gfg.txt", dtype=str, encoding=None, delimiter=",")

# 55
# np.ndenumerate()

# 56
gauss_like_arr = np.random.normal(10, 5, size=[100, 2])

# 57
size = 4
amount_to_place = 3
num = 10

array_nums1 = np.zeros((size, size))
np.put(array_nums1, np.random.choice(range(size * size), amount_to_place, replace=False), num)

# 58
# done

# 59
nums = np.random.randint(0, 10, (3, 3))
nth_column = 1
sorted_arr = nums[nums[:, nth_column].argsort()]

# 60
arr = np.array([[1, 2, 2], [3, 0, np.nan], [0, 6, np.nan]])
has_null_columns = np.any(np.all(np.isnan(arr), axis=0))

# 61
arr = np.array([12, 40, 65, 78, 10, 99, 30])
some_number = 56
difference_array = np.absolute(arr - some_number)
nearest_value_index = difference_array.argmin()

# 62
a = np.arange(3)
b = a.reshape(3, 1)
c = a.reshape(1, 3)
z = 0

for x in np.nditer(b + c):
    z = z + x


# 63
class C(np.ndarray):
    def __new__(cls, name):
        return object.__new__(cls, name)

    def __init__(self, name):
        self.name = name


# 64
arr = np.array([12, 40, 65, 78, 10, 99, 30])
arr2 = np.array([0, 4, 2, 1, 1])
arr2 = np.unique(arr2)
np.add.at(arr, arr2, 1)

# 65
# F = np.bincount(arr , arr2)

# 66
w, h = 16, 16
I = np.random.randint(0, 2, (w, h, 3)).astype(np.ubyte)
I_flat = I.reshape(-1, 3)

n = len(np.unique(I_flat, axis=0))

# 67
a = "some 4d array i considered"
# np.sum(arr , axis=(-1,-2))

# 68
D = np.random.uniform(0,1,100)
S = np.random.randint(0,10,100)
sum = (np.bincount(S, weights=D))
count = np.bincount(S)
D_means = sum/ count

# 69
a = np.random.uniform(0, 1, (5, 5))
b = np.random.uniform(0, 1, (5, 5))
Z = np.diag(a.dot(b))

# 70
inputArray = [1, 2, 3, 4, 5]
newArray = np.zeros(4 * len(inputArray), dtype=int)
newArray[::4] = inputArray

# 71
y = np.random.rand(5, 5)
x = np.random.rand(5, 5, 3)
result = x * y[:, :, np.newaxis]

# 72
num_arr = np.array([[1, 3, 1], [3, 1, 3], [2, 9, 2], [9, 2, 9]])
num_arr = np.roll(num_arr, 2, axis=0)

# 73--?
triangles = np.random.randint(0,100,(10,3))
F = np.roll(triangles.repeat(2,axis=1),-1,axis=1)
F = F.reshape(len(F)*3,2)
F = np.sort(F,axis=1)
G = np.unique(F)

# 74
C = np.bincount([2, 2, 2, 4, 4, 6, 8, 8, 8, 8, 8])
A = np.repeat(np.arange(len(C)), C)

# 75
from numpy.lib.stride_tricks import sliding_window_view

arr = np.array([12, 40, 65, 78, 10, 99, 30])
i = sliding_window_view(arr, window_shape=3).mean(axis=1)

# 76
Z = arr
Z = sliding_window_view(Z, window_shape=3)

# 77
np.logical_not(True)

# 78
p0 = np.random.randint(0, 1000, (10, 2))
p1 = np.random.randint(0, 1000, (10, 2))
p = np.random.randint(0, 1000, (1, 2))
i = 3
d = (np.cross(p1 - p0, p - p0) / np.linalg.norm(p1 - p0))[i]

# 79
j = 4
p3 = np.random.randint(0, 1000, (10, 2))
d = (np.cross(p1 - p0, p3[j] - p0) / np.linalg.norm(p1 - p0))[i]

# 80--!
arb_arr = np.random.randint(0, 1000, (10, 10))
center = arb_arr[3][4]
condition = np.mod(arr, 3) == center

# 81
Z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
i = sliding_window_view(Z, window_shape=4)

# 82
arr = np.array([[1, 2, 3], [5, 6, 4], [9, 8, 7]])
rank = np.array(arr).argsort().argsort()

# 83
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
x = np.bincount(x).argmax()

# 84
arr = np.random.randint(0, 1000, (10, 10))
i = sliding_window_view(arr, window_shape=(3, 3))

# 85
class C(np.ndarray):
    def __setitem__(self, index, value):
        i, j = index
        super(C, self).__setitem__((i, j), value)
        super(C, self).__setitem__((j, i), value)


# 86
n = 5
p = 3
p_mat = np.random.randint(0, 1000, (p , n , n))
p_vec = np.random.randint(0, 1000, (p , n ,1))
p_products_sum = np.tensordot(p_mat , p_vec , axes=[[0, 2], [0, 1]])

# 87
arra1 = np.ones((16, 16))
k = 4
result = np.add.reduceat(
         np.add.reduceat(arra1, np.arange(0, arra1.shape[0], k), axis=0),
         np.arange(0, arra1.shape[1], k), axis=1)

# 88
def play_life(a):
    xmax, ymax = a.shape
    b = a.copy()
    for x in range(xmax):
        for y in range(ymax):
            n = np.sum(a[max(x - 1, 0):min(x + 2, xmax), max(y - 1, 0):min(y + 2, ymax)]) - a[x, y]
            if a[x, y]:
                if n < 2 or n > 3:
                    b[x, y] = 0
            elif n == 3:
                b[x, y] = 1
    return(b)
life = np.zeros((5, 5))
life[2, 1:4] = 1

print(life)
for i in range(3):
    life = play_life(life)
    print(life)

# 89
arr = np.array([12, 40, 65, 78, 10, 99, 30])
n = 4
largest_n_values = arr[np.argsort(arr)[-n:]]

# 90
def cartesian_product(*arrays):
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)

# 91
x = np.array([(1.0, 2), (3.0, 4)], dtype=[('x', '<f8'), ('y', '<i8')])
x = np.rec.array(x)

# 92
Z = arr
solution1 = np.power(Z, 3)
solution2 = Z ** 3
solution3 = Z * Z * Z

# 93
nums1 = np.random.randint(0,5,(8,3))
nums2 = np.random.randint(0,5,(2,2))

temp = (nums1[..., np.newaxis, np.newaxis] == nums2)
rows = (temp.sum(axis=(1, 2, 3)) >= nums2.shape[1]).nonzero()[0]

# 94
nums = np.random.randint(0, 4, (6, 3))
new_nums = np.logical_and.reduce(nums[:, 1:] == nums[:, :-1], axis=1)
result = nums[~new_nums]

# 95
I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128], dtype=np.uint8)
bin_rep = np.unpackbits(I[:, np.newaxis], axis=1)

# 96
original_array = np.random.randint(0, 3, (5, 3))
unique_rows = np.unique(original_array, axis=0)

# 97
a = np.arange(10)
b = np.arange(5, 15)

#inner
np.einsum('i,i', a, b)
#outer
np.einsum('i,j->ij', a, b)
#mult
np.einsum('i,i->i', a, b)
#sum
np.einsum('i->', a)

# 98--?
phi = np.arange(0, 1*np.pi, 0.1)
a = 1
v1 = a*phi*np.cos(phi)
v2 = a*phi*np.sin(phi)
dr = (np.diff(v1)**2 + np.diff(v2)**2)**.5
r = np.zeros_like(v1)
r[1:] = np.cumsum(dr)
r_int = np.linspace(0, r.max(), 200)
v1_int = np.interp(r_int, r, v1)
v2_int = np.interp(r_int, r, v2)

# 99
n= 6
x = np.array([[1,2,9], [5,2,4], [1,2,3]])
mult_dist = np.argwhere((np.sum(x , axis=1) == n) & (np.all(np.mod(x, 1) == 0)))

# 100
X = np.random.normal(loc= 300.0, size=1000)
N = 20
sample_mean = []
for i in range(N):
  y = random.sample(X.tolist(), 4)
  avg = np.mean(y)
  sample_mean.append(avg)

bootstrapped_result = np.mean(sample_mean)
