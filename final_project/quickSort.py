import random


def quicksort(A, left, right):
    if left >= right:
        return

    pivot = A[(left+right)//2]  # middle pivot point - O(nlogn)
    # pivot = A[left]  # left pivot point - worst case is O(n^2)
    # pivot = A[random.randint(left, right)]  # random pivot point - O(nlogn)
    # pivot = A[right]  # right pivot point - worst case is O(n^2)
    index = partition(A, left, right, pivot)

    # recursively call on left and right
    quicksort(A, left, index-1)
    quicksort(A, index, right)
    return A


def partition(A, left, right, pivot):

    while left <= right:

        while A[left] < pivot:
            left = left + 1

        while A[right] > pivot:
            right = right - 1

        if left <= right:
            A[left], A[right] = A[right], A[left]
            left = left + 1
            right = right - 1

    return left


A = [9, 2, 6, 4, 3, 5, 1]
print("Original list:", A)
print("Sorted list:", quicksort(A, 0, len(A)-1))
