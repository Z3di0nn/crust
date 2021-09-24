import crypter
import sys
import os


with open(sys.argv[1], 'r') as f:
	for line in f:

		enc = crypter.encode(line)
		if 'str' in line:
			break

