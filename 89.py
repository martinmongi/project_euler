#!/usr/bin/env python3


def roman_to_int(s):
	n = 0
	i = 0
	while i < len(s) and s[i] == 'M':
		n += 1000
		i+= 1


	if i < len(s) - 1 and s[i] == 'C' and s[i+1] == 'M':
		n += 900
		i += 2
	elif i < len(s) - 1 and s[i] == 'C' and s[i+1] == 'D':
		n += 400
		i += 2

	while i < len(s) and s[i] == 'D':
		n+= 500
		i +=1

	while i < len(s) and s[i] == 'C':
		n += 100
		i+= 1


	if i < len(s) - 1 and s[i] == 'X' and s[i+1] == 'C':
		n += 90
		i += 2
	elif i < len(s) - 1 and s[i] == 'X' and s[i+1] == 'L':
		n += 40
		i += 2

	while i < len(s) and s[i] == 'L':
		n+= 50
		i +=1

	while i < len(s) and s[i] == 'X':
		n += 10
		i+= 1

	if i < len(s) - 1 and s[i] == 'I' and s[i+1] == 'X':
		n += 9
		i += 2
	elif i < len(s) - 1 and s[i] == 'I' and s[i+1] == 'V':
		n += 4
		i += 2

	while i < len(s) and s[i] == 'V':
		n+= 5
		i +=1

	while i < len(s) and s[i] == 'I':
		n += 1
		i += 1



	return n

def int_to_roman(n):
	s = []
	while n >= 1000:
		s.append('M')
		n -= 1000

	if n >= 900:
		s.append('CM')
		n -= 900

	if n >= 500:
		s.append('D')
		n -=500

	if n >= 400:
		s.append('CD')
		n -= 400

	while n >= 100:
		s.append('C')
		n -= 100

	if n >= 90:
		s.append('XC')
		n -= 90

	if n >= 50:
		s.append('L')
		n -=50

	if n >= 40:
		s.append('XL')
		n -= 40

	while n >= 10:
		s.append('X')
		n -= 10

	if n >= 9:
		s.append('IX')
		n -= 9

	if n >= 5:
		s.append('V')
		n -=5

	if n >= 4:
		s.append('IV')
		n -= 4 

	while n >= 1:
		s.append('I')
		n -= 1

	return "".join(s)



import sys

c = 0
for line in sys.stdin:
	if line[-1] == '\n':
		line = line[:-1]
	c += len(line) - len(int_to_roman(roman_to_int(line)))
	print(line, roman_to_int(line), int_to_roman(roman_to_int(line)), len(line) - len(int_to_roman(roman_to_int(line)))-1)

print(roman_to_int("XXXXVIII\n"))
print(c)