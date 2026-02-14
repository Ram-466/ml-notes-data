import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4, 5], dtype=np.float32)

print("a:", a)
print("dtype a:", a.dtype)
print("shape a:", a.shape)

print("b:", b)
print("dtype b:", b.dtype)
print("shape b:", b.shape)

# 2D array
m = np.array([[1, 2, 3],
              [4, 5, 6]])

print("m:\n", m)
print("dtype m:", m.dtype)
print("shape m:", m.shape)
