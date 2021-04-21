import random
import matplotlib.pyplot as plt
import math
import statistics

# this function creates a tuple of coordinates


def create_coordinates():
    x = []
    y = []

    for i in range(64):

        # x and y coordinate
        x_cord = round(random.uniform(-1, 1), 2)
        y_cord = round(random.uniform(-1, 1), 2)

        # appending it to list of coordinates
        x.append(x_cord)
        y.append(y_cord)

    return x, y


def zip_coordinates(x, y):
    coordinates = zip(x, y)
    return coordinates

# sorts tuple by x values


def sort_by_x(x_cord):
    #x_cord.sort(key=lambda x: x[0])
    x_cord.sort()
    return x_cord


def sort_by_y(y_cord):
    #y_cord.sort(key=lambda x: x[0])
    y_cord.sort()
    return y_cord


def closest_pair(x, y):

    # Base Case
    if len(x) < 3:  # if you have two x and y points
        return (abs(x[0]-x[1]), abs(y[0]-y[1]))

    # Individual Coordinates
    Lx = sort_by_x(x[:len(x)//2])  # first half of x sorted by x coordinate
    Ly = sort_by_y(y[:len(y)//2])  # first half of y sorted by y coordinate
    Rx = sort_by_x(x[len(x)//2:])  # second half of x sorted by x coordinate
    Ry = sort_by_y(y[len(y)//2:])  # second half of y sorted by y coordinate

    print("left half of x", Lx)
    print("\n")
    print("left half of y", Ly)
    print("\n")
    print("right half of x", Rx)
    print("\n")
    print("right half of y", Ry)
    print("\n")
    print("\n")
    print("\n")
    print("\n")

    # tuple of an x and y value that is the best
    L1, L2 = closest_pair(Lx, Ly)  # best left pair (from x and y)
    R1, R2 = closest_pair(Rx, Ry)  # best right pair (from x and y)

    print("hey there!")

    # Parameter
    g = min(math.sqrt((L1 - L2) ** 2 + (L1 - L2)**2),
            math.sqrt((R1 - R2) ** 2 + (R1 - R2)**2))

    S1, S2 = closest_split_pair(x, y, g)  # best split pair

    all_cord = [(L1, L2), (R1, R2), (S1, S2)]
    print("all coordinates")
    print("lol", all_cord[0][0])
    min_distance = float("inf")
    min_cord = ()
    for i in range(3):
        current_distance = math.sqrt(all_cord[i][0] - 0)  # need to fix here
        print("current didstance", current_distance)
        if current_distance < min_distance:
            min_cord = all_cord[i]
            min_distance = current_distance

    return min_cord


def closest_split_pair(x, y, g):
    x_median = statistics.median(x)
    # filtered y coordinates (need to go through y coordinates and filter it)
    Sy = []

    # needs to go through the x and y coordinates
    coordinates = list(zip(x, y))
    print("my coordinates")
    print(coordinates)
    for i in range(len(coordinates)):
        if coordinates[i][0] >= coordinates[i][0] - g and coordinates[i][0] <= coordinates[i][0] + g:
            Sy.append(coordinates[i])

    print("this is Sy")
    print(Sy)

    best = g
    bestPair = None
    l = len(x)
    for i in range(l):
        for j in range(min(7, l-i)):
            if math.sqrt((Sy[i][0]-Sy[i+j][0]) ** 2 + (Sy[i][1]-Sy[i+j][1])**2) < best:
                print("hola")
                best = math.sqrt((Sy[i][0]-Sy[i+j][0]) **
                                 2 + (Sy[i][1]-Sy[i+j][1])**2)
                bestPair = (Sy[i], Sy[i+j])

    return bestPair


    # Runner code
x, y = create_coordinates()
A = list(zip_coordinates(x, y))
print(closest_pair(x, y))

# show on graph
plt.scatter(x, y)
plt.show()
