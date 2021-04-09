import math


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
    return target[0], target[1], minDistance


A = [(0, 2.1), (-1.3, 4.3), (5.7, 9), (-5, 4), (2.4, 6)]
print(bruteForce(A))
