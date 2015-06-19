#!/usr/bin/env python3

import sys

matrix = []
for line in sys.stdin:
	matrix.append(list(map(int,line.split(" "))))

score = matrix

print(matrix) 


for level in range(len(matrix)-2,-1,-1):
	#print(level)
	for i in range(0, len(score[level])):
		#print(level,i)
		score[level][i] = max(score[level+1][i], score[level+1][i+1]) + matrix[level][i]

print(score[0][0])