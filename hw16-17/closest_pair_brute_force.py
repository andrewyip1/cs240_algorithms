import math


def closest_pair_brute_force(A):

    min_distance = float("inf")
    first_coordinate = [(0, 0)]
    second_coordinate = [(0, 0)]

    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            current_distance = math.sqrt((A[j][0] - A[i][0]) **
                                         2 + (A[j][1] - A[i][1])**2)

            if current_distance < min_distance:
                min_distance = current_distance
                first_coordinate[0] = (A[j][0], A[j][1])
                second_coordinate[0] = (A[i][0], A[i][1])

    res1 = "first coordinate", first_coordinate
    res2 = "second coordinate", second_coordinate
    res3 = "distance between the two points: ", min_distance

    return res1, res2, res3


A = [(0, 2.1), (-1.3, 4.3), (5.7, 9), (-5, 4), (2.4, 6)]
print(closest_pair_brute_force(A))
