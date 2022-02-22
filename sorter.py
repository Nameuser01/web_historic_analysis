#!/usr/bin/env python3
import matplotlib.pyplot as plt
from collections import Counter
import stats_random as func
# import file_values

#	Way to use the generate function #
# generate(<start teminal>, <stop terminal>, <number of entities to generate>)

data = []
data = func.generate(1, 150, 10000000)
stats = Counter(data).most_common()

number_id = []
number_rep = []
i = 0
for i in range (len(stats)):
	number_id.append(stats[i][0])
	number_rep.append(stats[i][1])
print(number_id)
print(number_rep)
plt.bar(number_id, number_rep, color="blue")
plt.grid(True)
plt.show()

print(stats)