#!/usr/bin/env python3
import time
import matplotlib.pyplot as plt
from collections import Counter
import random
import string
import re
import sys

# Control
ACCURACY = 10

file_reading = open(sys.argv[1], "r")
file_content = file_reading.readlines()
file_reading.close()

liens = []

for line in file_content:
	if(line[0:5] == "https"):
		next_stop = line.find('/', 9)
		liens.append(line[8:next_stop])
	elif(line[0:5] == "http:"):
		next_stop = line.find('/', 8)
		liens.append(line[7:next_stop])
	else:
		pass
	# print(line.strip())
	# time.sleep(0.2)

cnt = Counter()
for domaine in liens:
	cnt[domaine] += 1

# Récupération des éléments qui se répètent le plus
domain_name = []
domain_rep = []
for k, v in sorted(cnt.items(), key=lambda item: item[1]):
	if (v >= ACCURACY):
		domain_name.append(k)
		domain_rep.append(v)
	else:
		pass

plt.barh(domain_name, domain_rep)
plt.ylabel("Nombre d'occurences")
plt.show()
