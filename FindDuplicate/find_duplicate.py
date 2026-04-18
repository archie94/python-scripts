# Find duplicate files in a directory
# Simple use of hash functions

import sys
import os
import hashlib
import json

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
	file_hash = {}

	if len(sys.argv) > 1:
		path = sys.argv[1]
		for root, dirs, files in os.walk(path):
			for file in files:
				file_path = os.path.join(root, file)
				hash_val = md5(file_path)
				
				if hash_val not in file_hash:
					file_hash[hash_val] = []
					file_hash[hash_val].append(file_path)
				else:
					file_hash[hash_val].append(file_path)
	else:
		print 'Please provide path to the target directory'

	#print json.dumps(file_hash, indent = 4, sort_keys = True)
	for key in file_hash:
		if len(file_hash[key]) > 1:
			print file_hash[key]

if __name__ == "__main__":
	main()
