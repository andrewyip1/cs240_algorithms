import decimal
import operator
import matplotlib.pyplot as plt
import random
import math


x = [round(random.uniform(-1, 1), 2) for x in range(1000)]
y = [round(random.uniform(-1, 1), 2) for x in range(1000)]

# filtered values with distance < 1
filtered_x = []
filtered_y = []

# loop to filter values
for i in range(1000):
    distance = math.sqrt((x[i]-0)**2 + (y[i]-0)**2)
    if distance < 1:
        filtered_x.append(x[i])
        filtered_y.append(y[i])


plt.scatter(filtered_x, filtered_y)
plt.show()
