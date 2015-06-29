#!/usr/bin/env python

import sys
import numpy as np

matrix = []

for line in sys.stdin:
	matrix.append(list(map(int,line.split(','))))

matrix = np.matrix(matrix)
min_sum = np.zeros(matrix.shape)

for i in range(matrix.shape[0]):
	min_sum[i,0] = matrix[i,0]


for j in range(1,matrix.shape[1]):
	#print(min_sum)
	min_sum[0,j] = matrix[0,j] + min_sum[0,j-1]
	
	for i in range(1,matrix.shape[0]):
	 	min_sum[i,j] = matrix[i,j] + min(min_sum[i-1,j], min_sum[i,j-1])

	for i in range(matrix.shape[0]-2, -1, -1):
		min_sum[i,j] = min(min_sum[i,j], matrix[i,j] + min_sum[i+1,j])

#print(matrix)
print(min(min_sum[:,matrix.shape[1]-1]))