import random
import math
import matplotlib.pyplot as plt
import time


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


def dist(p0, p1):  # distance formula (takes two tuples)
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


def closest_split_pair(Px, Py, g):
    median = Px[len(Px)//2][0]  # median for x

    # strip
    strip = []
    for point in Py:
        # a pair of points is a split pair if and only if one point x coordinate is in between (median - g) and (median + g)
        if median - g <= point[0] <= median + g:
            strip.append(point)

    best = g
    best_pair = Px[0], Px[1]  # (x,y), (x,y)

    for i in range(len(strip)):
        for j in range(1, min(7, len(strip)-i)):
            if dist(strip[i], strip[i+j]) < best:
                best = dist(strip[i], strip[i+j])
                best_pair = strip[i], strip[i+j]

    return best_pair[0], best_pair[1]  # returns (x,y), (x,y)


def closest_pair(Px, Py):

    # Base Case
    if len(Px) <= 3:
        return bruteForce(Px)

    Lx = Px[:len(Px)//2]  # first half of x sorted by x coordinate
    Ly = Py[:len(Py)//2]  # first half of y sorted by y coordinate
    Rx = Px[len(Px)//2:]  # second half of x sorted by x coordinate
    Ry = Py[len(Py)//2:]  # second half of y sorted by y coordinate

    l1, l2 = closest_pair(Lx, Ly)  # best left pair - returns (x,y), (x,y)
    r1, r2 = closest_pair(Rx, Ry)  # best right pair - returns (x,y), (x,y)

    # parameters
    g = min(dist(l1, l2), dist(r1, r2))

    # best split pair - returns (x,y), (x,y)
    s1, s2 = closest_split_pair(Px, Py, g)

    # CALCULATING WHICH IS THE SHORTEST DISTANCE
    bestDistance = min(dist(l1, l2), dist(r1, r2), dist(s1, s2))
    if bestDistance == dist(l1, l2):
        return l1, l2
    elif bestDistance == dist(r1, r2):
        return r1, r2
    else:
        return s1, s2


    # DRIVER CODE
random.seed(10**6)
all_coordinates = []  # list that holds all the coordinates (tuples)
x_coordinates = []  # all x coordinates
y_coordinates = []  # all y coordinates

# Filling x and y coordinates list
for i in range(10**6):

    # x coordinates
    x_val = round(20 * random.random() - 10, 2)
    x_coordinates.append(x_val)

    # y coordinates
    y_val = round(20 * random.random() - 10, 2)
    y_coordinates.append(y_val)

    # coordinates as a tuple
    all_coordinates.append((x_val, y_val))
# print(arr)


# Scatters all the points
plt.scatter(x_coordinates, y_coordinates)

# sorted list of x coordinates in increasing order
Px = sorted(all_coordinates, key=lambda x_val: x_val[0])

# sorted list of y coordinates in increasing order
Py = sorted(all_coordinates, key=lambda y_val: y_val[0])

# Run program n times
n = 5
for i in range(n):
    st = time.time()
    smallest_distance_points = closest_pair(Px, Py)
    print(time.time()-st)
    print("closest pair", smallest_distance_points)

plt.scatter(x_coordinates, y_coordinates)
# first coordinate
plt.plot(smallest_distance_points[0][0],
         smallest_distance_points[0][1], 'or', color="cyan")
# second coordinate
plt.plot(smallest_distance_points[1][0],
         smallest_distance_points[1][1], 'or', color="cyan")
plt.show()
