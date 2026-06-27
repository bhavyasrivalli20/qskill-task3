# Matrix Operations Tool
# Import NumPy library
import numpy as np

print("===== MATRIX OPERATIONS TOOL =====")

# Get matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Read first matrix
print("\nEnter values for Matrix 1")
matrix1 = []

for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix1.append(row)

# Read second matrix
print("\nEnter values for Matrix 2")
matrix2 = []

for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix2.append(row)

# Convert lists into NumPy arrays
matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

# Display matrices
print("\nMatrix 1")
print(matrix1)

print("\nMatrix 2")
print(matrix2)

# Addition
print("\nAddition")
print(matrix1 + matrix2)

# Subtraction
print("\nSubtraction")
print(matrix1 - matrix2)

# Multiplication
print("\nMultiplication")
print(np.dot(matrix1, matrix2))

# Transpose
print("\nTranspose of Matrix 1")
print(matrix1.T)

print("\nTranspose of Matrix 2")
print(matrix2.T)

# Determinant
if rows == cols:
    print("\nDeterminant of Matrix 1")
    print(np.linalg.det(matrix1))

    print("\nDeterminant of Matrix 2")
    print(np.linalg.det(matrix2))
else:
    print("\nDeterminant can be calculated only for square matrices.")