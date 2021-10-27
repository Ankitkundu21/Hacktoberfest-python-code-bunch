#!/bin/bash/env python3
#Taking File name as input
file = input('Enter the file name: ')
try:
    file = open(file)
except:
    print('File cannot be opened:', file)
    exit()

counts = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print("Here is complete list of words with counts :")
print(counts)
