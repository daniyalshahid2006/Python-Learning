import numpy as np

# 1. Array creation
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((2, 3))
c = np.ones((3, 3))
d = np.arange(0, 10, 2)
e = np.linspace(0, 1, 5)
print("a:", a)
print("b:\n", b)
print("c:\n", c)
print("d:", d)
print("e:", e)

# 2. Array attributes
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("shape:", arr.shape)
print("ndim:", arr.ndim)
print("size:", arr.size)
print("dtype:", arr.dtype)

# 3. Indexing and slicing
arr2 = np.array([10, 20, 30, 40, 50])
print("arr2[1]:", arr2[1])
print("arr2[1:4]:", arr2[1:4])
print("arr2[::-1]:", arr2[::-1])

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("m[0, :]:", m[0, :])
print("m[:, 1]:", m[:, 1])
print("m[1:, 1:]:\n", m[1:, 1:])

# 4. Boolean masking / filtering
data = np.array([5, 12, 8, 20, 3, 17])
mask = data > 10
print("mask:", mask)
print("filtered:", data[mask])
data[data < 5] = 0
print("modified:", data)

# 5. Reshaping
r = np.arange(12)
r2 = r.reshape(3, 4)
r3 = r.reshape(2, 2, 3)
print("r2:\n", r2)
print("r3:\n", r3)
print("flatten:", r2.flatten())

# 6. Arithmetic operations (element-wise)
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("x+y:", x + y)
print("x*y:", x * y)
print("x/y:", x / y)
print("x**2:", x ** 2)

# 7. Broadcasting
p = np.array([[1, 2, 3], [4, 5, 6]])
q = np.array([10, 20, 30])
print("broadcast add:\n", p + q)

# 8. Aggregate functions
nums = np.array([[1, 2, 3], [4, 5, 6]])
print("sum:", nums.sum())
print("sum axis=0 (columns):", nums.sum(axis=0))
print("sum axis=1 (rows):", nums.sum(axis=1))
print("mean:", nums.mean())
print("max:", nums.max())
print("min:", nums.min())
print("std:", nums.std())

# 9. Sorting and searching
s = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("sorted:", np.sort(s))
print("argsort:", np.argsort(s))
print("where >4:", np.where(s > 4))
print("unique:", np.unique(s))

# 10. Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("dot product:\n", np.dot(A, B))
print("matmul (@):\n", A @ B)
print("transpose:\n", A.T)
print("inverse:\n", np.linalg.inv(A))
print("determinant:", np.linalg.det(A))

# 11. Random numbers
np.random.seed(42)
rand_arr = np.random.randint(1, 100, size=(3, 3))
print("random ints:\n", rand_arr)
rand_floats = np.random.rand(3)
print("random floats:", rand_floats)

# 12. Stacking and splitting
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print("vstack:\n", np.vstack((v1, v2)))
print("hstack:", np.hstack((v1, v2)))
split_arr = np.arange(9)
print("split into 3:", np.split(split_arr, 3))

# 13. Conditional logic with np.where
scores = np.array([45, 78, 92, 34, 60])
result = np.where(scores >= 50, "Pass", "Fail")
print("pass/fail:", result)

# 14. Copy vs view
orig = np.array([1, 2, 3])
view = orig.view()
copy = orig.copy()
orig[0] = 100
print("orig:", orig)
print("view (changed too):", view)
print("copy (unchanged):", copy)