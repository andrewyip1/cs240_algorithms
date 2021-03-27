""" Write a function that will take an array of size n and return the number of inversions by 
using the brute force method. Test for A = [ 3 2 1 5 10 6 4 8 7 9 ] """
# What is an inversion?
# An inversion is when a[i] > a[j] and i < j
# Time complexity: O(n^2)


def brute_force_num_inversions(A):
    n = len(A)
    count = 0
    for i in range(n-1):  # slow pointer
        for j in range(i+1, n):  # fast pointer
            if A[i] > A[j]:
                count += 1
    return count


A = [1, 2, 4, 7, 0, 3, 5, 6]
print(brute_force_num_inversions(A))
