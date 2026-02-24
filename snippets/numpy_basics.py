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

# First row
print("First row:", m[0])

# Second column
print("Second column:", m[:, 1])

# Element at row 1, column 2
print("Element (1,2):", m[1, 2])

v = np.array([10, 20, 30])

print("Matrix:\n", m)
print("Vector:", v)

print("m + v:\n", m + v)

a = np.array([1, 2, 3, 4, 5])

print("Original:" , a)

print("Add 10:", a + 10)
print("Multiply by 2:", a * 2)
print("squared:", a ** 2)

print("Mean:", np.mean(a))
print("Sum:", np.sum(a))
print("Standard Deviation:", np.std(a))


print("Original:", a)
print("Original shape:", a.shape)

reshaped = a.reshape(2, 3)

print("Reshaped:\n", reshaped)
print("Reshaped shape:", reshaped.shape)
