# We need install numpy in order to import it
import numpy as np

# input two matrices
mat1 = ([1, 2, 3],[4, 5, 6])
mat2 = ([7, 8],[9, 10],[11, 12])

# This will return dot product
res = np.dot(mat1,mat2)

# print resulted matrix
print(res)
