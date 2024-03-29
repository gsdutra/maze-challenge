import numpy as np

def matrix_transfrom(matrix):
	matrix_len_x = matrix.shape[1]
	matrix_len_y = matrix.shape[0]
	newMatrix = matrix.copy()
	for i in range(matrix_len_y):
		for j in range(matrix_len_x):

			count = 0
			if (i-1 != -1):
				if matrix[i-1, j] == 1: count += 1
			if (i+1 != matrix_len_y):
				if matrix[i+1, j] == 1: count += 1
			if (j-1 != -1):
				if matrix[i, j-1] == 1: count += 1
			if (j+1 != matrix_len_x):
				if matrix[i, j+1] == 1: count += 1
			if (i-1 != -1 and j-1 != -1):
				if matrix[i-1, j-1] == 1: count += 1
			if (i+1 != matrix_len_y and j+1 != matrix_len_x):
				if matrix[i+1, j+1] == 1: count += 1
			if (i+1 != matrix_len_y and j-1 != -1):
				if matrix[i+1, j-1] == 1: count += 1
			if (i-1 != -1 and j+1 != matrix_len_x):
				if matrix[i-1, j+1] == 1: count += 1

			if (matrix[i, j] == 0 and count > 1 and count < 5):
				newMatrix[i, j] = 1
			if (matrix[i, j] == 1 and count != 4 and count != 5):
				newMatrix[i, j] = 0
	return newMatrix