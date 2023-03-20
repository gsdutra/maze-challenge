import numpy as np
from matrixTransf import matrix_transfrom

# matrix = np.loadtxt('simple_input.txt', usecols=range(6))
matrix = np.loadtxt('input.txt', usecols=range(85))
print (matrix)
#matrix[y, x]
matrix_len_x = matrix.shape[1]
matrix_len_y = matrix.shape[0]

brk = [0]

def choose_way(pos, history, matrix, depth):

	if depth > 990: brk [2]

	print (pos, matrix[pos[0], pos[1]], depth, *history)
	print (matrix)

	if (matrix[pos[0], pos[1]] == 4):
		return history
	
	if (pos[0] + 1 != matrix_len_y):
		if (matrix_transfrom(matrix)[pos[0] + 1, pos[1]] != 1):
			history.append('D')
			ans = choose_way([pos[0] + 1, pos[1]], history, matrix_transfrom(matrix), depth + 1)
			if ans != 0:
				return ans

	if (pos[1] + 1 != matrix_len_x):
		if (matrix_transfrom(matrix)[pos[0], pos[1] + 1] != 1):

			history.append('L')
			ans = choose_way([pos[0], pos[1] + 1], history, matrix_transfrom(matrix), depth + 1)
			if ans != 0:
				return ans

	if (pos[0] - 1 != -1):
		if (matrix_transfrom(matrix)[pos[0] - 1, pos[1]] != 1):
			history.append('U')
			ans = choose_way([pos[0] - 1, pos[1]], history, matrix_transfrom(matrix), depth + 1)
			if ans != 0:
				return ans

	if (pos[1] - 1 != -1):
		if (matrix_transfrom(matrix)[pos[0], pos[1] - 1] != 1):
			history.append('R')
			ans = choose_way([pos[0], pos[1] - 1], history, matrix_transfrom(matrix), depth + 1)
			if ans != 0:
				return ans

	return 0

print(*choose_way([0,0], [], matrix, 0))