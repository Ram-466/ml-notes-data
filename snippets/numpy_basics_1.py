import numpy as np

m = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Matrix:\n", m)

# First row
print("First row:", m[0])

# Second column
print("Second column:", m[:, 1])

# Element at row 1, column 2
print("Element (1,2):", m[1, 2])
