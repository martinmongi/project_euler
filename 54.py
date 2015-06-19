#!/usr/bin/env python3

from enum import Enum

#class Number(Enum):


class Card:
	def __init__(self, number, suit):
		if number == 'T':
			self.number = 10
		elif number == 'J':
			self.number = 11
		elif number == 'Q':
			self.number = 12
		elif number == 'K':
			self.number = 13
		elif number == 'A':
			self.number = 14
		else:
			self.number = int(number)
		self.suit = suit

class Hand:
	def __init__(self, s):
		cards = s.split(' ')
		self.cards = []
		for c in cards:
			if c != "":
				self.cards.append(Card(c[0],c[1]))
		self.ap_n = {}
		for c in self.cards:
			if not c.number in self.ap_n:
				self.ap_n[c.number] = 0
			self.ap_n[c.number] += 1
		self.ap_s = {}
		for c in self.cards:
			if not c.suit in self.ap_s:
				self.ap_s[c.suit] = 0
			self.ap_s[c.suit] += 1
		print(s)
	
	def flush(self):
		if len(self.ap_s) == 1:
			return max(iter(self.ap_n))

	def straight(self):
		if len(self.ap_n) == 5 and sorted(list(self.ap_n))[0] == sorted(list(self.ap_n))[4] - 4:
			return max(iter(self.ap_n))

	def poker(self):
		for i in iter(self.ap_n):
			if self.ap_n[i] == 4:
				return i

	def full(self):
		for i in iter(self.ap_n):
			for j in iter(self.ap_n):
				if self.ap_n[i] == 3 and self.ap_n[j] == 2:
					return i

	def three(self):
		for i in iter(self.ap_n):
			if self.ap_n[i] == 3:
				return i

	def twopair(self):
		for i in iter(self.ap_n):
			for j in iter(self.ap_n):
				if i != j and self.ap_n[i] == 2 and self.ap_n[j] == 2:
					return str(max(i,j)) + " " + str(min(i,j))

	def pair(self):
		for i in iter(self.ap_n):
			if self.ap_n[i] == 2:
				return i

	def play(self):
		if self.flush() and self.straight():
			return "20 " + str(self.flush())
		if self.poker():
			return "19 " + str(self.poker())
		if self.full():
			return "18 " + str(self.full())
		if self.flush():
			return "17 " + str(self.flush())
		if self.straight():
			return "16 " + str(self.straight())
		if self.three():
			return "15 " + str(self.three())
		if self.twopair():
			return "14 " + str(self.twopair())
		if self.pair():
			return "13 " + str(self.pair())
		l = list(self.ap_n)
		return "12 " + " ".join(map(str, sorted(l, reverse=True)))

	def best(self,b):
		a_s = a.play().split(" ")
		b_s = b.play().split(" ")

		for i in range(min(len(a_s), len(b_s))):
			#print(i)
			if a_s[i] != b_s[i]:
				return a_s[i] > b_s[i]


import sys
count = 0
for line in sys.stdin:
	a = Hand(line[:14])
	b = Hand(line[15:])
	
	if a.best(b):
		print("Gana 1")
		count += 1
print(count)

# a = Hand("TC 3H 4S 7H QC")
# b = Hand("2H 3S 8C JS KH")
# print(a.play())
# print(b.play())
# print(a.best(b))