# What is an inversion?
# An inversion is when a[i] > a[j] and i < j
# Time complexity: O(n^2)

def count_inversions_from_two_sorted_arr(C, D):
    merged_arr = []
    midpoint = (len(C) + len(D)) // 2
    split_inversions_count = 0
    i = 0
    j = 0

    # go through both sorted arrays
    while i < len(C) and j < len(D):
        if C[i] < D[j]:
            merged_arr.append(C[i])
            i += 1
        else:
            merged_arr.append(D[j])
            split_inversions_count += (midpoint - i)
            j += 1

    # remaining elements
    while i < len(C):
        merged_arr.append(C[i])
        i += 1

    while j < len(D):
        merged_arr.append(D[j])
        split_inversions_count += (midpoint - i)
        j += 1

    return merged_arr, split_inversions_count


C = [1, 2, 4, 7]
D = [0, 3, 5, 6]
print(count_inversions_from_two_sorted_arr(C, D))
