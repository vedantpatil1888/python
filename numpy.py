# import numpy as np
# # 1. 1D Array info
# arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(arr1, arr1.size, arr1.dtype, arr1.ndim)


# 2. Arithmetic on two arrays of 5 integers
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])
print("Add:", a + b, "Sub:", a - b, "Mul:", a * b, "Div:", a / b, "Mod:", a % b)

# # 3. Max, min, sum, average
# arr2 = np.array([5, 12, 45, 8, 2, 90, 34, 21, 6, 77])
# print("Max:", arr2.max(), "Min:", arr2.min(), "Sum:", arr2.sum(), "Avg:", arr2.mean())

# [9:38 am, 01/10/2026] Pranav biranje: 
# # 4. Boolean indexing for even/odd (1 to 20)
# arr_1_20 = np.arange(1, 21)
# print("Even:", arr_1_20[arr_1_20 % 2 == 0])
# print("Odd:", arr_1_20[arr_1_20 % 2 != 0])

# # 5. Reshape 1 to 12
# arr_12 = np.arange(1, 13)
# print("2x6:\n", arr_12.reshape(2, 6))
# print("3x4:\n", arr_12.reshape(3, 4))
# print("4x3:\n", arr_12.reshape(4, 3))
# [9:55 am, 01/10/2026] Pranav biranje: # 6. Matrix addition (3x3)
# mat1 = np.ones((3, 3))
# mat2 = np.full((3, 3), 5)
# print("Matrix Add:\n", mat1 + mat2)

# # 7. Matrix multiplication
# mat_a = np.ones((2, 3))
# mat_b = np.ones((3, 2))
# print("Matrix Mul:\n", np.dot(mat_a, mat_b))

# # 8. Transpose 3x4
# mat3x4 = np.arange(12).reshape(3, 4)
# print("Transpose:\n", mat3x4.T)

# # 9. Slicing a 4x4 array
# mat4x4 = np.arange(16).reshape(4, 4)
# print("First row:", mat4x4[0, :])
# print("Last column:", mat4x4[:, -1])
# print("Diagonal:", np.diag(mat4x4))
# print("2nd & 3rd rows:\n", mat4x4[1:3, :])

# # 10. Row and Column sums for 4x4
# print("Sum of each column (axis 0):", mat4x4.sum(axis=0))
# print("Sum of each row (axis 1):", mat4x4.sum(axis=1))

