#!/usr/bin/env python3

def sieve(n):

	c = []
	for i in range(n+1):
		c.append(set([]))

	for i in range(1,n+1):

		for j in range(2*i, n+1, i):
			c[j].add(i)

	return c


limit = 10**6

s = sieve(limit)

tree = []
for i in range(len(s)):
	tree.append(sum(list(s[i])))

cnt = []
for i in range(len(tree)):
	#	print(i)
	auxi = set([i])
	count = 1
	while i <= limit and i > 1 and tree[i] not in auxi:
		auxi.add(tree[i])
		count += 1
		i = tree[i]
		

	if i > limit or i <= 1:
		cnt.append(0)
	else:
		cnt.append(count)

m = max(cnt) 

for i in range(limit):
	if cnt[i] == m:
		print(i)