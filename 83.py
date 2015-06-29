#!/usr/bin/env python

import sys
import numpy as np

matrix = []

for line in sys.stdin:
	matrix.append(list(map(int,line.split(','))))

matrix = np.matrix(matrix)
min_sum = np.zeros(matrix.shape)


print matrix


min_sum[0,0] = matrix[0,0]

for j in range(1,matrix.shape[0]):
	min_sum[0,j] = matrix[0,j] + min_sum[0,j-1]

print min_sum
for i in range(matrix.shape[0]):
	for j in range(1,matrix.shape[1]):
		min_sum[j,i] = matrix[j,i] + min_sum[j-1,i]

print min_sum
changed = True

while changed:
	changed = False

	#moving right
	for j in range(1, matrix.shape[1]):
		for i in range(matrix.shape[0]):
			if min_sum[i,j] > matrix[i,j] + min_sum[i,j-1]:
				min_sum[i,j] = matrix[i,j] + min_sum[i,j-1]
				changed = True

	#moving left
	for j in range(matrix.shape[1] - 1):
		for i in range(matrix.shape[0]):
			if min_sum[i,j] > matrix[i,j] + min_sum[i,j+1]:
				min_sum[i,j] = matrix[i,j] + min_sum[i,j+1]
				changed = True

	#moving down
	for i in range(1, matrix.shape[0]):
		for j in range(matrix.shape[1]):
			if min_sum[i,j] > matrix[i,j] + min_sum[i-1,j]:
				min_sum[i,j] = matrix[i,j] + min_sum[i-1,j]
				changed = True

	for i in range(matrix.shape[0]-1):
		for j in range(matrix.shape[1]):
			if min_sum[i,j] > matrix[i,j] + min_sum[i+1,j]:
				min_sum[i,j] = matrix[i,j] + min_sum[i+1,j]
				changed = True



print min_sum