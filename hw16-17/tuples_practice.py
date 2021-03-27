import random
import decimal


def create_lists():
    x = []
    y = []

    for i in range(10):

        # x and y coordinate
        x_cord = round(random.uniform(-1, 1), 2)
        y_cord = round(random.uniform(-1, 1), 2)

        # appending it to list of coordinates
        x.append(x_cord)
        y.append(y_cord)

    coordinates = zip(x, y)
    return coordinates


def sort_by_x(A):
    A.sort(key=lambda x: x[0])
    return A


A = list(create_lists())
print("First coordinate: ", A[0])
print("Last coordinate: ", A[len(A)-1])

# sorted by x value
A = sort_by_x(A)  # reassigning list
for i in range(2, 8, 1):
    print("i =", i, A[i])
