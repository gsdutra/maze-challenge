import numpy as np
from matrixTransf import matrix_transfrom

matrix = np.loadtxt('simple_input.txt', usecols=range(6))
print (matrix)
#matrix[y, x]
matrix_len_x = matrix.shape[1]
matrix_len_y = matrix.shape[0]

def choose_way():
	return 0


def run():
	return 0

print(matrix_transfrom(matrix))