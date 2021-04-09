import time
import math
import random


def dist(p0, p1):  # distance formula (takes two tuples)
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


def bruteForce(A):
    n = len(A)
    minDistance = dist(A[0], A[1])
    target = (A[0], A[1])
    if n == 2:
        return A[0], A[1]
    for i in range(0, n):
        for j in range(i + 1, n):
            distance = dist(A[i], A[j])
            if distance < minDistance:
                minDistance = distance
                target = (A[i], A[j])
    return target[0], target[1]


    # DRIVER CODE
random.seed(8000)
all_coordinates = []  # list that holds all the coordinates (tuples)
x_coordinates = []  # all x coordinates
y_coordinates = []  # all y coordinates

# Filling x and y coordinates list
for i in range(8000):

    # x coordinate
    x_val = round(20 * random.random() - 10, 2)
    x_coordinates.append(x_val)

    # y coordinate
    y_val = round(20 * random.random() - 10, 2)
    y_coordinates.append(y_val)

    # coordinate as a tuple
    all_coordinates.append((x_val, y_val))
# print(arr)

# run n # of times
n = 5
for i in range(n):
    st = time.time()
    bruteForce(all_coordinates)
    print(time.time()-st)
