#!/usr/bin/env python3

import sys

def decrypt(key, message):
	ki = 0
	decrypted = []
	for c in message:
		decrypted.append(ord(key[ki]) ^ int(c))
		ki = (ki + 1) % len(key)
	return decrypted


for line in sys.stdin:
	message = line.split(",")

#for c in range(ord('a'), ord('z') + 1):
key = "".join(["g"] + ["o"] + ["d"])
dec = decrypt(key, message)

print(sum(dec))

