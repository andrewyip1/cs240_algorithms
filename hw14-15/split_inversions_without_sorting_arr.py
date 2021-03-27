# What is an inversion?
# An inversion is when a[i] > a[j] and i < j
# Time complexity: O(nlogn)

def merge_sort(A):

    # Base Case
    if len(A) == 1 or len(A) == 0:
        return 0
    else:

        # left and right half of the array
        C = A[:len(A)//2]
        D = A[len(A)//2:]

        # Recursive calls
        left_inversions = merge_sort(C)
        right_inversions = merge_sort(D)
        total_inversions = find_inversions(A)

        # Display statements
        print("left subarray:", C)
        print("inversions in left sub array:", left_inversions)
        print("right subarray:", D)
        print("inversions in right sub array:", right_inversions)
        print("subarray:", A)
        print("total inversions in sub array:", total_inversions)
        print("\n")

        return total_inversions

# Finding inversions with an unsorted array


def find_inversions(A):
    n = len(A)
    count = 0
    for i in range(n-1):  # checking the array
        for j in range(i+1, n):  # checking the right side
            if A[i] > A[j]:
                count += 1
    return count


A = [4, 2, 1, 7, 6, 5, 3, 0]
print("# of inversions in ", A, "is", merge_sort(A))
