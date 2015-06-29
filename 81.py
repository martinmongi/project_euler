#!/usr/bin/env python

import sys
import numpy as np

matrix = []

for line in sys.stdin:
	matrix.append(list(map(int,line.split(','))))

matrix = np.matrix(matrix)
min_sum = np.zeros(matrix.shape)

print(matrix)
print(min_sum)

min_sum[0,0] = matrix[0,0]

for i in range(1,matrix.shape[0]):
	min_sum[0,i] = matrix[0,i] + min_sum[0,i-1]
	min_sum[i,0] = matrix[i,0] + min_sum[i-1,0]

#print(matrix)
print(min_sum)

for j in range(1,matrix.shape[1]):
	for i in range(1,matrix.shape[0]):
		min_sum[i,j] = matrix[i,j] + min(min_sum[i-1,j], min_sum[i,j-1])

#print(matrix)
print(min_sum)