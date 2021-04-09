import random
import math
import matplotlib.pyplot as plt


def dist(p0, p1):  # distance formula (takes two points)
    print("p0", p0)
    print("p1", p1)
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


def closestPair(A):  # passing in a list of coordinates
    n = len(A)
    minDistance = dist(A[0], A[1])  # A[0] = (x0,y0), #A[1] = (x1,y1)
    target = (A[0], A[1])  # tuple consisting of 2 points

    # Base Case
    if n == 2:
        return dist(A[0], A[1]), A[0], A[1]

    # Iterative calls (brute force)
    for i in range(0, n):
        for j in range(i + 1, n):
            distance = dist(A[i], A[j])
            if distance < minDistance:
                minDistance = distance
                target = (A[i], A[j])
    return target  # target = tuple of two tuples ((x0,y0) , (x1, y1))


def deltaPoints(sorted_x_coordinates):
    # left side of sorted x coordinates (list) of left side
    L = sorted_x_coordinates[:len(sorted_x_coordinates)//2]

    # right side of sorted x coordinates (list) of right side
    R = sorted_x_coordinates[len(sorted_x_coordinates)//2:]

    # passing in first and second coordinate of the sorted left and right x
    deltaL = dist(closestPair(L)[0], closestPair(L)[
                  1])  # returns an x y coordinate
    deltaR = dist(closestPair(R)[0], closestPair(R)[1])

    if deltaL < deltaR:
        return closestPair(L)
    else:
        return closestPair(R)


# MAIN CODE

random.seed(10)
all_coordinates = []  # list that holds all the coordinates (tuples)
x_coordinates = []  # all x coordinates
y_coordinates = []  # all y coordinates

# Filling x and y coordinates list
for i in range(10):

    # x coordinate
    x_val = round(20 * random.random() - 10, 2)
    x_coordinates.append(x_val)

    # y coordinate
    y_val = round(20 * random.random() - 10, 2)
    y_coordinates.append(y_val)

    # coordinate as a tuple
    all_coordinates.append((x_val, y_val))
# print(arr)

# Scatters all the points
plt.scatter(x_coordinates, y_coordinates)

# sorted list of x coordinates in increasing order
sorted_x_coordinates = sorted(all_coordinates, key=lambda x_val: x_val[0])

# sorted list of y coordinates in increasing order
sorted_y_coordinates = sorted(all_coordinates, key=lambda y_val: y_val[0])

# left side of x coordinates
L = sorted_x_coordinates[:len(sorted_x_coordinates)//2]

# right side of x coordinates
R = sorted_x_coordinates[len(sorted_x_coordinates)//2:]

#print("Closet Left: ", closestPair(L))
#print("Closet Right: ", closestPair(R))
#print(closestPair(L)[0], closestPair(L)[1])

# delta is the distance between the two smallest length points
delta = dist(deltaPoints(sorted_x_coordinates)[
             0], deltaPoints(sorted_x_coordinates)[1])

#print("sorted_x_coordinates: ", sorted_x_coordinates)


# calculating the median (middle value of sorted x coordinates + )
median = (sorted_x_coordinates[len(sorted_x_coordinates)//2-1]
          [0] + sorted_x_coordinates[len(sorted_x_coordinates)//2][0])/2

#print("Median: ", median)

# determining the strip (Sy in the book)

strip = []
for pair in sorted_y_coordinates:
    if pair[0] < median+delta and pair[0] > median-delta:
        strip.append(pair)

#print("strip: ", strip)

best = delta
bestPair = deltaPoints(sorted_x_coordinates)
l = len(strip)
for i in range(l):
    for j in range(1, min(7, l-i)):
        if dist(strip[i], strip[i+j]) < best:
            best = dist(strip[i], strip[i+j])
            bestPair = (strip[i], strip[i+j])

# Plotting points
print("Best Pair: ", bestPair)
plt.axvline(x=median)
plt.axvline(x=median+delta, color="red")
plt.axvline(x=median-delta, color="red")
plt.plot(bestPair[0][0], bestPair[0][1], 'or', color="red")
plt.plot(bestPair[1][0], bestPair[1][1], 'or', color="red")
plt.plot(closestPair(L)[0][0], closestPair(L)[0][1], 'or', color="black")
plt.plot(closestPair(L)[1][0], closestPair(L)[1][1], 'or', color="black")
plt.plot(closestPair(R)[0][0], closestPair(R)[0][1], 'or', color="cyan")
plt.plot(closestPair(R)[1][0], closestPair(R)[1][1], 'or', color="cyan")
plt.show()
