def merge_sort(A):
    n = len(A)

    # Base Case
    if n == 0 or n == 1:
        return A, 0

    # Recursive Calls
    else:
        C = A[:n//2]  # left half of array
        D = A[n//2:]  # right half of array

        # MERGE SORT ON LEFT SUBARRAY returns C sorted and inversions from left subarray
        C, left_inversions_count = merge_sort(C)

        # MERGE SORT ON RIGHT SUBARRAY returns D sorted and inversions from right subarray
        D, right_inversions_count = merge_sort(D)

        # returns B (sorting C and D while merging ) and inversions
        A, merged_inversions_count = merge(C, D)

        # total # of inversions from the left subarray, right subarray, and merged array
        total_inversions_count = left_inversions_count + \
            right_inversions_count + merged_inversions_count

        # returns sorted merged array and total # of inversions from left, right, and merge subarray
        return A, total_inversions_count


def merge(C, D):
    sorted_merged_arr = []
    i = 0  # traverse C
    j = 0  # traverse D
    split_inversions = 0
    length = len(C)+len(D)

    while i < len(C) and j < len(D):
        if C[i] <= D[j]:
            sorted_merged_arr.append(C[i])
            i += 1
        else:
            sorted_merged_arr.append(D[j])
            j += 1
            split_inversions += ((length//2) - i)

    # remaining elements
    while i < len(C):
        sorted_merged_arr.append(C[i])
        i += 1

    while j < len(D):
        sorted_merged_arr.append(D[j])
        split_inversions += ((length//2) - i)
        j += 1

    print('1st left subarray:', C)
    print('2nd right subarray:', D)
    print('merged sorted subarray: ', sorted_merged_arr)
    print('inversion count: ', split_inversions)
    print("\n")
    return sorted_merged_arr, split_inversions


#A2 = [2, 3, 5, 7, 0, 1, 4, 6]
A3 = [4, 2, 1, 7, 6, 5, 3, 0]
print('sorted array, total split inversions: ', merge_sort(A3))
